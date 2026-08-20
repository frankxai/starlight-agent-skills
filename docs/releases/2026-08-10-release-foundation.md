# Starlight Agent Skills release-foundation audit — 2026-08-10

## Outcome

The repository described `v0.1.0` in its changelog and append-only attestation,
but GitHub had no semantic tag or release. The safe repair preserves the
historical attestation, appends a status correction, and prepares a guarded
draft release at the exact 26-skill boundary
`ff4efe5ac2bea17f080f1d85ba503277e3864a09`.

## History reconciled

- Audited head: `89db74a185fb75d7c51968649bd3f1242c3d8180`
- Total audited commits: 18
- Historical `v0.1.0` boundary: 10 commits, through 2026-06-22
- Audited unreleased delta: 8 commits, through 2026-08-06
- Merged PR receipts: 14
- Semantic tags: 0
- GitHub releases: 0
- Remote tags: 0
- Local-only recovery/archive tags: 4, all explicitly non-release

The eight post-boundary commits cover catalog corrections, executable example
validation, action upgrades, the 27th skill, the public hero, and the verified
music/sound index. They remain the `v0.2.0` queue until the first release and
this governance foundation are reviewed.

## Public surface truth

- `https://starlightintelligence.org/protocol`: 200, SIP v1.1.1.
- `https://starlightintelligence.org/changelog`: 200, but no mention of this
  repository, Agent Skills, or `v0.1.0` at the audit boundary.
- The protocol page declares `https://starlightintelligence.org/protocol/changelog`
  as canonical; that route returned 404.

Website repair is not performed here because Starlight public surfaces require
their mandatory multi-role lane. The gap is recorded for the central rollout.

## Controls added

- Two-stage release ledger with exact commit and PR coverage.
- Append-only attestation correction rather than historical rewriting.
- Dependency-free release validator and cheap release-contract CI.
- Manual-only, protected, draft-only release workflow.
- Exact action-SHA pins, concurrency cancellation, and timeouts.
- Meaningful-change cadence for future weekly receipt audits.

## Local validation

- Release contract and negative publication test: passed.
- Skill validation: 27 of 27 passed.
- Worked-example validation: 22 passed; 5 correctly skipped without an
  example/manifest pair.
- Catalog regeneration: current at 27 skills across 7 domains.
- Rule/orchestrator resolution: 27 skills, 27 rules, 2 orchestrators; passed.
- YAML parse, diff integrity, and credential-pattern scan: passed.
- Tag topology: four local recovery receipts, zero remote tags; passed in both
  the audited checkout and clean-checkout modes.
- Full build-class preflight: held by the machine RAM reserve; no build-class
  workload or agent swarm was started. Cloud CI remains required.

## Human gates preserved

No merge, tag, GitHub release, website change, registry publication, downstream
port, announcement, or package publication was performed by this audit.
