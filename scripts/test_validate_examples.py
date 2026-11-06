#!/usr/bin/env python3
"""Unit tests for the pure logic of the examples validator."""

from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path

VALIDATOR_PATH = Path(__file__).with_name("validate_examples.py")
SPEC = importlib.util.spec_from_file_location("validate_examples", VALIDATOR_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"could not load {VALIDATOR_PATH}")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class TestValidateExamples(unittest.TestCase):
    def test_extract_output_json_success(self):
        text = "Some intro text.\n```json\n{\"foo\": \"bar\"}\n```\nSome outro."
        data, err = VALIDATOR.extract_output_json(text)
        self.assertIsNone(err)
        self.assertEqual(data, {"foo": "bar"})

    def test_extract_output_json_last_block(self):
        text = "```json\n{\"first\": 1}\n```\n```json\n{\"last\": 2}\n```"
        data, err = VALIDATOR.extract_output_json(text)
        self.assertIsNone(err)
        self.assertEqual(data, {"last": 2})

    def test_extract_output_json_missing(self):
        text = "No fenced json block here."
        data, err = VALIDATOR.extract_output_json(text)
        self.assertIsNone(data)
        self.assertIn("no fenced ```json code block found", err)

    def test_extract_output_json_invalid(self):
        text = "```json\n{unquoted keys}\n```"
        data, err = VALIDATOR.extract_output_json(text)
        self.assertIsNone(data)
        self.assertIn("not valid JSON", err)

    def test_jsx_tag_balance_balanced(self):
        mdx = "<Row><Fact>1</Fact><Fact>2</Fact></Row>"
        counts = VALIDATOR._jsx_tag_balance(mdx)
        self.assertEqual(counts, [("Fact", 2, 2), ("Row", 1, 1)])

    def test_jsx_tag_balance_unbalanced(self):
        mdx = "<Card><Title>Title</Title>"
        counts = VALIDATOR._jsx_tag_balance(mdx)
        self.assertEqual(counts, [("Card", 1, 0), ("Title", 1, 1)])

    def test_jsx_tag_balance_self_closing(self):
        mdx = "<Hero /><List><Item /></List>"
        counts = VALIDATOR._jsx_tag_balance(mdx)
        self.assertEqual(counts, [("List", 1, 1)])

    def test_jsx_tag_balance_ignores_lowercase(self):
        mdx = "<div><Box></Box></div>"
        counts = VALIDATOR._jsx_tag_balance(mdx)
        self.assertEqual(counts, [("Box", 1, 1)])

    def test_check_outputs_match_manifest_success(self):
        data = {"title": "Hello", "score": 9.5, "tags": ["a"]}
        outputs = [
            {"name": "title", "type": "string"},
            {"name": "score", "type": "number"},
            {"name": "tags", "type": "array"}
        ]
        errors = []
        VALIDATOR.check_outputs_match_manifest(data, outputs, "test/path", errors)
        self.assertEqual(errors, [])

    def test_check_outputs_match_manifest_missing_key(self):
        data = {"title": "Hello"}
        outputs = [
            {"name": "title", "type": "string"},
            {"name": "score", "type": "number"}
        ]
        errors = []
        VALIDATOR.check_outputs_match_manifest(data, outputs, "test/path", errors)
        self.assertEqual(len(errors), 1)
        self.assertIn("score' is missing from the example's JSON", errors[0])

    def test_check_outputs_match_manifest_type_mismatch(self):
        data = {"score": "high"}
        outputs = [{"name": "score", "type": "number"}]
        errors = []
        VALIDATOR.check_outputs_match_manifest(data, outputs, "test/path", errors)
        self.assertEqual(len(errors), 1)
        self.assertIn("expected 'number'", errors[0])

    def test_check_outputs_match_manifest_nullable_valid(self):
        data = {"note": None}
        outputs = [{"name": "note", "type": "string", "nullable": True}]
        errors = []
        VALIDATOR.check_outputs_match_manifest(data, outputs, "test/path", errors)
        self.assertEqual(errors, [])

    def test_check_outputs_match_manifest_nullable_invalid(self):
        data = {"note": None}
        outputs = [{"name": "note", "type": "string", "nullable": False}]
        errors = []
        VALIDATOR.check_outputs_match_manifest(data, outputs, "test/path", errors)
        self.assertEqual(len(errors), 1)
        self.assertIn("not mark it nullable", errors[0])

    def test_check_outputs_match_manifest_not_object(self):
        data = ["an array instead of object"]
        outputs = [{"name": "key", "type": "string"}]
        errors = []
        VALIDATOR.check_outputs_match_manifest(data, outputs, "test/path", errors)
        self.assertEqual(len(errors), 1)
        self.assertIn("expected a JSON object", errors[0])


REPO_ROOT = Path(__file__).resolve().parents[1]
COMMUNITY_STUDIO = REPO_ROOT / "skills" / "studios" / "community-studio"


class TestCommunityStudioExample(unittest.TestCase):
    """The studio declares typed outputs, so its worked example must exist and be checked."""

    def load_output(self):
        text = (COMMUNITY_STUDIO / "examples" / "example-01.md").read_text(encoding="utf-8")
        data, err = VALIDATOR.extract_output_json(text)
        self.assertIsNone(err)
        return data

    def contract_errors(self, data):
        errors = []
        VALIDATOR.CONTRACT_CHECKS["studios/community-studio"](data, "community-studio", errors)
        return errors

    def test_example_exists_and_passes_the_gate(self):
        self.assertTrue((COMMUNITY_STUDIO / "examples" / "example-01.md").is_file())
        errors = []
        ok = VALIDATOR.validate_skill(str(COMMUNITY_STUDIO), "studios", "community-studio", errors)
        self.assertTrue(ok, errors)
        self.assertEqual(errors, [])

    def test_example_is_projected_into_the_plugin(self):
        projected = REPO_ROOT / "plugins" / "starlight-product-studios" / "skills" / "community-studio" / "examples" / "example-01.md"
        self.assertEqual(projected.read_bytes(), (COMMUNITY_STUDIO / "examples" / "example-01.md").read_bytes())

    def test_contract_check_accepts_the_example(self):
        self.assertEqual(self.contract_errors(self.load_output()), [])

    def test_contract_check_rejects_missing_mobile_walkthrough(self):
        data = self.load_output()
        data["walkthrough_evidence"]["viewports"] = [1280]
        self.assertTrue(any("390" in e for e in self.contract_errors(data)))

    def test_contract_check_rejects_unfinished_path(self):
        data = self.load_output()
        data["walkthrough_evidence"]["steps_reached"] = ["invite", "onboarding", "first lesson"]
        self.assertTrue(any("first receipt" in e for e in self.contract_errors(data)))

    def test_contract_check_rejects_lesson_with_mismatched_projection(self):
        data = self.load_output()
        data["contract_valid_curriculum"][0]["projections"]["mcpTool"] = "lesson_something_else"
        self.assertTrue(any("mcpTool" in e for e in self.contract_errors(data)))

    def test_contract_check_rejects_agent_with_tools(self):
        data = self.load_output()
        name = next(iter(data["staged_agents"]))
        data["staged_agents"][name]["tools"] = ["circle_mcp"]
        self.assertTrue(any("tools" in e for e in self.contract_errors(data)))

    def test_contract_check_rejects_failing_fixtures(self):
        data = self.load_output()
        name = next(iter(data["staged_agents"]))
        data["staged_agents"][name]["fixtures_passed"] -= 1
        self.assertTrue(any("fixtures" in e for e in self.contract_errors(data)))

    def test_contract_check_rejects_release_decided_by_the_studio(self):
        data = self.load_output()
        data["release_decision"] = "Published to all members."
        self.assertTrue(any("operator" in e for e in self.contract_errors(data)))


if __name__ == "__main__":
    unittest.main()
