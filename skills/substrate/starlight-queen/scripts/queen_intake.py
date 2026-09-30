#!/usr/bin/env python3
"""Offline metadata normalization and strict Queen packet review; stdout only.

This is neither an authority service nor a dispatcher. No network, subprocess,
credential reads, queue writes, or canonical Registry mutations are performed.
"""
from __future__ import annotations

import argparse
import copy
from datetime import datetime
import hashlib
import json
import math
import os
import stat
from pathlib import Path, PurePosixPath
import re
import sys

MAX_BYTES = 1024 * 1024
MAX_OBSERVATIONS = 1000
ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,127}\Z")
UTC = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3}Z\Z")
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
REQUIRED = {
    "envelope", "kind", "id", "slug", "producer", "status", "createdAt",
    "agent", "priority", "maxMinutes", "repo", "risk", "prompt",
}
OPTIONAL = {
    "idempotencyKey", "needs", "allowedChecks", "requiredChecks", "baseRef",
    "assignedRef", "requiredAncestors", "snapshotPaths",
}


class IntakeError(ValueError):
    pass


def require(condition: bool, reason: str) -> None:
    if not condition:
        raise IntakeError(reason)


def keys(value: object, required: set[str], optional: set[str] | None = None) -> dict:
    require(isinstance(value, dict), "expected an object")
    require(required <= value.keys(), "missing required fields")
    require(value.keys() <= required | (optional or set()), "unknown fields")
    return value


def string(value: object, limit: int = 128) -> str:
    require(isinstance(value, str) and 0 < len(value) <= limit and bool(value.strip()),
            "invalid or oversized string")
    require(not any((ord(c) < 32 and c not in "\n\t") or ord(c) == 127 for c in value), "control characters")
    return value


def identifier(value: object) -> str:
    require(isinstance(value, str) and bool(ID.fullmatch(value)), "invalid opaque ID")
    return value


def timestamp(value: object) -> str:
    require(isinstance(value, str) and bool(UTC.fullmatch(value)), "timestamp must be UTC ISO milliseconds")
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise IntakeError("invalid timestamp") from exc
    return value


def scope(value: object) -> dict:
    obj = keys(value, {"tenant", "project", "repository"})
    for item in obj.values():
        # Repository keys may be owner/name; paths, URLs and credentials do not belong here.
        require(isinstance(item, str) and bool(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._/-]{0,127}", item))
                and ".." not in item and "//" not in item, "invalid scope ID")
    return obj


def canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)


def digest(value: object) -> str:
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()


def normalize_evidence(document: object, selected_scope: object) -> dict:
    """Scope selection is supplied independently; matching is not authorization."""
    doc = keys(document, {"schema", "scope", "observations"})
    require(doc["schema"] == "starlight.operator_intake.v1", "unsupported intake schema")
    selected = scope(selected_scope)
    require(scope(doc["scope"]) == selected, "scope mismatch")
    items = doc["observations"]
    require(isinstance(items, list) and 0 < len(items) <= MAX_OBSERVATIONS, "invalid observation count")
    seen: dict[tuple[str, str, str], str] = {}
    out = []
    for item in items:
        row = keys(item, {"source", "id", "scope", "kind", "declared_state", "observed_at", "refs"})
        require(scope(row["scope"]) == selected, "observation scope mismatch")
        for field in ("source", "id", "declared_state"):
            identifier(row[field])
        require(row["kind"] in ("work", "decision", "run", "release"), "unsupported observation kind")
        timestamp(row["observed_at"])
        refs = row["refs"]
        require(isinstance(refs, list) and 0 < len(refs) <= 20, "invalid reference count")
        for ref in refs:
            keys(ref, {"kind", "id"}, {"sha256"})
            identifier(ref["kind"])
            identifier(ref["id"])
            if "sha256" in ref:
                require(isinstance(ref["sha256"], str) and bool(SHA256.fullmatch(ref["sha256"])), "invalid reference hash")
        key = (row["source"], row["kind"], row["id"])
        body = canonical(row)
        if key in seen:
            require(seen[key] == body, "conflicting observation replay; reconcile source versions")
            continue
        seen[key] = body
        # Preserve claims without upgrading them to verified runtime events.
        out.append({**copy.deepcopy(row), "verification": "not_evaluated", "observation_sha256": digest(row)})
    out.sort(key=lambda r: (r["source"], r["kind"], r["id"]))
    return {"schema": "starlight.operator_review.v1", "dispatch": False,
            "scope": copy.deepcopy(selected), "observations": out, "verification": "not_evaluated"}


def strings(value: object, limit: int = 10, item_limit: int = 2048) -> list[str]:
    require(isinstance(value, list) and len(value) <= limit, "invalid array")
    for item in value:
        string(item, item_limit)
    return value


def valid_ref(value: object, assigned: bool = False) -> None:
    text = string(value, 256)
    require(not re.search(r"[\s~^:?*\[\\]|\.\.|@\{|//|^/|/$|\.lock$|\.$", text), "invalid ref")
    parts = text.split("/")
    require(len(parts) >= 2 and all(p and not p.startswith((".", "-")) and not p.endswith(".lock") for p in parts), "invalid ref segments")
    if assigned:
        require(len(parts) >= 4 and parts[1] == "agent", "assigned ref must use remote/agent/harness/slug")


def review_packet(document: object, repo_root: str | Path) -> dict:
    packet = keys(document, REQUIRED, OPTIONAL)
    require(packet["envelope"] == "v1", "unsupported Queen envelope")
    require(packet["kind"] == "task", "only standalone task packets are supported")
    for field in REQUIRED - {"priority", "maxMinutes", "createdAt", "repo", "prompt"}:
        identifier(packet[field])
    require(bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", packet["slug"])), "invalid slug")
    string(packet["prompt"], 16384)
    timestamp(packet["createdAt"])
    require(type(packet["priority"]) is int and abs(packet["priority"]) <= 9007199254740991, "priority must be a safe integer")
    budget = packet["maxMinutes"]
    require(type(budget) in (int, float) and 1 <= budget <= 25 and math.isfinite(budget), "budget must be from 1 to 25 minutes")
    declared = Path(string(packet["repo"], 4096))
    allowed = Path(repo_root)
    require(declared.is_absolute() and allowed.is_absolute(), "repository paths must be explicit and absolute")
    require(declared.is_dir() and allowed.is_dir(), "repository does not exist")
    require(declared.resolve(strict=True) == allowed.resolve(strict=True), "repository mapping mismatch")
    if "idempotencyKey" in packet:
        identifier(packet["idempotencyKey"])
    for field in ("needs", "allowedChecks", "requiredChecks", "requiredAncestors", "snapshotPaths"):
        if field in packet:
            strings(packet[field])
    require(set(packet.get("requiredChecks", [])) <= set(packet.get("allowedChecks", [])), "required check is not allowed")
    for field in ("baseRef", "assignedRef"):
        if field in packet:
            valid_ref(packet[field], assigned=field == "assignedRef")
    for sha in packet.get("requiredAncestors", []):
        require(bool(re.fullmatch(r"[0-9a-fA-F]{40}", sha)), "invalid ancestor SHA")
    for raw in packet.get("snapshotPaths", []):
        rel = PurePosixPath(raw)
        require(not rel.is_absolute() and ".." not in rel.parts and rel != PurePosixPath(".") and "\\" not in raw
                and not re.match(r"^[A-Za-z]:", raw), "unsafe snapshot path")
        require(not any(part == ".git" or part == ".env" or part.startswith(".env.")
                        or part.lower() in {"id_rsa", "id_ed25519", "credentials.json", "credentials.yaml"}
                        for part in rel.parts), "sensitive snapshot path")
        cursor = declared
        for part in rel.parts:
            cursor /= part
            require(not cursor.is_symlink(), "symlinked snapshot path")
        target = (declared / raw).resolve()
        require(target.is_relative_to(declared.resolve(strict=True)), "snapshot path escapes repository")
    if "git-write" in packet.get("needs", []):
        require("assignedRef" in packet, "git-write requires an assigned ref")
        require(bool(packet.get("allowedChecks")), "git-write requires allowed checks")
    return {"schema": "starlight.queen_packet_review.v1", "dispatch": False,
            "authority": "not_evaluated", "verification": "not_evaluated",
            "host_path_scope": "current_host_only", "dispatch_path_validation": "not_evaluated",
            "packet_sha256": digest(packet), "packet": copy.deepcopy(packet)}


def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict:
    out = {}
    for key, value in pairs:
        require(key not in out, "duplicate JSON key")
        out[key] = value
    return out


def read_document(path: Path) -> object:
    # Nonblocking descriptor open prevents FIFO/device paths from hanging on POSIX.
    fd = os.open(path, os.O_RDONLY | getattr(os, "O_NONBLOCK", 0))
    with os.fdopen(fd, "rb") as stream:
        require(stat.S_ISREG(os.fstat(stream.fileno()).st_mode), "input must be a regular file")
        raw = stream.read(MAX_BYTES + 1)
    require(len(raw) <= MAX_BYTES, "input exceeds one MiB")
    def reject_constant(_value: str) -> None:
        raise IntakeError("non-finite JSON number")
    return json.loads(raw, object_pairs_hook=reject_duplicate_keys, parse_constant=reject_constant)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    evidence = sub.add_parser("evidence", help="normalize scoped metadata without crediting completion")
    evidence.add_argument("input", type=Path)
    for field in ("tenant", "project", "repository"):
        evidence.add_argument("--" + field, required=True)
    packet = sub.add_parser("packet", help="review an explicitly mapped envelope without dispatch")
    packet.add_argument("input", type=Path)
    packet.add_argument("--repo-root", required=True)
    args = parser.parse_args(argv)
    try:
        doc = read_document(args.input)
        if args.command == "evidence":
            result = normalize_evidence(doc, {k: getattr(args, k) for k in ("tenant", "project", "repository")})
        else:
            result = review_packet(doc, args.repo_root)
        print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False))
        return 0
    except (IntakeError, OSError, ValueError, TypeError, RuntimeError) as exc:
        # Do not echo source values, paths, credentials or prompt bodies on failures.
        reason = str(exc) if isinstance(exc, IntakeError) else "unreadable or malformed input"
        print(json.dumps({"error": reason, "dispatch": False}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
