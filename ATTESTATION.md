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
