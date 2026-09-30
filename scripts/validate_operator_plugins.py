#!/usr/bin/env python3
"""Validate generated operator plugin manifests, source equality and skill sets."""
from __future__ import annotations

import json
import re
from build_operator_plugins import OPERATORS, ROOT, expected_files, check_files
from validate_plugin import ALLOWED_TOP_LEVEL, REQUIRED_INTERFACE, is_https_url


def validate(name: str) -> None:
    root = ROOT / "plugins" / name
    check_files(root, expected_files(name))
    data = json.loads((root / ".codex-plugin/plugin.json").read_text())
    assert set(data) <= ALLOWED_TOP_LEVEL, "unknown plugin field"
    assert data["name"] == name and re.fullmatch(r"\d+\.\d+\.\d+", data["version"])
    assert data["skills"] == "./skills/"
    assert REQUIRED_INTERFACE <= data["interface"].keys()
    assert all(is_https_url(data[k]) for k in ("homepage", "repository"))
    assert is_https_url(data["interface"]["websiteURL"])
    assert all(isinstance(p, str) and 0 < len(p) <= 128 for p in data["interface"]["defaultPrompt"])
    assert {p.parent.name for p in (root / "skills").glob("*/SKILL.md")} == {name}
    assert not any("[TODO:" in b.decode("utf-8") for b in expected_files(name).values())
    print(f"Operator plugin valid: {name}, skills-only, no live endpoint.")


if __name__ == "__main__":
    for name in OPERATORS:
        validate(name)
