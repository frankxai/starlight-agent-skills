# Releasing Starlight Agent Skills

The library separates skill frontmatter versions, repository releases, ports
into downstream runtimes, the Starlight website, and package distribution. One
never silently authorizes another.

## Current truth

- `CHANGELOG.md` is the curated library history.
- `docs/releases/release-ledger.json` is the machine-readable release state.
- `docs/releases/v0.1.0.md` is a draft historical candidate.
- No remote tag or GitHub release exists. Four local-only `asph-wip-*` and
  `archive/*` tags are recovery receipts, not releases.
- The existing attestation's `v0.1.0` wording described intended identity, not
  a published GitHub release; the append-only correction records that fact.
- Eight commits after the `v0.1.0` boundary are queued for `v0.2.0`.

## Why the first release uses a historical boundary

Commit `ff4efe5ac2bea17f080f1d85ba503277e3864a09` is the internally consistent
26-skill `v0.1.0` source boundary. Tagging the current 27-skill tree as the
original release would make its source archive disagree with its own changelog
and attestation. The first release therefore backfills that exact historical
boundary. `v0.2.0` receives a new immutable boundary only after this governance
foundation and the first release are reviewed.

## Meaningful-update rhythm

Update the changelog when a skill contract, manifest, validator, adapter,
activation rule, orchestrator, security boundary, distribution path, or public
source of truth materially changes. Batch small documentation and dependency
chores into the next meaningful entry. A weekly audit finds missing receipts;
it does not manufacture releases.

Each release candidate must name its exact Git boundary, complete commit and PR
receipts, validation results, attestation state, public-surface state, and human
approvals. Skill-level frontmatter remains independently versioned.

## GitHub release path

1. Update the changelog, notes, audit, ledger, and attestation correction.
2. Run `make release-check` plus the normal skill validators.
3. Merge the governance change through a reviewed draft-first pull request.
4. In a follow-up review, mark validation complete and set the attestation,
   public-surface acknowledgement, and release approvals to `true`.
5. Configure required reviewers on the `github-release-draft` environment.
6. Manually run **Draft GitHub release** from `main` with the exact version and
   target SHA from the ledger.
7. Review the generated GitHub draft. Publishing remains a human action.

The workflow rejects automatic triggers, a non-main dispatch, a mismatched or
non-ancestor target, incomplete approvals, or a conflicting tag. Safe retries
may reuse an exact annotated tag or existing draft. It never publishes.

## Public Starlight changelog

The shared site changelog is live at `https://starlightintelligence.org/changelog`
but did not mention this repository or `v0.1.0` at the audit boundary. The SIP
page also declares `/protocol/changelog`, which returned 404. Fixing those
surfaces belongs to the mandatory multi-role Starlight website lane; this repo
records the gap and routes a public receipt through the central domain-command
rollout without bypassing that gate.
