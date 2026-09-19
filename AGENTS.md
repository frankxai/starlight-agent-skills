# Starlight Agent Skills — cross-harness agent contract

> The portable agent card. Same contract in Claude Code, Codex, Cursor, Gemini CLI, or OpenCode.
> Per-runtime detail lives in `adapters/`. This file is the SIP § 1 file-contract artifact for this repo.

**Tier:** T0 — substrate. Every session in the estate installs this repo, because other repos read its skills.
**Company:** Starlight Intelligence Systems · **Brand register:** `sis` (substrate — canon-free, functional names)
**Accountable seat:** `agent:starlight-caio` — agent/skill admission and the necessity gate
**Escalates to:** CEO, then Frank

Bands A (inherited DNA, guardrails, branch protocol) and B (company projection) are specified in
[`Starlight-Intelligence-System/docs/architecture/AGENTS-MD-CONTRACT.md`](https://github.com/frankxai/Starlight-Intelligence-System/blob/main/docs/architecture/AGENTS-MD-CONTRACT.md)
and will be generated into this file when `scripts/agents-md-project.mjs` ships. Everything below is Band C —
repo-local, hand-written, and **it outranks the generated bands on any conflict inside this repo.**

---

## What this repo is

A curated, production-grade skill library. Eight domains under `skills/`: `substrate`, `research`, `media`,
`education`, `coding`, `brand`, `cosmos`, `studios`. Plus three agents in `agents/`, six runtime adapters in
`adapters/`, and a Codex plugin manifest.

It is a **library, not an application**. It ships no runtime. Consuming repos install skills from here; nothing
here imports from them.

## The one rule

**The format is the product.** A skill that does not pass the validator is not a skill — it is a draft. The
strictness is deliberate: these files must load unmodified into five different runtimes, and strict hosts reject
custom top-level frontmatter keys. Loosening the standard to land one skill breaks portability for all of them.

## Before you change anything

```bash
make check     # the full gate — exactly what CI runs
```

`make check` chains six independent validators. Run it before every commit; run the individual targets while iterating:

| Target | Checks |
|---|---|
| `make validate` | Frontmatter, attestation, and manifest ↔ `SKILL.md` ↔ folder integrity |
| `make validate-examples` | Worked-example output JSON matches each skill's manifest contract |
| `make catalog` | Regenerates `docs/CATALOG.md` from skill frontmatter |
| `make catalog-check` | Fails if the committed catalog is stale — **commit the regenerated catalog** |
| `make rules` | Every rule and orchestrator resolves to a real skill; no name collisions |
| `make plugin` | Codex plugin manifest and five-studio package integrity |
| `make release-check` | Release history, attestation, receipts, publication safety |

Python 3 and Node are both required. `scripts/` holds the validators; do not bypass them.

## Adding a skill

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`docs/SKILL_SPEC.md`](docs/SKILL_SPEC.md) in full first. The
non-negotiables:

1. Path is `skills/<domain>/<skill-name>/SKILL.md`, domain from the eight above. No new domain without CAIO.
2. Frontmatter is Agent Skills-compatible: `name`, `description`, `metadata`. Starlight's `version` and `domain`
   go **inside** the single-line string-valued `metadata` object — never as top-level keys.
3. `name` is lowercase kebab-case, ≤ 64 chars, `^[a-z0-9]+(?:-[a-z0-9]+)*$`.
4. `description` is ≤ 1024 chars and says **when** it fires ("Use when …") with real trigger keywords. A
   description that does not name triggers will not activate.
5. Body follows the skeleton: Purpose · When it fires · Inputs · Workflow · Output contract · Tools & MCP ·
   Quality bar · Example.
6. Carries the `Built on SIP` attestation footer.
7. Passes `make check`, and the host-native validator where the target runtime provides one.

A `manifest.json` plus `examples/` and `tests/` are strongly recommended and required for anything with a
structured output contract.

## Adding an agent

The necessity gate is binding, and it is CAIO's: **a new agent must demonstrate a capability that no existing
agent + skill composition provides.** Most proposed agents are a skill. Write the skill.

## Do not

- Hand-edit `docs/CATALOG.md` — it is generated. Change frontmatter and run `make catalog`.
- Add a top-level frontmatter key outside the spec. Strict runtimes reject the whole file.
- Vendor a skill from a consuming repo back into this one without reading both versions first.
- Relax a validator to land a skill. Fix the skill.
- Ship a skill without its attestation footer.

## Branch and PR

Work on `agent/<harness>/<scope>` or the branch you were assigned. Open a **draft** PR. `make check` green before
marking ready. Never push directly to `main`.

Built on SIP.
