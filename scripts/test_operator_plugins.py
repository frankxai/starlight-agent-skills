#!/usr/bin/env python3
"""Verify projection drift, manifest tampering and source-body parity failures."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import build_operator_plugins as builder

from build_operator_plugins import ROOT, check_files, expected_files, skill_files


class ProjectionTests(unittest.TestCase):
    def test_personal_host_presentation_overlay_does_not_hide_instruction_drift(self):
        expected = {Path("SKILL.md"): b"canonical", Path("agents/openai.yaml"): b"authored-ui"}
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); (root / "agents").mkdir(); (root / "assets").mkdir()
            (root / "SKILL.md").write_bytes(b"canonical")
            (root / "agents/openai.yaml").write_bytes(b"host-ui")
            (root / "assets/icon.svg").write_bytes(b"host-icon")
            check_files(root, expected, personal_ui_overlay=True)
            (root / "SKILL.md").write_bytes(b"changed")
            with self.assertRaises(ValueError): check_files(root, expected, personal_ui_overlay=True)

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
