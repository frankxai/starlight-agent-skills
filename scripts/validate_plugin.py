#!/usr/bin/env python3
"""Validate the distributable Starlight Product Studios Codex plugin."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugins" / "starlight-product-studios"
MANIFEST = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
REQUIRED_SKILLS = {
    "publishing-studio",
    "template-studio",
    "software-studio",
    "media-studio",
    "world-experience-studio",
    "product-studio-director",
}
ALLOWED_TOP_LEVEL = {
    "name",
    "version",
    "description",
    "author",
    "homepage",
    "repository",
    "license",
    "keywords",
    "skills",
    "interface",
}
REQUIRED_INTERFACE = {
    "displayName",
    "shortDescription",
    "longDescription",
    "developerName",
    "category",
    "capabilities",
    "websiteURL",
    "defaultPrompt",
    "brandColor",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def is_https_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def main() -> None:
    if PLUGIN_ROOT.name != "starlight-product-studios":
        fail("plugin folder name is not canonical")
    if not MANIFEST.is_file():
        fail("missing plugin .codex-plugin/plugin.json")

    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot parse plugin manifest: {exc}")

    if not isinstance(data, dict):
        fail("plugin manifest must be a JSON object")
    unknown = sorted(set(data) - ALLOWED_TOP_LEVEL)
    if unknown:
        fail(f"unsupported top-level field(s): {', '.join(unknown)}")
    if data.get("name") != PLUGIN_ROOT.name:
        fail("plugin name must match its outer folder")
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?", str(data.get("version", ""))):
        fail("version must use strict semantic versioning")
    if not isinstance(data.get("description"), str) or not data["description"].strip():
        fail("description is required")

    author = data.get("author")
    if not isinstance(author, dict) or not isinstance(author.get("name"), str) or not author["name"].strip():
        fail("author.name is required")
    for key in ("homepage", "repository"):
        if not is_https_url(data.get(key)):
            fail(f"{key} must be an absolute HTTPS URL")

    if data.get("skills") != "./skills/":
        fail("skills must resolve to the compiled ./skills/ projection")
    interface = data.get("interface")
    if not isinstance(interface, dict):
        fail("interface object is required")
    missing = sorted(REQUIRED_INTERFACE - set(interface))
    if missing:
        fail(f"missing interface field(s): {', '.join(missing)}")
    if not is_https_url(interface.get("websiteURL")):
        fail("interface.websiteURL must be an absolute HTTPS URL")
    prompts = interface.get("defaultPrompt")
    if not isinstance(prompts, list) or not 1 <= len(prompts) <= 3:
        fail("interface.defaultPrompt must contain one to three prompts")
    if any(not isinstance(prompt, str) or not prompt.strip() or len(prompt) > 128 for prompt in prompts):
        fail("default prompts must be non-empty strings of at most 128 characters")
    if not re.fullmatch(r"#[0-9A-Fa-f]{6}", str(interface.get("brandColor", ""))):
        fail("interface.brandColor must be a six-digit hex color")

    found = {
        path.parent.name
        for path in (PLUGIN_ROOT / "skills").glob("*/SKILL.md")
        if path.is_file()
    }
    if found != REQUIRED_SKILLS:
        fail(f"plugin skill set drift: expected {sorted(REQUIRED_SKILLS)}, found {sorted(found)}")

    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_product_studios_plugin.py"), "--check"],
        cwd=ROOT,
        check=True,
    )
    serialized = MANIFEST.read_text(encoding="utf-8")
    if "[TODO:" in serialized:
        fail("plugin manifest contains unfinished scaffold placeholders")

    print(
        "Plugin contract valid "
        f"({data['name']} {data['version']}, {len(found)} packaged skills, skills-only)."
    )


if __name__ == "__main__":
    main()
