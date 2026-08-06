# Security Policy

## Scope

This repository ships **executable tooling** alongside its skills:

- `scripts/port-skill.mjs` writes files into a caller-supplied `--target` repo.
- `scripts/validate_skills.py`, `scripts/generate_catalog.py`, `scripts/check-rules.mjs`
  read repo files and run in CI.

Skills themselves (`skills/**/SKILL.md`) are instructions for AI agents. Treat any
content an agent fetches at runtime (web pages, images, API responses) as
untrusted input, and never let a skill exfiltrate secrets or act outside its
stated contract.

## Hardening already in place

- `port-skill.mjs` validates the `<domain>/<skill>` id against `^[a-z0-9][a-z0-9-]*$`,
  rejects absolute or `..`-bearing `--dest`, and refuses to write outside the
  resolved `--target` (path-traversal containment).
- It refuses to port any skill missing its `Built on SIP` attestation footer.
- The CI workflow runs with least privilege (`permissions: contents: read`) and
  uses no secrets.
- `validate_skills.py` cross-checks every `manifest.json` against its `SKILL.md`
  and folder, and rejects malformed/multi-line frontmatter.

## Reporting a vulnerability

Please report security issues privately via GitHub Security Advisories
("Report a vulnerability" on the repo's **Security** tab) rather than opening a
public issue. We aim to acknowledge within 5 business days.

When porting skills into a downstream repo, always run with `--dry-run` first and
review the planned writes.
