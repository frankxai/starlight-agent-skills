#!/usr/bin/env python3
"""Validate release truth without third-party dependencies."""

from __future__ import annotations

import json
import os
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    raise SystemExit(f"release contract: {message}")


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def git(*args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=check,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


ledger = json.loads(read("docs/releases/release-ledger.json"))
changelog = read("CHANGELOG.md")
attestation = read("ATTESTATION.md")
notes = read(ledger["release"]["notesPath"])
audit = read("docs/releases/2026-08-10-release-foundation.md")
draft_workflow = read(".github/workflows/draft-github-release.yml")
makefile = read("Makefile")

if ledger.get("schemaVersion") != 1:
    fail("schemaVersion must be 1")
if ledger.get("repository") != "frankxai/starlight-agent-skills":
    fail("repository identity is incorrect")
if ledger.get("defaultBranch") != "main":
    fail("defaultBranch must be main")

release = ledger["release"]
source = ledger["source"]
next_release = ledger["nextRelease"]
semver = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?$")
if not semver.fullmatch(release["version"]):
    fail("release.version must be SemVer")
if release["tag"] != f"v{release['version']}":
    fail("release tag must match version")
if release["status"] not in {"draft", "ready", "published"}:
    fail("release status must be draft, ready, or published")
if release["published"] != (release["status"] == "published"):
    fail("published flag must agree with release status")
if next_release["version"] != "0.2.0" or next_release["targetSha"] is not None:
    fail("v0.2.0 must remain queued without an invented target")
if next_release["status"] != "awaiting-v0.1.0-and-post-governance-boundary":
    fail("v0.2.0 queue state is incorrect")

full_sha = re.compile(r"^[0-9a-f]{40}$")
for field, value in {
    "source.auditedHead": source["auditedHead"],
    "release.targetSha": release["targetSha"],
    "nextRelease.auditedFromExclusive": next_release["auditedFromExclusive"],
    "nextRelease.auditedThroughInclusive": next_release["auditedThroughInclusive"],
}.items():
    if not full_sha.fullmatch(value):
        fail(f"{field} must be a full SHA")

if next_release["auditedFromExclusive"] != release["targetSha"]:
    fail("v0.2.0 audit must begin after the v0.1.0 boundary")
if next_release["auditedThroughInclusive"] != source["auditedHead"]:
    fail("v0.2.0 audit must end at the audited head")
if source["semanticTags"] != [] or source["remoteTags"] != [] or source["githubReleaseCount"] != 0:
    fail("the audit must preserve the absence of semantic releases")
if len(source["localNonReleaseTags"]) != 4:
    fail("exactly four local-only recovery/archive tags are expected")
actual_tags = set(git("tag", "--list").splitlines())
local_receipts = set(source["localNonReleaseTags"])
if actual_tags not in (set(), local_receipts):
    fail("checkout tags must be either the empty remote topology or all four local receipts")

try:
    git("cat-file", "-e", f"{release['targetSha']}^{{commit}}")
    git("cat-file", "-e", f"{source['auditedHead']}^{{commit}}")
    git("merge-base", "--is-ancestor", release["targetSha"], source["auditedHead"])
    git("merge-base", "--is-ancestor", source["auditedHead"], "HEAD")
except subprocess.CalledProcessError:
    fail("release and audit boundaries must exist in ordered HEAD history")

if int(git("rev-list", "--count", source["auditedHead"])) != source["commitCount"]:
    fail("audited commit count does not match Git history")
if int(git("rev-list", "--count", release["targetSha"])) != release["targetCommitCount"]:
    fail("v0.1.0 target commit count does not match Git history")
range_spec = f"{release['targetSha']}..{source['auditedHead']}"
if int(git("rev-list", "--count", range_spec)) != next_release["auditedCommitCount"]:
    fail("v0.2.0 queued commit count does not match Git history")

boundary = ledger["receipts"]["releaseBoundary"]
boundary_receipts: set[str] = set()
for receipt in boundary["pullRequests"]:
    number = receipt["number"]
    if receipt["url"] != f"https://github.com/frankxai/starlight-agent-skills/pull/{number}":
        fail(f"pull request #{number} has an incorrect URL")
    boundary_receipts.add(receipt["mergeCommit"])
    boundary_receipts.update(receipt["includedCommits"])
boundary_receipts.update(item["commit"] for item in boundary["directCommits"])
actual_boundary = set(git("rev-list", release["targetSha"]).splitlines())
if boundary_receipts != actual_boundary:
    fail("v0.1.0 receipts must cover the exact historical boundary")

unreleased = ledger["receipts"]["unreleasedAfterBoundary"]["pullRequests"]
unreleased_receipts = {item["mergeCommit"] for item in unreleased}
for receipt in unreleased:
    number = receipt["number"]
    if receipt["url"] != f"https://github.com/frankxai/starlight-agent-skills/pull/{number}":
        fail(f"unreleased pull request #{number} has an incorrect URL")
actual_unreleased = set(git("rev-list", range_spec).splitlines())
if unreleased_receipts != actual_unreleased:
    fail("v0.2.0 queue receipts must cover the exact audited delta")

if release["targetSha"] not in changelog or source["auditedHead"] not in attestation:
    fail("changelog and attestation must name their immutable boundaries")
for document in (notes, audit):
    if release["targetSha"] not in document or source["auditedHead"] not in document:
        fail("release documents must name both historical and audited boundaries")
if "Release-status correction — 2026-08-10" not in attestation:
    fail("append-only attestation correction is missing")
if "did not have\na corresponding semantic tag or GitHub release" not in attestation:
    fail("attestation correction must preserve unpublished status")

public = ledger["publicSurface"]
if public["homepage"]["status"] != "ok-200":
    fail("protocol homepage status must remain explicit")
if public["siteChangelog"]["status"] != "ok-200":
    fail("site changelog status must remain explicit")
if public["siteChangelog"]["mentionsRepository"] or public["siteChangelog"]["mentionsVersion"]:
    fail("site changelog omission must remain explicit until the site lane updates it")
if public["protocolDeclaredChangelog"]["status"] != "missing-404":
    fail("declared protocol changelog gap must remain explicit")
if public["siteChangeGate"] != "mandatory-multi-role-starlight-lane":
    fail("website changes must remain in the mandatory Starlight lane")

if "workflow_dispatch:" not in draft_workflow:
    fail("release workflow must be manual-only")
if re.search(r"^  (push|pull_request|release|schedule):", draft_workflow, re.MULTILINE):
    fail("release workflow may not have an automatic trigger")
if "environment: github-release-draft" not in draft_workflow:
    fail("release workflow must use its protected environment")
if "--draft" not in draft_workflow:
    fail("release workflow may create only a draft")
if "gh release edit" in draft_workflow or "--latest" in draft_workflow:
    fail("release workflow may not publish or promote a release")
if "release-check:" not in makefile or "python3 scripts/validate_release.py" not in makefile:
    fail("Makefile must expose the release contract")
if ledger["packagePublishing"]["status"] != "not-applicable":
    fail("package publication must remain out of scope")

existing_tag = git("rev-parse", "--verify", f"refs/tags/{release['tag']}^{{commit}}", check=False)
if existing_tag and existing_tag != release["targetSha"]:
    fail("existing release tag points to a different boundary")

mode = os.environ.get("RELEASE_MODE", "validate")
if mode == "github-release-draft":
    approvals = ledger["approvals"]
    if release["status"] != "ready":
        fail("GitHub release requires release.status=ready")
    if not approvals["validationComplete"]:
        fail("GitHub release requires completed validation")
    if not approvals["humanAttestationApproval"]:
        fail("GitHub release requires attestation approval")
    if not approvals["humanPublicSurfaceAcknowledgement"]:
        fail("GitHub release requires public-surface acknowledgement")
    if not approvals["humanReleaseApproval"]:
        fail("GitHub release requires human release approval")
    if os.environ.get("RELEASE_VERSION") != release["version"]:
        fail("workflow version must match the ledger")
    if os.environ.get("RELEASE_TARGET_SHA") != release["targetSha"]:
        fail("workflow target must match the ledger")

print(
    f"release contract ok: {release['tag']} {release['status']} at {release['targetSha']}; "
    f"v{next_release['version']} queue={next_release['auditedCommitCount']} commits"
)
