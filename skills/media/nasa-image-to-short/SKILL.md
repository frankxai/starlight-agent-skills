---
name: nasa-image-to-short
description: "Turn any NASA/ESA still image (not just APOD) into a vertical short package — hook, narration, captions, shot list, rights line. Use when making a space short/reel from a specific image, a gallery still, or a mission photo."
version: 0.1.0
domain: media
tags: [nasa, image, short, video, social]
---

# NASA Image → Short

> Any NASA/ESA still → a ready-to-shoot vertical short.

## Purpose

The general-purpose sibling of `cosmos/apod-to-short`: works for any agency still
(mission photo, gallery image, instrument capture), not just the daily APOD. Same
discipline — true facts, exact credit, shootable structure.

## When it fires

- Keyword triggers: `image short`, `space short`, `reel from this image`,
  `nasa photo short`
- File triggers: `images/**`, `*.jpg`, `*.png`
- Command triggers: `/nasa-image-to-short`

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| `image` | yes | Image URL/page with caption + credit. |
| `length` | no | Target seconds, default `40`. |
| `voice` | no | `starlight` (default), `arcanea`, `frankx`. |

## Workflow

1. **Resolve caption + credit** — verbatim credit; flag non-NASA parties. ✅ Check: credit captured.
2. **One true idea** — the single surprising, accurate fact.
3. **Hook (0–3s)** — earn attention without distorting science.
4. **Narration** — timed to `length` at ~2.5 words/sec; claims traceable to caption.
5. **Captions** — ≤7-word on-screen beats.
6. **Shot list** — Ken Burns moves + label overlays; no fabricated footage.
7. **Rights line** — route non-NASA credit through [`../../cosmos/rights-check-nasa-esa`](../../cosmos/rights-check-nasa-esa).

## Output contract

```json
{
  "hook": "string",
  "script": "string",
  "captions": ["string"],
  "shot_list": ["string"],
  "rights_line": "string",
  "duration_sec": "number"
}
```

## Tools & MCP

- Tools: `WebFetch`, `Read`. MCP: none required.

## Quality bar

- [ ] Facts traceable to the caption; no invented numbers.
- [ ] Rights line verbatim; non-NASA flagged.
- [ ] Narration fits `length`.

## Example

Input: a Hubble gallery still + caption → a 40s short package with a verbatim
credit line and caption-traceable narration.

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
