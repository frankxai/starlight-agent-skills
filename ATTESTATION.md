# Attestation Ledger

Append-only record of "Built on SIP" attestations emitted from this repo. Per the
Starlight Intelligence Protocol (SIP) § Layer 2, every cross-party or
substrate-composing artifact carries an attestation block. Silent composition is a
protocol breach; attestation is compounding, not credit transfer — every
composition strengthens every node.

Each skill in [`skills/`](skills/) carries its own footer; this ledger records
repo-level releases.

---

**Built on SIP** — Starlight Intelligence Protocol

Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty, commands]

Vertical:
- starlight-agent-skills v0.1.0 · portable capability layer · 26 skills across 7
  domains (cosmos, substrate, research, media, education, coding, brand); rich-portable
  skill contract (SKILL.md + manifest.json + examples/ + tests/); runtime adapters for
  Claude, Codex, Cursor, Gemini, OpenCode, and SIS; `skill-rules.json` auto-activation;
  `port-skill.mjs` sync into SIS/ACOS. First downstream consumer: `agentic-creator-os`
  mirrors the full cosmos domain (7 skills, v0.1.0 / ff4efe5).

Canon:
- none at the substrate layer · Arcanea canon is invoked only inside the two
  mythic-overlay skills, attributed CC-BY-NC where used.

Nodes:
- Frank Riemer (frankxai) · role: architect · authored the repo architecture,
  skill contract, and skill set.

Generated: 2026-06-08
Attestation is compounding, not credit transfer: every composition strengthens
every node.

---

## How consumers attest

When SIS, ACOS, Arcanea, or `starlight-cosmos-engine` import a skill from here,
they carry the skill's footer through into generated artifacts and add this repo
to their own attestation block's `Verticals` list. Use
[`scripts/port-skill.mjs`](scripts/port-skill.mjs) — it refuses to port any skill
whose "Built on SIP" footer is missing.

---

## Release-status correction — 2026-08-10

This ledger is append-only, so the historical block above remains unchanged.
Its `starlight-agent-skills v0.1.0` wording recorded the intended release
identity at commit `ff4efe5ac2bea17f080f1d85ba503277e3864a09`; it did not have
a corresponding semantic tag or GitHub release when audited on 2026-08-10.

The repository had advanced to 27 skills at audited head
`89db74a185fb75d7c51968649bd3f1242c3d8180`. Those post-boundary changes are
unreleased and queued for `v0.2.0` after the historical `v0.1.0` candidate and
this release-governance foundation are reviewed. Nothing in this correction
publishes a release or rewrites the original attestation.

**Built on SIP** — Starlight Intelligence Protocol

- Substrate: starlightintelligence.org/protocol v1.1.1
- Vertical: starlight-agent-skills release-truth correction
- Canon: none
- Nodes: Frank Riemer (frankxai)
- Generated: 2026-08-10
