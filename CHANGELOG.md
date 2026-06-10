# Changelog

All notable changes to this repository are documented here. Individual skills
carry their own semver `version` in frontmatter; this log tracks the library.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [0.1.0]

### Added
- 22 skills across 6 domains (cosmos, research, media, education, coding, brand),
  each with worked `examples/` and golden `tests/`.
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

[0.1.0]: https://github.com/frankxai/starlight-agent-skills/releases/tag/v0.1.0
