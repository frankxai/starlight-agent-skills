---
name: social-repurposer
description: "Repurpose one source asset (article, video, paper brief, image) into a platform-tailored social pack — X thread, LinkedIn post, Instagram caption, YouTube short script, newsletter blurb. Use when asked to 'repurpose', 'turn this into posts', 'make social content', or distribute one piece across channels."
metadata: {"version": "0.1.0", "domain": "media", "tags": ["social", "repurpose", "distribution", "multi-platform"]}
---

# Social Repurposer

> One source asset → a coordinated, platform-native social pack.

## Purpose

Most creators make one good thing and under-distribute it. This skill takes a
single source and produces channel-tailored variants that respect each platform's
norms (length, structure, CTA) while keeping the core message and facts consistent
— so distribution is a 10-minute step, not a second project.

## When it fires

- Keyword triggers: `repurpose`, `turn this into posts`, `social pack`,
  `cross-post`, `distribute`, `make threads`
- File triggers: `content/**`, `*.mdx`, `*.md`
- Command triggers: `/social-repurposer`, `/generate-social`

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| `source` | yes | Article/brief/video transcript/image + caption. |
| `platforms` | no | Subset of `x`, `linkedin`, `instagram`, `youtube-short`, `newsletter`. Default: all. |
| `voice` | no | `starlight` (default), `arcanea`, `frankx`. |

## Workflow

1. **Find the core** — the one message + the 3–5 supporting points worth carrying
   across channels. ✅ Check: message is true to the source.
2. **X thread** — hook post + 3–6 beats + closing CTA. No fabricated stats.
3. **LinkedIn** — first-line hook, 120–200 words, 1 insight, soft CTA.
4. **Instagram caption** — hook + value + 5–10 relevant hashtags (see
   [`caption-and-hashtag`](../caption-and-hashtag)).
5. **YouTube-short script** — 30–45s spoken, in the chosen voice.
6. **Newsletter blurb** — 2–3 sentences + link.
7. **Consistency pass** — every variant agrees on facts and message; carry any
   rights line from the source.

## Output contract

```json
{
  "core_message": "string",
  "x_thread": ["string — one per post"],
  "linkedin": "string",
  "instagram": { "caption": "string", "hashtags": ["string"] },
  "youtube_short": "string — script",
  "newsletter": "string",
  "rights_line": "string | null"
}
```

## Tools & MCP

- Tools: `Read`, `WebFetch` (if source is a URL).
- MCP dependencies: none required.

## Quality bar

- [ ] Each variant fits its platform's norms (length, structure).
- [ ] Facts are identical across variants and true to the source.
- [ ] Hooks respect the audience; no engagement-bait that distorts the message.
- [ ] Source rights/credit carried where the asset requires it.

## Example

See [`examples/example-01.md`](examples/example-01.md).

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
