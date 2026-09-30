#!/usr/bin/env python3
"""Verify projection drift, manifest tampering and source-body parity failures."""
from pathlib import Path
import tempfile
import unittest
import subprocess
import sys
from unittest.mock import patch

import build_operator_plugins as builder

from build_operator_plugins import ROOT, check_files, expected_files, skill_files


HOST_UI = b"interface:\n  display_name: Starlight\n  short_description: Execute bounded work\n  default_prompt: Use $starlight to prepare a\n    tested change.\n  icon_small: assets/icon.svg\npolicy:\n  products:\n  - chatgpt\n  - codex\n  allow_implicit_invocation: true\n"
STATIC_ICON = b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M0 0" fill="#fff"/></svg>'

class ProjectionTests(unittest.TestCase):
    def test_personal_host_presentation_overlay_does_not_hide_instruction_drift(self):
        expected = {Path("SKILL.md"): b"canonical", Path("agents/openai.yaml"): b"authored-ui"}
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); (root / "agents").mkdir(); (root / "assets").mkdir()
            (root / "SKILL.md").write_bytes(b"canonical")
            (root / "agents/openai.yaml").write_bytes(HOST_UI)
            (root / "assets/icon.svg").write_bytes(STATIC_ICON)
            check_files(root, expected, personal_ui_overlay=True)
            (root / "SKILL.md").write_bytes(b"changed")
            with self.assertRaises(ValueError): check_files(root, expected, personal_ui_overlay=True)

    def test_overlay_cannot_hide_capabilities_or_ambiguous_yaml(self):
        for addition in (b'\ndependencies:\n  tools: endpoint\n', b'  endpoints: https://evil.invalid\n',
                         b'  allow_implicit_invocation: maybe\n', b'  products: [unknown]\n',
                         b'interface:\n  display_name: replaced\n'):
            with self.subTest(addition=addition):
                with self.assertRaises(ValueError): builder.validate_personal_metadata(HOST_UI + addition)
        with self.assertRaises(ValueError):
            builder.validate_personal_metadata(HOST_UI.replace(b'Execute bounded work', b'&alias capability'))

    def test_icon_rejects_active_content_and_external_resources(self):
        for body in (b'<script>alert(1)</script>', b'<foreignObject/>', b'<image href="https://evil.invalid"/>',
                     b'<path onload="alert(1)"/>', b'<use href="https://evil.invalid/icon.svg"/>',
                     b'<path fill="url(https://evil.invalid)"/>', b'<path style="fill:red"/>'):
            with self.subTest(body=body):
                with self.assertRaises(ValueError):
                    builder.validate_static_icon(b'<svg xmlns="http://www.w3.org/2000/svg">' + body + b'</svg>')
        for raw in (b'<!DOCTYPE svg>' + STATIC_ICON, b'<?xml-stylesheet href="https://evil.invalid"?>' + STATIC_ICON):
            with self.assertRaises(ValueError): builder.validate_static_icon(raw)

    def test_manifest_gates_remain_enabled_in_optimized_python(self):
        result = subprocess.run([sys.executable, '-O', '-c',
            'from validate_operator_plugins import require; require(False, "contract rejected")'],
            cwd=ROOT / 'scripts', capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('contract rejected', result.stderr)

    def test_personal_frontmatter_rejects_unsupported_delimiters_explicitly(self):
        for content in ('\ufeff---\nname: starlight\n---\nbody', '---\r\nname: starlight\r\n---\r\nbody'):
            with tempfile.TemporaryDirectory() as temp:
                root = Path(temp); source = root / 'skills/substrate/starlight'; source.mkdir(parents=True)
                (source / 'SKILL.md').write_bytes(content.encode())
                with patch.object(builder, 'ROOT', root):
                    with self.assertRaisesRegex(ValueError, 'exact LF frontmatter'):
                        builder.skill_files('starlight', personal=True)

    def test_compiler_refuses_symlinked_parent_without_deleting_outside_files(self):
        with tempfile.TemporaryDirectory() as repo, tempfile.TemporaryDirectory() as foreign:
            root = Path(repo); outside = Path(foreign)
            (root / "plugins").symlink_to(outside, target_is_directory=True)
            (outside / "starlight").mkdir()
            sentinel = outside / "starlight/unrelated.txt"; sentinel.write_text("preserve")
            with patch.object(builder, "ROOT", root):
                with self.assertRaises(ValueError): builder.compile_plugin("starlight")
            self.assertEqual(sentinel.read_text(), "preserve")

    def test_compiler_refuses_symlinked_canonical_source_ancestor(self):
        with tempfile.TemporaryDirectory() as repo, tempfile.TemporaryDirectory() as foreign:
            root = Path(repo); (root / "skills").symlink_to(foreign, target_is_directory=True)
            with patch.object(builder, "ROOT", root):
                with self.assertRaises(ValueError): builder.skill_files("starlight")

    def test_private_files_cannot_enter_via_symlinked_reference_folder(self):
        with tempfile.TemporaryDirectory() as repo, tempfile.TemporaryDirectory() as foreign:
            root = Path(repo); source = root / "skills/substrate/starlight"
            source.mkdir(parents=True); (source / "SKILL.md").write_text("canonical")
            outside = Path(foreign); (outside / "private.txt").write_text("private")
            (source / "references").symlink_to(outside, target_is_directory=True)
            with patch.object(builder, "ROOT", root):
                with self.assertRaises(ValueError): builder.skill_files("starlight")

    def test_generated_manifests_and_skills_have_one_authoring_owner(self):
        for name in ("starlight", "starlight-queen"):
            files = expected_files(name)
            with tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                for path, data in files.items():
                    (root / path).parent.mkdir(parents=True, exist_ok=True)
                    (root / path).write_bytes(data)
                check_files(root, files)
                path = root / ".codex-plugin/plugin.json"
                path.write_bytes(path.read_bytes() + b" ")
                with self.assertRaises(ValueError): check_files(root, files)

    def test_undeclared_endpoint_cannot_enter_projection(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); (root / ".mcp.json").write_text('{"url":"https://invented.invalid"}')
            with self.assertRaises(ValueError): check_files(root, {})

    def test_projection_symlinks_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); (root / "link").symlink_to("missing")
            with self.assertRaises(ValueError): check_files(root, {})

    def test_personal_projection_changes_frontmatter_only(self):
        for name in ("starlight", "starlight-queen"):
            canonical = skill_files(name)
            personal = skill_files(name, personal=True)
            source = canonical[Path("SKILL.md")].decode()
            projected = personal[Path("SKILL.md")].decode()
            self.assertEqual(source.split("\n---\n", 1)[1], projected.split("\n---\n", 1)[1])
            self.assertNotIn("\nmetadata:", projected.split("\n---\n", 1)[0])
            self.assertEqual({p: b for p, b in canonical.items() if p.name != "SKILL.md"},
                             {p: b for p, b in personal.items() if p.name != "SKILL.md"})


if __name__ == "__main__":
    unittest.main()
