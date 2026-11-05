#!/usr/bin/env python3
"""Unit tests for the pure logic of the catalog generator."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

VALIDATOR_PATH = Path(__file__).with_name("generate_catalog.py")
SPEC = importlib.util.spec_from_file_location("generate_catalog", VALIDATOR_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"could not load {VALIDATOR_PATH}")
GENERATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GENERATOR)

class TestGenerateCatalog(unittest.TestCase):
    def test_parse_frontmatter_valid(self):
        content = """---
name: "test-skill"
description: "A test skill"
metadata: {"version":"1.0.0","domain":"cosmos"}
---
# Content
"""
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False) as f:
            f.write(content)
            temp_path = f.name

        try:
            fm = GENERATOR.parse_frontmatter(temp_path)
            self.assertEqual(fm.get("name"), "test-skill")
            self.assertEqual(fm.get("description"), "A test skill")
            self.assertEqual(fm.get("metadata"), {"version": "1.0.0", "domain": "cosmos"})
        finally:
            Path(temp_path).unlink()

    def test_parse_frontmatter_empty(self):
        content = """---
---
# Content
"""
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False) as f:
            f.write(content)
            temp_path = f.name

        try:
            fm = GENERATOR.parse_frontmatter(temp_path)
            self.assertEqual(fm, {})
        finally:
            Path(temp_path).unlink()

    def test_parse_frontmatter_invalid_json(self):
        content = """---
name: test
metadata: {"invalid JSON
---
# Content
"""
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False) as f:
            f.write(content)
            temp_path = f.name

        try:
            fm = GENERATOR.parse_frontmatter(temp_path)
            self.assertEqual(fm.get("name"), "test")
            self.assertEqual(fm.get("metadata"), {})
        finally:
            Path(temp_path).unlink()

    def test_parse_frontmatter_no_quotes(self):
        content = """---
name: test-skill
---
"""
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False) as f:
            f.write(content)
            temp_path = f.name

        try:
            fm = GENERATOR.parse_frontmatter(temp_path)
            self.assertEqual(fm.get("name"), "test-skill")
        finally:
            Path(temp_path).unlink()

if __name__ == "__main__":
    unittest.main()
