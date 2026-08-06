---
name: thumbnail-concept
description: "Generate high-CTR thumbnail concepts for a video — layout, focal subject, text overlay (≤4 words), color/contrast, and an image-gen prompt. Use when designing a YouTube/short thumbnail, asked for 'thumbnail ideas', or planning cover art for a video."
version: 0.1.0
domain: media
tags: [thumbnail, design, youtube, cover, ctr]
---

# Thumbnail Concept

> A video topic → several high-CTR thumbnail concepts with image-gen prompts.

## Purpose

The thumbnail decides whether good content gets watched. This skill produces a
few distinct, honest, high-contrast thumbnail concepts — each with a layout, a
short text overlay, a color logic, and a ready image-generation prompt — so the
creator can pick and generate quickly.

## When it fires

- Keyword triggers: `thumbnail`, `cover art`, `thumbnail ideas`, `ctr`,
  `video cover`
- File triggers: `thumbnails/**`
- Command triggers: `/thumbnail-concept`

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| `topic` | yes | Video subject + the promise. |
| `subject` | no | Hero image/asset (e.g. a nebula, a rocket). |
| `count` | no | Number of concepts, default `3`. |

## Workflow

1. **Find the visual hook** — the single image idea that conveys the promise. ✅ Check: readable at small size.
2. **Per concept:** layout (subject placement, rule-of-thirds), overlay text
   (≤4 words, high contrast), color/contrast logic, and emotional read.
3. **Honesty check** — the thumbnail must match the actual content (no bait).
4. **Image-gen prompt** — a concrete prompt to produce the background/subject;
   if using NASA imagery, note the rights step.

## Output contract

```json
{
  "concepts": [{
    "layout": "string",
    "overlay_text": "string — ≤4 words",
    "color_logic": "string",
    "emotional_read": "string",
    "image_prompt": "string"
  }]
}
```

## Tools & MCP

- Tools: `Read`. MCP: optional image-gen MCP.

## Quality bar

- [ ] Overlay text ≤4 words and legible at thumbnail size.
- [ ] Concept matches the real content (no clickbait).
- [ ] High contrast / clear focal point.
- [ ] Rights noted if real agency imagery is used.

## Example

Input: "Why Webb sees what Hubble can't" → 3 concepts, each with a 2–3 word
overlay, contrast logic, and an image prompt.

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
