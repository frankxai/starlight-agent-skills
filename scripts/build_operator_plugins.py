#!/usr/bin/env python3
"""Compile two skills-only plugins from the canonical operator capabilities."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import shutil
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OPERATORS = {
    "starlight": ("Starlight", "Execute bounded work with verified evidence.",
                  "Implement the next tested, reviewable Starlight change."),
    "starlight-queen": ("Starlight Queen", "Coordinate agent work, decisions and evidence.",
                        "Review agent work and prepare the next bounded assignment."),
}


def validate_personal_metadata(raw: bytes) -> dict:
    """Accept the host's narrow YAML format, not arbitrary YAML capabilities."""
    if len(raw) > 16384:
        raise ValueError("oversized personal metadata")
    text = raw.decode("utf-8")
    section = field = None
    seen = set()
    values = {}
    products = []
    for line in text.splitlines():
        if not line.strip():
            continue
        if line in ("interface:", "policy:"):
            section = line[:-1]
            if section in seen:
                raise ValueError("duplicate personal metadata section")
            seen.add(section); field = None
            continue
        if section == "policy" and field == "products" and re.fullmatch(r" {2,4}- [a-z]+", line):
            products.append(line.strip()[2:]); continue
        match = re.fullmatch(r"  ([a-z_]+):(?: (.+))?", line)
        if match and section:
            field, value = match.groups()
            key = (section, field)
            if key in values:
                raise ValueError("duplicate personal metadata field")
            values[key] = value
            continue
        if section == "interface" and field and line.startswith("    ") and not line.startswith("     "):
            key = (section, field)
            if not values[key] or values[key].startswith(('"', "'")):
                raise ValueError("unsupported personal metadata continuation")
            values[key] += " " + line.strip(); continue
        raise ValueError("unsupported personal metadata syntax")
    interface = {k: v for (s, k), v in values.items() if s == "interface"}
    required = {"display_name", "short_description", "default_prompt"}
    if not required <= interface.keys() or not interface.keys() <= required | {"icon_small", "icon_large", "brand_color"}:
        raise ValueError("unknown or missing personal interface field")
    for key, value in interface.items():
        if value is None:
            raise ValueError("empty personal interface field")
        if value.startswith('"'):
            value = json.loads(value)
        elif (key != "brand_color" and "#" in value) or any(c in value for c in "&*!|>{}[]'\t"):
            raise ValueError("unsupported personal metadata scalar")
        if not isinstance(value, str) or not 0 < len(value) <= 2048 or any(ord(c) < 32 for c in value):
            raise ValueError("invalid personal interface value")
        if key.startswith("icon_") and value != "assets/icon.svg":
            raise ValueError("personal icon must use the bounded static asset")
        if key == "brand_color" and not re.fullmatch(r"#[0-9A-Fa-f]{6}", value):
            raise ValueError("invalid personal brand color")
    policy = {k: v for (s, k), v in values.items() if s == "policy"}
    if policy.keys() - {"products", "allow_implicit_invocation"}:
        raise ValueError("unknown personal host policy field")
    if "products" in policy and (policy["products"] is not None or not products or len(products) != len(set(products))
                                 or set(products) - {"chatgpt", "codex", "api", "atlas"}):
        raise ValueError("invalid personal host products")
    if "allow_implicit_invocation" in policy and policy["allow_implicit_invocation"] not in ("true", "false"):
        raise ValueError("invalid personal invocation policy")
    return {**({"products": products} if "products" in policy else {}),
            **({"allow_implicit_invocation": policy["allow_implicit_invocation"] == "true"}
               if "allow_implicit_invocation" in policy else {})}


def validate_static_icon(raw: bytes) -> None:
    text = raw.decode("utf-8")
    if len(raw) > 65536 or "<!" in text or "<?" in text or any(ord(c) < 32 and c not in "\n\r\t" for c in text):
        raise ValueError("oversized or declarative personal icon")
    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        raise ValueError("invalid personal icon") from exc
    namespace = "{http://www.w3.org/2000/svg}"
    tags = {"svg", "g", "path", "rect", "circle", "ellipse", "line", "polyline", "polygon", "defs",
            "linearGradient", "radialGradient", "stop", "clipPath", "mask", "title", "desc", "use"}
    attributes = {"id", "viewBox", "width", "height", "x", "y", "x1", "y1", "x2", "y2", "cx", "cy",
                  "r", "rx", "ry", "d", "points", "fill", "fill-rule", "fill-opacity", "stroke", "stroke-width",
                  "stroke-opacity", "stroke-linecap", "stroke-linejoin", "stroke-dasharray", "opacity", "transform",
                  "offset", "stop-color", "stop-opacity", "gradientUnits", "gradientTransform", "spreadMethod",
                  "clip-path", "clip-rule", "clipPathUnits", "mask", "maskUnits", "maskContentUnits", "href",
                  "preserveAspectRatio", "role", "aria-label"}
    elements = list(root.iter())
    if root.tag != namespace + "svg" or len(elements) > 1000:
        raise ValueError("invalid personal icon root or complexity")
    for node in elements:
        if node.tag not in {namespace + tag for tag in tags}:
            raise ValueError("nonstatic personal icon element")
        for key, value in node.attrib.items():
            key = key.removeprefix("{http://www.w3.org/1999/xlink}")
            if key not in attributes:
                raise ValueError("unsafe personal icon attribute")
            if key == "href" and not re.fullmatch(r"#[A-Za-z][A-Za-z0-9_-]*", value):
                raise ValueError("external personal icon reference")
            if re.search(r"url\s*\(", value, re.I) and not re.fullmatch(r"url\(#[A-Za-z][A-Za-z0-9_-]*\)", value):
                raise ValueError("external personal icon resource")


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
            if not text.startswith("---\n") or "\r" in text or "\n---\n" not in text[4:]:
                raise ValueError("personal projection requires exact LF frontmatter delimiters")
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


def check_files(root: Path, expected: dict[Path, bytes], personal_ui_overlay: bool = False) -> dict | None:
    host_policy = None
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
        # Validate presentation AND the host's invocation policy separately.
        # Dependencies, tools and endpoints cannot hide in the overlay.
        if Path("agents/openai.yaml") not in actual:
            raise ValueError("missing personal UI metadata")
        host_policy = validate_personal_metadata(actual[Path("agents/openai.yaml")])
        if Path("assets/icon.svg") in actual:
            validate_static_icon(actual[Path("assets/icon.svg")])
        expected = {p: b for p, b in expected.items() if p != Path("agents/openai.yaml")}
        actual = {p: b for p, b in actual.items() if p not in {Path("agents/openai.yaml"), Path("assets/icon.svg")}}
    failures = [("missing", p) for p in expected.keys() - actual.keys()]
    failures += [("extra", p) for p in actual.keys() - expected.keys()]
    failures += [("changed", p) for p in expected.keys() & actual.keys() if expected[p] != actual[p]]
    if failures:
        for reason, path in sorted(failures):
            print(f"ERROR: {reason}: {path}", file=sys.stderr)
        raise ValueError("projection drift")
    return host_policy


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
            host_policy = check_files(args.personal_root, skill_files(args.check_personal, personal=True), personal_ui_overlay=True)
            print(f"Personal projection current: {args.check_personal}; host presentation validated; declared invocation policy={json.dumps(host_policy, sort_keys=True)}.")
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
