---
name: arxiv-space-paper-to-brief
description: "Turn an astrophysics/space-science arXiv paper into a structured brief tuned for space audiences — adds object/mission context, instruments, and observational caveats. Use when summarizing an astro-ph paper, a space-science result, or a mission's published findings."
metadata: {"version": "0.1.0", "domain": "cosmos", "tags": ["arxiv", "astrophysics", "space", "brief", "astro-ph"]}
---

# arXiv Space Paper → Brief

> An astro-ph paper → a structured brief with the context space readers need.

## Purpose

The space-tuned sibling of [`../../research/arxiv-paper-to-brief`](../../research/arxiv-paper-to-brief).
Same rigor, plus the context astrophysics readers expect: which objects/missions,
which instruments, and the observational caveats (selection effects, calibration,
model assumptions) that determine how much to trust a result.

## When it fires

- Keyword triggers: `astro-ph`, `astrophysics paper`, `space paper`,
  `observation paper`, `mission result`
- File triggers: `papers/astro/**`, `*.pdf`
- Command triggers: `/arxiv-space-paper-to-brief`

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| `paper` | yes | arXiv URL/ID, PDF, or text. |
| `audience` | no | `astronomer` (default), `enthusiast`, `general`. |

## Workflow

1. **Metadata + identifier** — title, authors, date, arXiv ID. ✅ Check: ID captured.
2. **Object/mission context** — what was observed and with which facility/instrument.
3. **Problem + method** — faithful to the paper.
4. **Results** — each tied to a figure/table; claimed vs. demonstrated separated.
5. **Observational caveats** — selection effects, calibration, sample size, model
   dependence. Be candid — this is where space results are over-read.
6. **Why it matters** — for the chosen audience.
7. **Citations** — exact quotes/figures with locations.

## Output contract

```json
{
  "metadata": { "title": "string", "authors": "string", "id": "string", "date": "string" },
  "context": { "objects": ["string"], "instruments": ["string"] },
  "problem": "string",
  "method": "string",
  "results": [{ "claim": "string", "evidence": "string" }],
  "caveats": ["string — observational/statistical"],
  "why_it_matters": "string",
  "citations": ["string"]
}
```

## Tools & MCP

- Tools: `WebFetch`, `Read`. MCP: optional docs/library MCP.

## Quality bar

- [ ] Instruments/objects named correctly.
- [ ] Observational caveats are substantive, not generic.
- [ ] Results tied to figures/tables; identifier correct.

## Example

Input: an astro-ph exoplanet-atmosphere paper → brief with the telescope/instrument,
the detection claim tied to a figure, and caveats on signal-to-noise and model
assumptions.

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
