---
name: rocket-launch-to-youtube
description: "Turn a rocket launch (mission details + footage notes) into a full YouTube package — title options, description, chapters, tags, and a long-form script. Use when producing a launch recap/explainer video, or asked to 'make a YouTube video about this launch'."
version: 0.1.0
domain: media
tags: [rocket, launch, youtube, longform, script]
---

# Rocket Launch → YouTube

> A launch + its facts → a complete long-form YouTube package.

## Purpose

Launches are high-interest events that reward fast, accurate long-form coverage.
This skill assembles the full YouTube package — clickable-but-honest titles, a
structured description with timestamps, tags, and a narrated script — grounded in
verified mission facts.

## When it fires

- Keyword triggers: `rocket launch`, `youtube video`, `launch recap`,
  `mission video`, `long-form script`
- File triggers: `videos/**`, `*.script.md`
- Command triggers: `/rocket-launch-to-youtube`

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| `mission` | yes | Vehicle, payload, provider, date, outcome (+ source). |
| `footage` | no | Notes on available clips/segments for chapters. |
| `length` | no | Target minutes, default `8`. |

## Workflow

1. **Verify mission facts** — vehicle, payload, provider, date, outcome from a
   cited source. ✅ Check: outcome confirmed, not assumed.
2. **Title options** — 3–5, accurate and compelling (no false drama).
3. **Script** — intro hook → context → the launch beat-by-beat → significance →
   outro/CTA, timed to `length`.
4. **Chapters** — timestamped sections matching the script/footage.
5. **Description** — 2–3 paragraphs + chapter list + sources.
6. **Tags** — relevant, non-spammy.
7. **Rights** — credit any agency/provider footage used.

## Output contract

```json
{
  "titles": ["string"],
  "script": "string",
  "chapters": [{ "time": "string", "title": "string" }],
  "description": "string",
  "tags": ["string"],
  "rights_line": "string | null"
}
```

## Tools & MCP

- Tools: `WebSearch`, `WebFetch`, `Read`. MCP: none required.

## Quality bar

- [ ] Mission outcome and facts are verified and cited.
- [ ] Titles are honest — no fabricated stakes.
- [ ] Chapters align with script timing.
- [ ] Footage credit included where required.

## Example

Input: "Falcon 9, Starlink batch, [date], nominal" + footage notes → titles,
8-min script, timestamped chapters, description with sources, tags.

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
