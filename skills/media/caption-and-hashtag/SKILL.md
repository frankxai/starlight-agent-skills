---
name: caption-and-hashtag
description: "Write a platform-tuned caption plus a researched, non-spammy hashtag set for a post. Use when finishing a social post, asked for 'caption and hashtags', or optimizing reach for Instagram/TikTok/X/LinkedIn."
version: 0.1.0
domain: media
tags: [caption, hashtags, social, instagram, reach]
---

# Caption & Hashtag

> A post's subject → a platform-tuned caption + a tiered hashtag set.

## Purpose

Captions and hashtags are where reach is won or wasted. This skill writes a
caption that fits the platform's voice and produces a tiered hashtag set (broad /
niche / branded) that's relevant rather than spammy — calibrated to the platform's
norms.

## When it fires

- Keyword triggers: `caption`, `hashtags`, `caption and hashtags`, `tags for post`
- File triggers: `posts/**`
- Command triggers: `/caption-and-hashtag`

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| `subject` | yes | What the post is about (+ any link/credit). |
| `platform` | yes | `instagram`, `tiktok`, `x`, `linkedin`. |
| `voice` | no | `starlight` (default), `arcanea`, `frankx`. |

## Workflow

1. **Caption** — hook line + value + optional CTA, sized to the platform (IG/TikTok
   short; LinkedIn longer; X terse). ✅ Check: fits platform length norms.
2. **Hashtag tiers** — broad (reach), niche (relevance), branded (identity). Count
   per platform norm (IG ~8–12; TikTok ~3–5; X ~1–3; LinkedIn ~3–5).
3. **Relevance + safety pass** — drop spammy/banned/irrelevant tags; keep facts true.
4. **Carry credit** — include any required image credit.

## Output contract

```json
{
  "caption": "string",
  "hashtags": { "broad": ["string"], "niche": ["string"], "branded": ["string"] },
  "platform": "string"
}
```

## Tools & MCP

- Tools: `Read`, optional `WebSearch` for trending tags. MCP: none required.

## Quality bar

- [ ] Hashtag count matches the platform norm; no spam/banned tags.
- [ ] Caption length and tone fit the platform.
- [ ] Claims true; credit carried if needed.

## Example

Input: "Webb image of the Carina Nebula", platform `instagram` → a caption + ~10
tiered hashtags, credit line included.

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
