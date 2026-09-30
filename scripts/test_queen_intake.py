#!/usr/bin/env python3
"""Exercise trust boundaries, failure modes, replay, and offline CLI behavior."""
from __future__ import annotations

import copy
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "skills/substrate/starlight-queen/scripts/queen_intake.py"
spec = importlib.util.spec_from_file_location("queen_intake", HELPER)
q = importlib.util.module_from_spec(spec)
spec.loader.exec_module(q)
SCOPE = {"tenant": "company-a", "project": "starlight", "repository": "frankxai/starlight-agent-skills"}


def observation() -> dict:
    return {"source": "paperclip", "id": "task-22", "scope": copy.deepcopy(SCOPE),
            "kind": "work", "declared_state": "done", "observed_at": "2026-09-30T12:00:00.000Z",
            "refs": [{"kind": "run", "id": "run-r12"}]}


def intake(rows: list | None = None) -> dict:
    return {"schema": "starlight.operator_intake.v1", "scope": copy.deepcopy(SCOPE),
            "observations": rows if rows is not None else [observation()]}


def envelope(repo: Path) -> dict:
    return {"envelope": "v1", "kind": "task", "id": "task-22", "slug": "review-task",
            "producer": "paperclip", "status": "pending", "createdAt": "2026-09-30T12:00:00.000Z",
            "agent": "claude", "priority": 100, "maxMinutes": 15, "repo": str(repo),
            "risk": "normal", "prompt": "Inspect the current PR and report exact-head failing checks."}


class EvidenceTests(unittest.TestCase):
    def test_preserves_claim_and_no_authority_upgrade(self):
        report = q.normalize_evidence(intake(), SCOPE)
        self.assertEqual(report["observations"][0]["declared_state"], "done")
        self.assertEqual(report["verification"], "not_evaluated")
        self.assertFalse(report["dispatch"])
        self.assertNotIn("outcome", report["observations"][0])
        self.assertEqual(report["schema"], "starlight.operator_review.v1")

    def test_scope_is_selected_independently(self):
        foreign = copy.deepcopy(SCOPE); foreign["tenant"] = "company-b"
        with self.assertRaises(q.IntakeError): q.normalize_evidence(intake(), foreign)
        row = observation(); row["scope"] = foreign
        with self.assertRaises(q.IntakeError): q.normalize_evidence(intake([row]), SCOPE)

    def test_identical_replay_dedup_and_conflict_rejection(self):
        self.assertEqual(len(q.normalize_evidence(intake([observation(), observation()]), SCOPE)["observations"]), 1)
        changed = observation(); changed["declared_state"] = "failed"
        with self.assertRaises(q.IntakeError): q.normalize_evidence(intake([observation(), changed]), SCOPE)

    def test_replay_is_per_batch_and_later_observations_are_independent(self):
        first = q.normalize_evidence(intake(), SCOPE)
        newer = observation(); newer['declared_state'] = 'failed'; newer['observed_at'] = '2026-09-30T12:01:00.000Z'
        second = q.normalize_evidence(intake([newer]), SCOPE)
        self.assertEqual(first['observations'][0]['declared_state'], 'done')
        self.assertEqual(second['observations'][0]['declared_state'], 'failed')
        self.assertEqual(second['verification'], 'not_evaluated')

    def test_source_ids_do_not_collide(self):
        row = observation(); row["source"] = "hermes"
        self.assertEqual(len(q.normalize_evidence(intake([row, observation()]), SCOPE)["observations"]), 2)

    def test_arbitrary_content_credentials_and_urls_are_rejected(self):
        for field in ("prompt", "logs", "token", "approval"):
            row = observation(); row[field] = "private-value"
            with self.assertRaises(q.IntakeError): q.normalize_evidence(intake([row]), SCOPE)
        row = observation(); row["refs"][0]["id"] = "https://user:secret@example.org/run"
        with self.assertRaises(q.IntakeError): q.normalize_evidence(intake([row]), SCOPE)

    def test_timestamp_and_hash_validity(self):
        for bad in ("yesterday", "2026-09-30T12:00:00Z", "2026-02-30T12:00:00.000Z", "２０２６-09-30T12:00:00.000Z"):
            row = observation(); row["observed_at"] = bad
            with self.assertRaises(q.IntakeError): q.normalize_evidence(intake([row]), SCOPE)
        row = observation(); row["refs"][0]["sha256"] = "not-a-hash"
        with self.assertRaises(q.IntakeError): q.normalize_evidence(intake([row]), SCOPE)


class PacketTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.packet = envelope(self.root)

    def tearDown(self): self.temp.cleanup()

    def test_wraps_and_does_not_mutate_or_dispatch(self):
        original = copy.deepcopy(self.packet)
        review = q.review_packet(self.packet, self.root)
        self.assertEqual(self.packet, original)
        self.assertFalse(review["dispatch"])
        self.assertEqual(review["authority"], "not_evaluated")
        self.assertEqual(review["host_path_scope"], "current_host_only")
        self.assertEqual(review["dispatch_path_validation"], "not_evaluated")
        self.assertNotIn("prompt", review)
        self.assertNotIn("envelope", review)
        self.assertEqual(list(self.root.iterdir()), [])

    def test_never_infers_missing_mapping_fields(self):
        for field in ("agent", "repo", "maxMinutes", "prompt"):
            p = copy.deepcopy(self.packet); del p[field]
            with self.assertRaises(q.IntakeError): q.review_packet(p, self.root)

    def test_chain_cards_require_their_own_admitted_consumer(self):
        self.packet["kind"] = "chain-task"
        with self.assertRaises(q.IntakeError): q.review_packet(self.packet, self.root)

    def test_repo_mapping_requires_exact_existing_checkout(self):
        sub = self.root / "other-repo"; sub.mkdir()
        self.packet["repo"] = str(sub)
        with self.assertRaises(q.IntakeError): q.review_packet(self.packet, self.root)
        self.packet["repo"] = "relative/repo"
        with self.assertRaises(q.IntakeError): q.review_packet(self.packet, self.root)

    def test_budget_and_priority_booleans_nan_and_large_integers(self):
        for value in (True, float("nan"), float("inf"), 0, 26, 10 ** 1000):
            self.packet["maxMinutes"] = value
            with self.assertRaises(q.IntakeError): q.review_packet(self.packet, self.root)
        self.packet["maxMinutes"] = 15; self.packet["priority"] = True
        with self.assertRaises(q.IntakeError): q.review_packet(self.packet, self.root)

    def test_code_requires_ref_and_check_allowlist(self):
        self.packet["needs"] = ["git-write"]
        with self.assertRaises(q.IntakeError): q.review_packet(self.packet, self.root)
        self.packet["assignedRef"] = "origin/agent/claude/review-task"
        with self.assertRaises(q.IntakeError): q.review_packet(self.packet, self.root)
        self.packet["allowedChecks"] = ["python3 scripts/test_queen_intake.py"]
        self.packet["requiredChecks"] = ["touch forbidden"]
        with self.assertRaises(q.IntakeError): q.review_packet(self.packet, self.root)
        self.packet["requiredChecks"] = self.packet["allowedChecks"][:]
        self.assertEqual(q.review_packet(self.packet, self.root)["packet"], self.packet)
        self.assertFalse((self.root / "forbidden").exists())

    def test_snapshot_paths_cannot_escape_or_snapshot_whole_repo(self):
        for value in ("..", "../secret", "/private", "C:/secret", "..\\secret", ".", "./"):
            self.packet["snapshotPaths"] = [value]
            with self.assertRaises(q.IntakeError): q.review_packet(self.packet, self.root)
        with tempfile.TemporaryDirectory() as foreign:
            (self.root / "escape").symlink_to(foreign, target_is_directory=True)
            self.packet["snapshotPaths"] = ["escape/secret"]
            with self.assertRaises(q.IntakeError): q.review_packet(self.packet, self.root)

    def test_snapshot_denylist_and_internal_symlinks(self):
        for path in ('.git/config', '.env', '.env.local', '.env.example', 'private/id_rsa', 'credentials.json'):
            self.packet['snapshotPaths'] = [path]
            with self.assertRaises(q.IntakeError): q.review_packet(self.packet, self.root)
        (self.root / 'real').mkdir(); (self.root / 'link').symlink_to('real', target_is_directory=True)
        self.packet['snapshotPaths'] = ['link/future.md']
        with self.assertRaises(q.IntakeError): q.review_packet(self.packet, self.root)
        self.packet['snapshotPaths'] = ['real/future.md']
        self.assertFalse(q.review_packet(self.packet, self.root)['dispatch'])

    def test_unsafe_refs(self):
        for value in ("origin/agent/claude/../secret", "origin/agent/claude/a.lock/b", "origin/agent/claude/a\x7fb", "origin/agent/claude/a b"):
            self.packet["assignedRef"] = value
            with self.assertRaises(q.IntakeError): q.review_packet(self.packet, self.root)

    def test_symlink_cycle_is_sanitized_at_cli(self):
        (self.root / "private-cycle").symlink_to("private-cycle")
        self.packet["snapshotPaths"] = ["private-cycle"]
        file = self.root / "packet.json"; file.write_text(json.dumps(self.packet))
        result = subprocess.run([sys.executable, str(HELPER), "packet", str(file), "--repo-root", str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertNotIn(str(self.root), result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertFalse(json.loads(result.stderr)["dispatch"])


class InputTests(unittest.TestCase):
    @unittest.skipUnless(hasattr(os, "mkfifo"), "POSIX FIFO test")
    def test_fifo_is_rejected_without_blocking(self):
        with tempfile.TemporaryDirectory() as temp:
            fifo = Path(temp) / "input.json"; os.mkfifo(fifo)
            args = [sys.executable, str(HELPER), "evidence", str(fifo)]
            for key, value in SCOPE.items(): args += ["--" + key, value]
            result = subprocess.run(args, capture_output=True, text=True, timeout=3)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(json.loads(result.stderr)["error"], "input must be a regular file")

    def test_duplicate_keys_nonfinite_and_oversize(self):
        with tempfile.TemporaryDirectory() as temp:
            file = Path(temp) / "input.json"
            for raw in ('{"schema":"a","schema":"b"}', '{"number":NaN}', 'x' * (q.MAX_BYTES + 1)):
                file.write_text(raw)
                with self.assertRaises(q.IntakeError): q.read_document(file)

    def test_cli_rejects_exponent_overflow_and_deep_nesting(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); file = root / 'input.json'
            packet = envelope(root)
            cases = [json.dumps(packet).replace('"maxMinutes": 15', '"maxMinutes": 1e999'), '[' * 2000 + '0' + ']' * 2000]
            for raw in cases:
                file.write_text(raw)
                result = subprocess.run([sys.executable, str(HELPER), 'packet', str(file), '--repo-root', str(root)], capture_output=True, text=True)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, '')
                self.assertNotIn('Traceback', result.stderr)

    def test_cli_stdout_only_and_no_queue_writes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); file = root / "input.json"; file.write_text(json.dumps(intake()))
            args = [sys.executable, str(HELPER), "evidence", str(file)]
            for key, value in SCOPE.items(): args += ["--" + key, value]
            result = subprocess.run(args, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(json.loads(result.stdout)["dispatch"])
            self.assertEqual(list(root.iterdir()), [file])


if __name__ == "__main__":
    unittest.main()
