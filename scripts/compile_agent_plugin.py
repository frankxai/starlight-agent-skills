#!/usr/bin/env python3
"""Agent Plugin Compiler (Agent Plugins 1.0 Standard).

Compiles a curated skill lane into vendor-neutral Agent Plugins (plugin.json),
with native compatibility projections for OpenAI Codex, Claude Code, Cursor,
and Google Antigravity.

Usage:
  python compile_agent_plugin.py --lane creator --src ../creator-skills --out ../plugins/starlight-creator
  python compile_agent_plugin.py --repo ../skills --name starlight-architect
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import sys

FM_REGEX = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", re.DOTALL)


def extract_skill_meta(skill_md: Path) -> dict | None:
    try:
        content = skill_md.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None
    m = FM_REGEX.match(content)
    slug = skill_md.parent.name
    if not m:
        return {"name": slug, "description": f"Specialist capability: {slug}"}
    fm_raw = m.group(1)
    name = slug
    desc = ""
    for line in fm_raw.splitlines():
        if line.strip().startswith("name:"):
            name = line.split(":", 1)[1].strip().strip('"').strip("'")
        elif line.strip().startswith("description:"):
            desc = line.split(":", 1)[1].strip().strip('"').strip("'")
    return {"name": name or slug, "description": desc or f"Specialist capability: {slug}"}


def compile_plugin(
    repo_root: Path,
    plugin_name: str,
    title: str,
    description: str,
    out_dir: Path,
    keywords: list[str] | None = None
) -> dict:
    skills_dir = repo_root / "skills"
    if not skills_dir.is_dir():
        raise ValueError(f"Skills directory not found at {skills_dir}")

    skill_entries = []
    for smd in sorted(skills_dir.rglob("SKILL.md")):
        rel = smd.relative_to(repo_root)
        rel_str = str(rel.parent).replace("\\", "/")
        meta = extract_skill_meta(smd)
        if meta:
            skill_entries.append({
                "path": rel_str,
                "name": meta["name"],
                "description": meta["description"]
            })

    out_dir.mkdir(parents=True, exist_ok=True)

    # 1. Standard Agent Plugins 1.0 manifest
    agent_plugin = {
        "$schema": "https://agent-plugins.org/schemas/plugin.v1.json",
        "name": plugin_name,
        "version": "1.0.0",
        "description": description,
        "author": {
            "name": "Frank Riemer",
            "url": "https://frankx.ai",
            "github": "frankxai"
        },
        "homepage": f"https://github.com/frankxai/{repo_root.name}",
        "repository": {
            "type": "git",
            "url": f"https://github.com/frankxai/{repo_root.name}.git"
        },
        "license": "MIT",
        "keywords": keywords or ["agent-skills", "agent-plugins", "starlight"],
        "skills": "./skills",
        "runtimes": {
            "codex": {"supported": True, "skills_dir": "./skills"},
            "claude": {"supported": True, "skills_dir": "./skills"},
            "grok": {"supported": True, "skills_dir": "./skills"},
            "antigravity": {"supported": True, "skills_dir": "./skills"},
            "cursor": {"supported": True, "skills_dir": "./skills"}
        }
    }

    # 2. Codex plugin projection
    codex_plugin = {
        "name": plugin_name,
        "version": "1.0.0",
        "description": description,
        "author": "Frank Riemer",
        "skills": [s["path"] for s in skill_entries]
    }

    # 3. Claude plugin projection
    claude_plugin = {
        "name": plugin_name,
        "version": "1.0.0",
        "description": description,
        "author": "Frank Riemer",
        "skills": "./skills"
    }

    # Write files
    (out_dir / "plugin.json").write_text(json.dumps(agent_plugin, indent=2) + "\n", encoding="utf-8")
    
    codex_dir = out_dir / ".codex-plugin"
    codex_dir.mkdir(parents=True, exist_ok=True)
    (codex_dir / "plugin.json").write_text(json.dumps(codex_plugin, indent=2) + "\n", encoding="utf-8")

    claude_dir = out_dir / ".claude-plugin"
    claude_dir.mkdir(parents=True, exist_ok=True)
    (claude_dir / "plugin.json").write_text(json.dumps(claude_plugin, indent=2) + "\n", encoding="utf-8")

    return {
        "plugin_name": plugin_name,
        "skills_count": len(skill_entries),
        "output_directory": str(out_dir)
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True, help="Path to skills repository root")
    parser.add_argument("--name", type=str, required=True, help="Plugin package name (e.g. starlight-creator)")
    parser.add_argument("--title", type=str, default="", help="Human title")
    parser.add_argument("--desc", type=str, default="", help="Plugin description")
    parser.add_argument("--out", type=Path, default=None, help="Output directory")
    args = parser.parse_args()

    out_dir = args.out or args.repo
    res = compile_plugin(
        repo_root=args.repo.resolve(),
        plugin_name=args.name,
        title=args.title or args.name,
        description=args.desc or f"Portable Agent Skills bundle: {args.name}",
        out_dir=out_dir.resolve()
    )
    print(f"Compiled {res['skills_count']} skills into {res['output_directory']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
