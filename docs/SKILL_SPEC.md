# Skill Spec — the rich-portable contract

Every skill in this library is a **self-contained, portable package**. It is
canonical in one place (`SKILL.md`) and adapts to every runtime without being
rewritten. This document is the contract the validator (`scripts/validate_skills.py`)
and CI enforce.

## Folder layout

```
skills/<domain>/<skill-name>/
├── SKILL.md          # REQUIRED — canonical instructions + frontmatter
├── manifest.json     # OPTIONAL — machine-readable I/O + dependency contract
├── references/       # OPTIONAL — deep material loaded on demand
├── examples/         # OPTIONAL — worked input → output examples
└── tests/            # OPTIONAL — golden-checklist asserting the output contract
```

- `<domain>` ∈ `research`, `media`, `education`, `coding`, `brand`, `cosmos`.
- `<skill-name>` is kebab-case and matches `^[a-z0-9][a-z0-9-]*$`.

## `SKILL.md` frontmatter (validated)

```yaml
---
name: apod-to-short          # kebab-case, ≤64 chars, ^[a-z0-9][a-z0-9-]*$
description: "What it does + 'Use when …' triggers. ≤1024 chars."
version: 0.1.0               # semver X.Y.Z
domain: cosmos              # one of the 6 domains
tags: [nasa, video, social] # optional, free-form
---
```

Required keys: `name`, `description`, `version`, `domain`. Every `SKILL.md` MUST
also contain the `Built on SIP` attestation footer (checked by the validator).

## `SKILL.md` body — consistent sections

So skills are predictable to read and to auto-activate, the body follows the same
skeleton (see [`templates/skill-template/SKILL.md`](../templates/skill-template/SKILL.md)):

**Purpose · When it fires · Inputs · Workflow · Output contract · Tools & MCP ·
Quality bar · Example.**

Keep `SKILL.md` lean (target <500 lines). Push deep reference material into
`references/` so it is loaded only when needed (progressive disclosure).

## `manifest.json` (optional but recommended)

Machine-readable mirror of the skill's contract — lets engines (e.g.
`starlight-cosmos-engine`) and orchestrators discover inputs, outputs, tools, and
MCP dependencies without parsing prose. Shape: see
[`templates/skill-template/manifest.json`](../templates/skill-template/manifest.json).

## Portability model

`SKILL.md` is the **single source of truth**. Runtimes differ only in *where the
file lives* and *how discovery happens* — never in the instructions. Per-runtime
guidance lives once in [`adapters/`](../adapters/), not duplicated per skill.

## Attestation

Every skill carries the `Built on SIP` footer. This is non-decorative: it is the
protocol-level attribution that lets the skill compose across the Starlight
ecosystem. See [`../ATTESTATION.md`](../ATTESTATION.md).
