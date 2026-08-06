---
name: claim-verification
description: "Fact-check a claim against sources and return a verdict with evidence and confidence — supported, refuted, partially-supported, or unverifiable. Use when asked to 'verify', 'fact-check', 'is this true', or before publishing a statistic or scientific claim."
version: 0.1.0
domain: research
tags: [fact-check, verification, evidence, sources]
---

# Claim Verification

> A claim + (optional) sources → a verdict with evidence and a calibrated
> confidence.

## Purpose

Before a claim ships in a post, brief, or video, it should be checked. This skill
takes a single claim, gathers or accepts sources, and returns a structured verdict
that separates what the evidence supports from what it doesn't — with honest
confidence, not false certainty.

## When it fires

- Keyword triggers: `verify`, `fact-check`, `is this true`, `confirm`,
  `source check`, `debunk`
- File triggers: `claims.md`, `fact-check/**`
- Command triggers: `/claim-verification`

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| `claim` | yes | The exact statement to check. |
| `sources` | no | Provided URLs/quotes; else the skill gathers them. |
| `strictness` | no | `standard` (default) or `high` (primary sources only). |

## Workflow

1. **Restate the claim precisely** — pin the testable assertion; flag ambiguity.
   ✅ Check: the claim is falsifiable as stated.
2. **Gather evidence** — find/accept sources; prefer primary and authoritative.
3. **Weigh** — does the evidence support, refute, or only partly cover the claim?
   Note source quality and any conflict.
4. **Verdict + confidence** — assign one of the four verdicts and a confidence
   level with a one-line rationale.
5. **Cite** — quote the decisive evidence with locations.

## Output contract

```json
{
  "claim": "string — restated precisely",
  "verdict": "supported | refuted | partially-supported | unverifiable",
  "confidence": "low | medium | high",
  "evidence": [{ "quote": "string", "source": "string" }],
  "rationale": "string",
  "caveats": ["string"]
}
```

## Tools & MCP

- Tools: `WebSearch`, `WebFetch`, `Read`.
- MCP dependencies: optional docs/library MCP for technical claims.

## Quality bar

- [ ] Verdict matches the evidence; `unverifiable` is used honestly.
- [ ] Confidence is calibrated, not defaulted to "high".
- [ ] Every verdict-driving quote is real and located.
- [ ] Source quality is considered, not just source count.

## Example

Input: "The James Webb Space Telescope orbits the Earth." → verdict `refuted`
(it orbits the Sun–Earth L2 point), high confidence, with a cited NASA source.

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
