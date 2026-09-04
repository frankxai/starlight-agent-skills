# Architecture

## Where this repo sits

Starlight Agent Skills is the **portable capability layer** of the Starlight
ecosystem. It is a sibling to the Starlight Intelligence System — not a folder
inside it. The governing rule:

> **SIS remembers. MCP connects. Skills execute. Engines produce.**
> SIS can load skills; skills must not own SIS.

| Layer | Repo | Role |
|-------|------|------|
| Substrate / memory | `frankxai/Starlight-Intelligence-System` | Vaults, retrieval, protocol (SIP), platform adapters |
| **Skills** | **`frankxai/starlight-agent-skills`** | **Portable, reusable capability packs (this repo)** |
| Product control plane | `frankxai/agentic-ops` | Studio identity, topology, channel adapters, budgets and release contracts |
| Connectors | `frankxai/starlight-mcp` | External tool/data senses + hands (MCP servers) |
| Domain engine | `frankxai/starlight-cosmos-engine` | One domain machine — consumes `skills/cosmos/*` |
| Operation | `frankxai/agentic-creator-os` | Creator productivity OS that consumes skills |
| Universe | `frankxai/arcanea` | Mythic creative layer |

Think: SIS = brain/memory/protocol · Agent Skills = learned moves · MCP =
senses/hands · Cosmos Engine = one domain machine · sites/socials = public
nervous system.

## Why a separate repo

SIS is the operating substrate. It should not become a junk drawer for every
skill pack. Keeping skills sovereign means any consumer (SIS, ACOS, Arcanea, the
Cosmos Engine, or a third party) can pull exactly the skills it needs, version
them independently, and compose them under SIP attestation.

## How consumers load skills

- **Codex plugin** — `plugins/starlight-product-studios` packages byte-matched
  projections of the five canonical studio skills plus the Product Studio
  Director. The first release is skills-only; it does not claim an MCP server
  or app surface that has not been deployed and tested.
- **Claude Code / Codex / Cursor / Gemini / OpenCode** — copy a skill folder into
  the runtime's skills path (see [`../adapters/`](../adapters/)). `SKILL.md` is the
  same everywhere.
- **SIS / ACOS** — use `scripts/port-skill.mjs` to copy a skill into the target
  repo's skills tree with self-referential paths rewritten and attestation
  verified. Auto-activation is driven by [`../skill-rules.json`](../skill-rules.json).
- **`starlight-cosmos-engine`** — imports `skills/cosmos/*` and reads each skill's
  `manifest.json` to wire inputs/outputs and MCP dependencies. (Engine code is out
  of scope for this repo; only the contract is published here.)

## Auto-activation

`skill-rules.json` follows the ACOS/SIS schema: an `activation_rules[]` array of
`{ skill, triggers: { keywords, file_patterns, commands }, priority }`. A consuming
system fires a skill when the current context matches its triggers. Every `skill`
id in the rules file resolves to a real `skills/<domain>/<name>/SKILL.md`
(enforced by `scripts/check-rules.mjs`).

## Federated product studios

`skills/studios/*` provides five vertical managers: Publishing, Templates,
Software, Media, and World and Experience. The skills are portable execution
logic; they do not own portfolio or product truth. Reviewed `agentic-ops`
records select the studio, pack, repositories, budget and channel adapters.
Product repositories retain canonical source and release artifacts.

Cross-media work uses `agents/product-studio-director`. It appoints one primary
studio, gives other studios bounded sub-envelopes, keeps evidence append-only,
and returns one synthesized release receipt.

Plugin packaging is a generated distribution projection of this repository,
not another source of skill truth. `scripts/build_product_studios_plugin.py
--check` fails on any byte drift; `scripts/validate_plugin.py` also fails if a
studio entrypoint or the director disappears, or if the package claims an
undeployed MCP/app surface.
