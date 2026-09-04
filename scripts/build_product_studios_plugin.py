#!/usr/bin/env python3
"""Compile canonical studio capabilities into the distributable Codex plugin."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugins" / "starlight-product-studios"
PLUGIN_SKILLS = PLUGIN_ROOT / "skills"
STUDIOS = (
    "publishing-studio",
    "template-studio",
    "software-studio",
    "media-studio",
    "world-experience-studio",
)
DIRECTOR_FRONTMATTER = """---
name: product-studio-director
description: "Assign one primary specialist studio and compose bounded cross-studio contributions into one canonical release. Use when a product spans publishing, templates, software, media, or world experiences."
metadata: {"version":"0.1.0","domain":"studios","tags":"orchestration,routing,product-studio,release-governance"}
---

"""


def expected_files() -> dict[Path, bytes]:
    files: dict[Path, bytes] = {}
    for studio in STUDIOS:
        source = ROOT / "skills" / "studios" / studio
        if not (source / "SKILL.md").is_file():
            raise RuntimeError(f"canonical studio is missing: {source}")
        for path in source.rglob("*"):
            if path.is_file():
                relative = Path("skills") / studio / path.relative_to(source)
                files[relative] = path.read_bytes()

    agent_path = ROOT / "agents" / "product-studio-director" / "AGENT.md"
    agent_text = agent_path.read_text(encoding="utf-8")
    parts = agent_text.split("---", 2)
    if len(parts) != 3:
        raise RuntimeError("product-studio-director has invalid frontmatter")
    director = (DIRECTOR_FRONTMATTER + parts[2].lstrip("\n")).encode("utf-8")
    files[Path("skills/product-studio-director/SKILL.md")] = director
    return files


def compile_plugin(files: dict[Path, bytes]) -> None:
    resolved = PLUGIN_SKILLS.resolve(strict=False)
    if resolved.parent != PLUGIN_ROOT.resolve() or PLUGIN_ROOT.name != "starlight-product-studios":
        raise RuntimeError("refusing to replace an unexpected plugin path")
    if PLUGIN_SKILLS.exists():
        shutil.rmtree(PLUGIN_SKILLS)
    for relative, content in files.items():
        destination = PLUGIN_ROOT / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)
    print(f"Compiled {len(files)} files into {PLUGIN_ROOT.relative_to(ROOT)}.")


def check_plugin(files: dict[Path, bytes]) -> None:
    actual = {
        path.relative_to(PLUGIN_ROOT): path.read_bytes()
        for path in PLUGIN_SKILLS.rglob("*")
        if path.is_file()
    } if PLUGIN_SKILLS.is_dir() else {}
    missing = sorted(set(files) - set(actual))
    extra = sorted(set(actual) - set(files))
    changed = sorted(path for path in set(files) & set(actual) if files[path] != actual[path])
    if missing or extra or changed:
        for label, paths in (("missing", missing), ("extra", extra), ("changed", changed)):
            for path in paths:
                print(f"ERROR: plugin projection {label}: {path}", file=sys.stderr)
        raise SystemExit(1)
    print(f"Plugin projection current ({len(files)} files, {len(STUDIOS)} studios + director).")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail when compiled files drift")
    args = parser.parse_args()
    files = expected_files()
    if args.check:
        check_plugin(files)
    else:
        compile_plugin(files)


if __name__ == "__main__":
    main()
