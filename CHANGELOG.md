# Changelog

All notable changes to this repository are documented here. Individual skills
carry their own semver `version` in frontmatter; this log tracks the library.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

Repository-release status is verified in
[`docs/releases/release-ledger.json`](docs/releases/release-ledger.json). A
changelog heading is not, by itself, proof of a tag or GitHub release.

## [Unreleased]

### Added
- `substrate/notion-operating-system` — private-first Notion estate audits, parallel
  v2 rebuilds, template systems, and sanitized public mirrors (ported from the
  pre-v0.1.0 local library; substrate domain grows to 5, library to 27 skills).
- Executable example validation that checks worked outputs against each skill's
  manifest and caught two real contract mismatches.
- A source-verified music and sound skills index plus the public GitHub hero.
- A guarded release ledger, append-only release-status correction, and a
  manual, protected, draft-only GitHub release path.

### Changed
- Catalog counts and substrate-domain documentation now match the 27-skill tree.
- GitHub Actions dependencies advanced to v7 and are pinned to exact commits in
  the validation and release workflows.
- The claimed `v0.1.0` entry is now explicitly a historical candidate because
  the repository has no semantic tag or GitHub release yet.

### Release queue
- Eight audited commits after the historical `v0.1.0` boundary are queued for
  `v0.2.0`. Its immutable target will be chosen only after `v0.1.0` and this
  governance foundation are reviewed; no tag is inferred from calendar time.

## [0.1.0] - Candidate (historical boundary: 2026-06-22)

Draft repository release: `v0.1.0` at
`ff4efe5ac2bea17f080f1d85ba503277e3864a09`. No semantic tag or GitHub
release existed at the 2026-08-10 audit boundary.

### Added
- 26 skills across 7 domains. The creative domains (cosmos, research, media,
  education, coding, brand — 22 skills) each ship worked `examples/` and golden
  `tests/`; the `substrate` domain (4 brand-neutral operating skills:
  `agentic-income`, `affiliate-audit`, `payments-mandate`,
  `swarm-queen-coordination`) feeds the Starlight Intelligence System directly.
- Premium GitHub visual suite (`assets/github/`) and unified ecosystem README.
- Rich-portable skill contract (`SKILL.md` + `manifest.json` + `examples/` + `tests/`)
  and `templates/skill-template/`.
- Two reference orchestrators (`agents/`) that chain skills into pipelines, with
  CI verifying each only composes skills that exist.
- Runtime adapters for Claude, Codex, Cursor, Gemini, OpenCode, and SIS.
- Tooling: `validate_skills.py`, `generate_catalog.py`, `check-rules.mjs`,
  `port-skill.mjs`; `Makefile` (`make check`); CI with least-privilege permissions.
- `skill-rules.json` auto-activation; `Built on SIP` attestation + `ATTESTATION.md`.
- Governance: `SECURITY.md`, `CONTRIBUTING.md`, `CODEOWNERS`, `dependabot.yml`,
  `.editorconfig`, `docs/ROADMAP.md`.

### Security
- `port-skill.mjs`: path-traversal containment (validated id, rejected absolute/`..`
  dest, write-inside-target guard) and a bounded link-rewrite regex.
- `validate_skills.py`: manifest ↔ SKILL.md ↔ folder cross-validation; strict
  single-line frontmatter; exact `SKILL.md` filename match.
- CI reads with `permissions: contents: read` and uses no secrets.

### Fixed
- `validate_skills.py` / `generate_catalog.py` now read `SKILL.md` as UTF-8 (was
  `latin-1`), fixing mojibake in `docs/CATALOG.md` and inflated char counts.
- `check-rules.mjs` fails on duplicate skill names across domains.

[0.1.0]: https://github.com/frankxai/starlight-agent-skills/tree/ff4efe5ac2bea17f080f1d85ba503277e3864a09
