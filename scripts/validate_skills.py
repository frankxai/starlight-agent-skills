#!/usr/bin/env python3
"""Validate every SKILL.md against the Starlight Agent Skills frontmatter spec.

Checks, for each `SKILL.md` under `skills/`:
  * YAML frontmatter is present and well-formed
  * `name` exists, is <= 64 chars, and matches ^[a-z0-9][a-z0-9-]*$
  * `description` exists and is non-empty (<= 1024 chars)
  * `version` exists and looks like semver (X.Y.Z)
  * `domain` exists and is one of the known domains
  * the file is not empty

Exit code is non-zero if any skill fails, so this can run in CI.

Adapted from frankxai/claude-skills-library scripts/validate_skills.py.
"""
from __future__ import annotations
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(__file__), "..", "skills")
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
DOMAINS = {"research", "media", "education", "coding", "brand", "cosmos"}
# Frontmatter block: tolerant of a BOM and of the closing `---` having no trailing newline.
FM_RE = re.compile("^﻿?---\\s*\n(.*?)\n?---", re.S)


def parse_frontmatter(text: str) -> dict | None:
    m = FM_RE.match(text)
    if not m:
        return None
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if kv:
            fm[kv.group(1)] = kv.group(2).strip().strip('"')
    return fm


def main() -> int:
    errors: list[str] = []
    count = 0
    for dirpath, _dirs, files in os.walk(ROOT):
        for fn in files:
            if fn.lower() != "skill.md":
                continue
            count += 1
            path = os.path.relpath(os.path.join(dirpath, fn), os.path.join(ROOT, ".."))
            with open(os.path.join(dirpath, fn), encoding="utf-8") as f:
                text = f.read()
            if not text.strip():
                errors.append(f"{path}: file is empty")
                continue
            fm = parse_frontmatter(text)
            if fm is None:
                errors.append(f"{path}: missing or malformed YAML frontmatter")
                continue
            name = fm.get("name", "")
            if not name:
                errors.append(f"{path}: missing 'name'")
            elif not NAME_RE.match(name):
                errors.append(f"{path}: 'name' must match ^[a-z0-9][a-z0-9-]*$ (got {name!r})")
            elif len(name) > 64:
                errors.append(f"{path}: 'name' exceeds 64 characters")
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
            # Attestation footer is required for ecosystem skills.
            if "Built on SIP" not in text:
                errors.append(f"{path}: missing 'Built on SIP' attestation footer")

    if errors:
        print(f"FAIL: {len(errors)} issue(s) across {count} skill file(s):\n")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK: {count} skill file(s) are spec-compliant.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
