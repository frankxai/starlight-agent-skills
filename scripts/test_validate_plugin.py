#!/usr/bin/env python3
"""Unit tests for the pure logic of the plugin validator."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

VALIDATOR_PATH = Path(__file__).with_name("validate_plugin.py")
SPEC = importlib.util.spec_from_file_location("validate_plugin", VALIDATOR_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"could not load {VALIDATOR_PATH}")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)

class TestValidatePlugin(unittest.TestCase):
    def test_is_https_url_valid(self):
        self.assertTrue(VALIDATOR.is_https_url("https://example.com"))
        self.assertTrue(VALIDATOR.is_https_url("https://github.com/path"))

    def test_is_https_url_invalid_scheme(self):
        self.assertFalse(VALIDATOR.is_https_url("http://example.com"))
        self.assertFalse(VALIDATOR.is_https_url("ftp://example.com"))
        self.assertFalse(VALIDATOR.is_https_url("example.com"))

    def test_is_https_url_missing_netloc(self):
        self.assertFalse(VALIDATOR.is_https_url("https:///path"))
        self.assertFalse(VALIDATOR.is_https_url("https://"))

    def test_is_https_url_not_string(self):
        self.assertFalse(VALIDATOR.is_https_url(None))
        self.assertFalse(VALIDATOR.is_https_url(123))
        self.assertFalse(VALIDATOR.is_https_url(["https://example.com"]))

if __name__ == "__main__":
    unittest.main()
