# Public surface

Checked against `main` on 2026-10-06. This file records what is shipped and what is not. It does not move a release boundary.

## Shipped on main

- README badge and domain table say 41 skills across 8 domains.
- `docs/ROADMAP.md` marks v0.1 as shipped and records the post-v0.1.0 growth to 41 skills.
- Release text says the first GitHub release is a draft candidate at the historical 26-skill boundary.
- Skill frontmatter versions, repository releases, downstream ports, and website updates stay separate approval boundaries.

## Not shipped

- v0.2 consumption proof is still roadmap: `starlight-cosmos-engine` importing `skills/cosmos/*` and reading each `manifest.json`, `starlight-mcp` hooks for declared MCP dependencies, and porting the remaining creator-content domains into `agentic-creator-os`.
- Music and sound skills are not in this repo. `music-intelligence-systems` is documented here as README-only, with no cross-repo skills registry.
- Open pull requests #23, #25, and #29 are drafts. They are not on `main`.

## Next public step

Do not publish a GitHub release from this note. The next proof is a non-draft PR that shows one downstream consumer reading a cosmos `manifest.json`, with CI green, before any release tag moves.
