#!/usr/bin/env python3
"""Generate docs/CATALOG.md from the frontmatter of every SKILL.md.

Skills are grouped by `metadata.domain` (the canonical taxonomy), falling back
to a path-derived domain for catalog diagnostics. Run this whenever skills are
added or renamed:

    python3 scripts/generate_catalog.py

Adapted from frankxai/claude-skills-library scripts/generate_catalog.py.
"""
from __future__ import annotations
import collections
import json
import os
import re

HERE = os.path.dirname(__file__)
ROOT = os.path.normpath(os.path.join(HERE, "..", "skills"))
REPO = os.path.normpath(os.path.join(HERE, ".."))
OUT = os.path.join(REPO, "docs", "CATALOG.md")

FM_RE = re.compile("^﻿?---\\s*\n(.*?)\n?---", re.S)

# Canonical domain order + human label.
DOMAIN_ORDER = [
    ("substrate", "🧩 Substrate (income · payments · swarm)"),
    ("cosmos", "🌌 Cosmos (flagship pack)"),
    ("research", "🔬 Research"),
    ("media", "🎬 Media"),
    ("education", "🎓 Education"),
    ("coding", "💻 Coding"),
    ("brand", "✨ Brand & Voice"),
]


def parse_frontmatter(path: str) -> dict:
    """Parse the supported single-line frontmatter fields for one skill."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = FM_RE.match(text)
    fm: dict[str, object] = {}
    if m:
        for line in m.group(1).splitlines():
            kv = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$", line)
            if kv:
                key = kv.group(1)
                value = kv.group(2).strip()
                if key == "metadata":
                    try:
                        parsed = json.loads(value)
                    except json.JSONDecodeError:
                        parsed = {}
                    fm[key] = parsed if isinstance(parsed, dict) else {}
                else:
                    fm[key] = value.strip('"')
    return fm


def collect() -> dict[str, tuple[str, str, str, str]]:
    """Collect catalog rows keyed by portable skill identifier."""
    skills: dict[str, tuple[str, str, str, str]] = {}
    for dirpath, _dirs, files in os.walk(ROOT):
        for fn in files:
            if fn != "SKILL.md":
                continue
            p = os.path.join(dirpath, fn)
            fm = parse_frontmatter(p)
            name = fm.get("name")
            if not isinstance(name, str) or not name:
                continue
            rel = os.path.relpath(p, REPO).replace(os.sep, "/")
            metadata = fm.get("metadata") if isinstance(fm.get("metadata"), dict) else {}
            # Canonical metadata domain, with path fallback for diagnostics.
            domain = metadata.get("domain") or rel.split("/")[1]
            description = fm.get("description", "") if isinstance(fm.get("description"), str) else ""
            version = metadata.get("version") or ""
            skills[name] = (rel, description, str(domain), str(version))
    return skills


def main() -> None:
    """Regenerate the checked-in skill catalog from current skill sources."""
    skills = collect()
    grouped: dict[str, list[tuple[str, str, str, str]]] = collections.defaultdict(list)
    for name, (rel, desc, domain, ver) in sorted(skills.items()):
        grouped[domain].append((name, rel, desc, ver))

    total = len(skills)
    lines = [
        "# 🛰️ Starlight Agent Skills — Catalog\n",
        f"\nThe complete index of all **{total} skills** in this library. "
        "Every skill ships as a self-contained, rich-portable package: a canonical `SKILL.md` "
        "(spec-compliant frontmatter), an optional `manifest.json`, and optional `examples/` + "
        "`tests/`. Skills run across Claude Code, Codex, Cursor, Gemini, OpenCode, and the "
        "Starlight Intelligence System — see [`adapters/`](../adapters/).\n",
        "\n> This file is generated. After adding or renaming a skill, run "
        "`python3 scripts/generate_catalog.py` to regenerate it, then "
        "`python3 scripts/validate_skills.py` to verify compliance.\n",
    ]
    ordered = DOMAIN_ORDER + [
        (d, d.title()) for d in sorted(grouped) if d not in {k for k, _ in DOMAIN_ORDER}
    ]
    for key, label in ordered:
        items = grouped.get(key)
        if not items:
            continue
        lines.append(f"\n## {label}\n")
        lines.append(f"\n_{len(items)} skill{'s' if len(items) != 1 else ''}_\n")
        lines.append("\n| Skill | Version | Description |\n|---|---|---|\n")
        for name, rel, desc, ver in items:
            d = desc.replace("|", "\\|")
            if len(d) > 160:
                d = d[:157].rstrip() + "..."
            # CATALOG.md lives in docs/, so prefix ../ to reach repo-root skills/.
            folder = "../" + rel.rsplit("/", 1)[0]
            lines.append(f"| [`{name}`]({folder}) | {ver} | {d} |\n")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write("".join(lines))
    print(f"Wrote {OUT} with {total} skills across "
          f"{sum(1 for key, _ in ordered if grouped.get(key))} domains.")


if __name__ == "__main__":
    main()
