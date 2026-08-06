---
name: mission-page-to-summary
description: "Turn an official mission page (NASA/ESA/JPL spacecraft, instrument, or mission site) into a clean, accurate summary — objective, timeline, instruments, status, and key results. Use when summarizing a space mission, building a mission card, or asked to 'explain this mission' from an agency page."
version: 0.1.0
domain: research
tags: [mission, nasa, esa, summary, spacecraft]
---

# Mission Page → Summary

> An official mission page → a structured, accurate mission summary.

## Purpose

Agency mission pages are authoritative but sprawling. This skill distills one into
a consistent summary card — objective, key dates, instruments, current status, and
headline results — sourced only from the official page, so it's safe to publish or
template across a mission catalog.

## When it fires

- Keyword triggers: `mission`, `spacecraft`, `mission summary`, `mission card`,
  `nasa mission`, `esa mission`
- File triggers: `content/missions/**`, `*.mission.md`
- Command triggers: `/mission-page-to-summary`

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| `page` | yes | Official mission/instrument page URL or text. |
| `format` | no | `card` (default) or `long`. |

## Workflow

1. **Identify the mission** — name, agency, mission type. ✅ Check: official name captured.
2. **Objective** — the mission's stated goal, in one or two sentences.
3. **Timeline** — launch date, key milestones, end/extended status; only dates the page states.
4. **Instruments/payload** — list with one-line purposes.
5. **Status** — current operational state as the page reports it.
6. **Key results** — notable findings, each attributable to the page.
7. **Source line** — link the official page.

## Output contract

```json
{
  "name": "string",
  "agency": "string",
  "objective": "string",
  "timeline": [{ "date": "string", "event": "string" }],
  "instruments": [{ "name": "string", "purpose": "string" }],
  "status": "string",
  "key_results": ["string"],
  "source": "string — official URL"
}
```

## Tools & MCP

- Tools: `WebFetch`, `Read`.
- MCP dependencies: none required.

## Quality bar

- [ ] Every date/result is on the official page — no memory-filled gaps.
- [ ] Mission name and agency are correct and official.
- [ ] Status reflects the page, with the page's date noted if available.

## Example

Input: a NASA mission page URL → output a populated mission card whose every
timeline entry and result links back to that page.

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
