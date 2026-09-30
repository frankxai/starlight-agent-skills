#!/usr/bin/env python3
"""Compile two skills-only plugins from the canonical operator capabilities."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
OPERATORS = {
    "starlight": ("Starlight", "Execute bounded work with verified evidence.",
                  "Implement the next tested, reviewable Starlight change."),
    "starlight-queen": ("Starlight Queen", "Coordinate agent work, decisions and evidence.",
                        "Review agent work and prepare the next bounded assignment."),
}


def safe_checkout_path(path: Path) -> None:
    path.relative_to(ROOT)
    if not path.resolve().is_relative_to(ROOT.resolve()):
        raise ValueError("path escapes checkout")
    cursor = path
    while cursor != ROOT:
        if cursor.is_symlink():
            raise ValueError("symlinked source or projection ancestor")
        cursor = cursor.parent


def manifest(name: str) -> dict:
    display, short, prompt = OPERATORS[name]
    return {
        "name": name, "version": "0.1.0", "description": short,
        "author": {"name": "FrankX / Starlight Intelligence", "url": "https://github.com/frankxai"},
        "homepage": f"https://github.com/frankxai/starlight-agent-skills/tree/main/plugins/{name}",
        "repository": "https://github.com/frankxai/starlight-agent-skills", "license": "MIT",
        "keywords": ["starlight", "operations", "agents", "evidence"], "skills": "./skills/",
        "interface": {
            "displayName": display, "shortDescription": short,
            "longDescription": "Portable operator procedure using host-provided tools. Includes no live MCP endpoint, credentials or runtime activation.",
            "developerName": "FrankX / Starlight Intelligence", "category": "Productivity",
            "capabilities": ["Write", "Code"], "websiteURL": "https://github.com/frankxai/starlight-agent-skills",
            "defaultPrompt": [prompt], "brandColor": "#7FFFD4",
        },
    }


def skill_files(name: str, personal: bool = False) -> dict[Path, bytes]:
    if name not in OPERATORS:
        raise ValueError("unknown generated package")
    source = ROOT / "skills" / "substrate" / name
    safe_checkout_path(source)
    files = {}
    paths = [source / "SKILL.md"]
    for folder in ("agents", "references", "scripts"):
        safe_checkout_path(source / folder)
        paths.extend((source / folder).rglob("*"))
    for path in paths:
        if "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        if path.is_symlink():
            raise ValueError("canonical skill cannot contain symlinks")
        if not path.is_file():
            continue
        safe_checkout_path(path)
        if not path.resolve().is_relative_to(source.resolve()):
            raise ValueError("file escapes canonical skill")
        content = path.read_bytes()
        if personal and path.name == "SKILL.md":
            # Personal host permits name/description only; preserve the body exactly.
            text = content.decode("utf-8")
            front, body = text[4:].split("\n---\n", 1)
            front = "\n".join(line for line in front.splitlines() if not line.startswith("metadata:"))
            content = ("---\n" + front + "\n---\n" + body).encode("utf-8")
        files[path.relative_to(source)] = content
    if Path("SKILL.md") not in files:
        raise ValueError("missing canonical skill")
    return files


def expected_files(name: str) -> dict[Path, bytes]:
    files = {Path("skills") / name / path: data for path, data in skill_files(name).items()}
    files[Path(".codex-plugin/plugin.json")] = (json.dumps(manifest(name), indent=2) + "\n").encode()
    return files


def check_files(root: Path, expected: dict[Path, bytes], personal_ui_overlay: bool = False) -> None:
    if root.is_symlink():
        raise ValueError("projection root cannot be a symlink")
    actual = {}
    for path in root.rglob("*"):
        if "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        if path.is_symlink():
            raise ValueError("projection cannot contain symlinks")
        if path.is_file():
            actual[path.relative_to(root)] = path.read_bytes()
    if personal_ui_overlay:
        # The personal host enriches presentation after installation. These two
        # files are not runtime instructions and are not authored back into canon.
        if Path("agents/openai.yaml") not in actual:
            raise ValueError("missing personal UI metadata")
        expected = {p: b for p, b in expected.items() if p != Path("agents/openai.yaml")}
        actual = {p: b for p, b in actual.items() if p not in {Path("agents/openai.yaml"), Path("assets/icon.svg")}}
    failures = [("missing", p) for p in expected.keys() - actual.keys()]
    failures += [("extra", p) for p in actual.keys() - expected.keys()]
    failures += [("changed", p) for p in expected.keys() & actual.keys() if expected[p] != actual[p]]
    if failures:
        for reason, path in sorted(failures):
            print(f"ERROR: {reason}: {path}", file=sys.stderr)
        raise ValueError("projection drift")


def compile_plugin(name: str) -> None:
    if name not in OPERATORS:
        raise ValueError("unknown generated package")
    root = ROOT / "plugins" / name
    safe_checkout_path(root)
    # Only these two generated packages are replaceable. Existing studio package is untouched.
    files = expected_files(name)
    if root.exists():
        shutil.rmtree(root)
    for relative, content in files.items():
        destination = root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)
    print(f"Compiled {name}: {len(files)} files.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--check-personal", choices=OPERATORS)
    parser.add_argument("--personal-root", type=Path, help="exact existing personal skill directory")
    args = parser.parse_args()
    try:
        if args.check_personal:
            if not args.personal_root:
                parser.error("--check-personal requires --personal-root")
            check_files(args.personal_root, skill_files(args.check_personal, personal=True), personal_ui_overlay=True)
            print(f"Personal projection current: {args.check_personal}.")
        else:
            for name in OPERATORS:
                if args.check:
                    check_files(ROOT / "plugins" / name, expected_files(name))
                    print(f"Plugin projection current: {name}.")
                else:
                    compile_plugin(name)
        return 0
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
