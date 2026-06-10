# Roadmap

How this library sequences from a strong v0.1 to the capability layer the whole
Starlight ecosystem runs on. Decisions here were made with the CEO/CTO/CMO/CAIO
lenses; this is the "right place" the work is heading.

## v0.1 — Foundation (shipped)

- 22 skills across 6 domains, each with `examples/` + `tests/`.
- Rich-portable contract; runtime adapters; `skill-rules.json`; SIP attestation.
- Two reference orchestrators showing skill composition.
- Self-checking tooling + least-privilege CI; security-hardened porting.

## v0.2 — Consumption proof

- **`starlight-cosmos-engine` integration**: have the engine import `skills/cosmos/*`
  and read each `manifest.json` to wire inputs/outputs/MCP deps. This is the first
  real downstream consumer and validates the contract end-to-end.
- **`starlight-mcp` hooks**: where skills declare `mcp_dependencies`, point them at
  the NASA/ESA media connectors so fetching is real, not described.
- Port the Cosmos Pack into SIS + ACOS via `port-skill.mjs` and confirm
  auto-activation through `skill-rules.json`.

## v0.3 — Depth and breadth

- Deepen each domain (more research, media, education, coding, brand skills) driven
  by actual usage, not speculation.
- Add evals beyond golden checklists: small input→assert fixtures runnable in CI
  for the deterministic skills (coding labs, rights checks).
- More reference orchestrators per domain.

## Ongoing principles

- **Skills stay sovereign** — SIS loads skills; skills never own SIS.
- **Every artifact carries attestation** — silent composition is a protocol breach.
- **The contract is enforced, not hoped for** — validation + drift checks gate CI.
- **Quality over count** — a skill ships only when its `tests/` contract is real.
