#!/usr/bin/env python3
"""Regression tests for the zero-dependency Agent Skills validator."""

from __future__ import annotations

import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path


VALIDATOR_PATH = Path(__file__).with_name("validate_skills.py")
SPEC = importlib.util.spec_from_file_location("validate_skills", VALIDATOR_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"could not load {VALIDATOR_PATH}")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class SkillValidatorTests(unittest.TestCase):
    def validate(self, folder: str, frontmatter: str, filename: str = "SKILL.md") -> tuple[int, str]:
        """Run the validator against one isolated skill fixture."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "skills"
            skill_dir = root / "coding" / folder
            skill_dir.mkdir(parents=True)
            (skill_dir / filename).write_text(
                f"---\n{frontmatter}\n---\n\n# Fixture\n\nBuilt on SIP\n",
                encoding="utf-8",
            )
            original_root = VALIDATOR.ROOT
            VALIDATOR.ROOT = str(root)
            output = io.StringIO()
            try:
                with contextlib.redirect_stdout(output):
                    result = VALIDATOR.main()
            finally:
                VALIDATOR.ROOT = original_root
            return result, output.getvalue()

    def test_accepts_standard_compatibility_and_string_metadata(self) -> None:
        """Accept official compatibility and string metadata fields."""
        result, output = self.validate(
            "valid-skill",
            "\n".join(
                [
                    "name: valid-skill",
                    "description: A valid fixture. Use when testing the validator.",
                    "compatibility: Requires Python 3.11 or newer.",
                    'metadata: {"version": "0.1.0", "domain": "coding", "tags": "qa,fixture"}',
                ]
            ),
        )
        self.assertEqual(result, 0, output)

    def test_rejects_array_metadata_values(self) -> None:
        """Reject non-string metadata values from portable frontmatter."""
        result, output = self.validate(
            "array-tags",
            "\n".join(
                [
                    "name: array-tags",
                    "description: An invalid fixture. Use when testing metadata values.",
                    'metadata: {"version": "0.1.0", "domain": "coding", "tags": ["qa"]}',
                ]
            ),
        )
        self.assertEqual(result, 1)
        self.assertIn("metadata keys and values must be strings", output)

    def test_rejects_consecutive_hyphens(self) -> None:
        """Reject names with consecutive hyphens."""
        result, output = self.validate(
            "bad--name",
            "\n".join(
                [
                    "name: bad--name",
                    "description: An invalid fixture. Use when testing names.",
                    'metadata: {"version": "0.1.0", "domain": "coding"}',
                ]
            ),
        )
        self.assertEqual(result, 1)
        self.assertIn("must be lowercase kebab-case", output)

    def test_rejects_overlong_compatibility(self) -> None:
        """Reject compatibility text beyond the official length limit."""
        result, output = self.validate(
            "long-compatibility",
            "\n".join(
                [
                    "name: long-compatibility",
                    "description: An invalid fixture. Use when testing compatibility.",
                    f"compatibility: {'x' * 501}",
                    'metadata: {"version": "0.1.0", "domain": "coding"}',
                ]
            ),
        )
        self.assertEqual(result, 1)
        self.assertIn("must be 1-500 characters", output)

    def test_rejects_custom_top_level_keys(self) -> None:
        """Reject non-standard top-level frontmatter keys."""
        result, output = self.validate(
            "custom-key",
            "\n".join(
                [
                    "name: custom-key",
                    "description: An invalid fixture. Use when testing top-level keys.",
                    "version: 0.1.0",
                    'metadata: {"version": "0.1.0", "domain": "coding"}',
                ]
            ),
        )
        self.assertEqual(result, 1)
        self.assertIn("unsupported top-level frontmatter keys", output)


    def test_rejects_mis_cased_skill_filename(self) -> None:
        """Reject skill files that disappear on case-sensitive hosts."""
        result, output = self.validate(
            "mis-cased-file",
            "\n".join(
                [
                    "name: mis-cased-file",
                    "description: An invalid fixture. Use when testing filename casing.",
                    'metadata: {"version": "0.1.0", "domain": "coding"}',
                ]
            ),
            filename="Skill.md",
        )
        self.assertEqual(result, 1)
        self.assertIn("skill file must be named exactly 'SKILL.md'", output)


if __name__ == "__main__":
    unittest.main()
