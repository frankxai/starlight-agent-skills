#!/usr/bin/env python3
"""Validate every SKILL.md against the Starlight Agent Skills spec.

For each `SKILL.md` under `skills/<domain>/<name>/`:
  * YAML frontmatter is present and single-line (block scalars / multi-line
    values are rejected — keep `description` a single quoted line)
  * `name` matches ^[a-z0-9][a-z0-9-]*$, is <= 64 chars, AND equals the folder name
  * `description` is non-empty and <= 1024 chars
  * `version` is semver X.Y.Z
  * `domain` is a known domain AND equals the parent folder
  * the "Built on SIP" attestation footer is present

If a sibling `manifest.json` exists, it must be valid JSON and agree with the
SKILL.md / folder: `name`, `domain`, `version` match, and `id` == "<domain>/<name>".

Exit code is non-zero if any skill fails, so this can run in CI.
Zero third-party dependencies (standard library only).
"""
from __future__ import annotations
import json
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(__file__), "..", "skills")
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
DOMAINS = {"research", "media", "education", "coding", "brand", "cosmos"}
# Frontmatter block: tolerant of a BOM and of the closing `---` having no trailing newline.
FM_RE = re.compile("^﻿?---\\s*\n(.*?)\n?---", re.S)


def parse_frontmatter(text: str) -> tuple[dict | None, str | None]:
    """Return (fields, error). Enforces simple single-line `key: value` frontmatter.

    Block scalars (`>` / `|`) and indented continuation/list lines are rejected
    rather than silently mis-parsed, so a malformed value can never pass as valid.
    """
    m = FM_RE.match(text)
    if not m:
        return None, "missing or malformed YAML frontmatter"
    fm: dict[str, str] = {}
    for raw in m.group(1).splitlines():
        if not raw.strip():
            continue
        if raw[:1] in (" ", "\t", "-"):
            return None, f"frontmatter must be single-line `key: value` (offending line: {raw.strip()!r})"
        kv = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", raw)
        if not kv:
            return None, f"unparseable frontmatter line: {raw.strip()!r}"
        key, val = kv.group(1), kv.group(2).strip()
        if val in (">", "|") or val.startswith((">", "|")) and val[1:].strip() in ("", "-", "+"):
            return None, f"block scalars are not allowed for {key!r}; use a single quoted line"
        # Strip one layer of matching surrounding quotes only.
        if len(val) >= 2 and val[0] == val[-1] and val[0] in ("'", '"'):
            val = val[1:-1]
        fm[key] = val
    return fm, None


def validate_manifest(skill_dir: str, name: str, domain: str, version: str, path: str, errors: list[str]) -> None:
    mpath = os.path.join(skill_dir, "manifest.json")
    if not os.path.exists(mpath):
        return
    try:
        with open(mpath, encoding="utf-8") as f:
            man = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        errors.append(f"{path}: sibling manifest.json is not valid JSON ({e})")
        return
    checks = {
        "name": (man.get("name"), name),
        "domain": (man.get("domain"), domain),
        "version": (man.get("version"), version),
        "id": (man.get("id"), f"{domain}/{name}"),
    }
    for field, (got, want) in checks.items():
        if got != want:
            errors.append(f"{path}: manifest.json {field}={got!r} disagrees with SKILL.md/folder ({want!r})")


def main() -> int:
    errors: list[str] = []
    count = 0
    for dirpath, _dirs, files in os.walk(ROOT):
        # Exact filename — a stray `Skill.md` should not pass on case-insensitive FS.
        if "SKILL.md" not in files:
            continue
        count += 1
        skill_dir = dirpath
        folder = os.path.basename(dirpath)
        parent = os.path.basename(os.path.dirname(dirpath))
        path = os.path.relpath(os.path.join(dirpath, "SKILL.md"), os.path.join(ROOT, ".."))
        with open(os.path.join(dirpath, "SKILL.md"), encoding="utf-8") as f:
            text = f.read()
        if not text.strip():
            errors.append(f"{path}: file is empty")
            continue
        fm, fm_err = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{path}: {fm_err}")
            continue

        name = fm.get("name", "")
        if not name:
            errors.append(f"{path}: missing 'name'")
        elif not NAME_RE.match(name):
            errors.append(f"{path}: 'name' must match ^[a-z0-9][a-z0-9-]*$ (got {name!r})")
        elif len(name) > 64:
            errors.append(f"{path}: 'name' exceeds 64 characters")
        elif name != folder:
            errors.append(f"{path}: 'name' ({name!r}) must equal the folder name ({folder!r})")

        desc = fm.get("description", "")
        if not desc:
            errors.append(f"{path}: missing 'description'")
        elif len(desc) > 1024:
            errors.append(f"{path}: 'description' exceeds 1024 characters")

        version = fm.get("version", "")
        if not version:
            errors.append(f"{path}: missing 'version'")
        elif not SEMVER_RE.match(version):
            errors.append(f"{path}: 'version' must be semver X.Y.Z (got {version!r})")

        domain = fm.get("domain", "")
        if not domain:
            errors.append(f"{path}: missing 'domain'")
        elif domain not in DOMAINS:
            errors.append(f"{path}: 'domain' must be one of {sorted(DOMAINS)} (got {domain!r})")
        elif domain != parent:
            errors.append(f"{path}: 'domain' ({domain!r}) must equal the parent folder ({parent!r})")

        if "Built on SIP" not in text:
            errors.append(f"{path}: missing 'Built on SIP' attestation footer")

        # Cross-validate the optional manifest only when the core fields are sane.
        if name and domain:
            validate_manifest(skill_dir, name, domain, version, path, errors)

    if errors:
        print(f"FAIL: {len(errors)} issue(s) across {count} skill file(s):\n")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK: {count} skill file(s) are spec-compliant.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
