---
name: starlight-voice
description: "Apply the Starlight voice to any text — cool, premium, high-intellect, direct, technical, warm, playful; pattern recognition as poetry. Use when writing or rewriting content in the Starlight register, enforcing brand voice, or asked to 'make this sound like Starlight'."
version: 0.1.0
domain: brand
tags: [brand, voice, starlight, tone, editing]
---

# Starlight Voice

> Any draft → the same content in the Starlight register.

## Purpose

Starlight is the substrate brand register: cool, premium, intellectually serious,
and genuinely fun — direct and technical, but warm. This skill applies that voice
consistently and strips the failure modes (spiritual/guru language, vague
transformation talk, grandiose claims) so output reads as Starlight, not generic.

## When it fires

- Keyword triggers: `starlight voice`, `brand voice`, `make this sound like
  starlight`, `on-brand`, `rewrite in voice`
- File triggers: `content/**`, `*.mdx`, `*.md`
- Command triggers: `/starlight-voice`

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| `text` | yes | Draft to voice. |
| `mode` | no | `rewrite` (default) or `review` (annotate, don't change). |

## Voice rules

**Do:** lead with results; precise, technical language where it earns its keep;
show don't tell; confident but understated; pattern recognition framed vividly.
**Don't:** spiritual/consciousness language ("soul-aligned", "awakening",
"transformation"); grandiose impact claims; over-explaining motivation;
self-help-guru cadence.

**Test (Frank DNA):** every phrase should be *measurable, actionable, grounded,
earned* — if someone asks "what does that mean specifically?", you can answer with
an example.

## Workflow

1. **Diagnose** — flag off-register phrases (spiritual/vague/grandiose). ✅ Check:
   each flag cites the rule it breaks.
2. **Rewrite** (or annotate, in `review` mode) into the Starlight register.
3. **Preserve meaning + facts** — voice changes tone, not truth.
4. **Final pass** — does it sound cool, premium, and earned?

## Output contract

```json
{
  "mode": "rewrite | review",
  "result": "string — rewritten text (rewrite mode)",
  "flags": [{ "span": "string", "rule": "string", "fix": "string" }]
}
```

## Tools & MCP

- Tools: `Read`. MCP: none required.

## Quality bar

- [ ] No spiritual/guru/vague-transformation language remains.
- [ ] Claims are earned and specific.
- [ ] Facts unchanged; tone is cool, premium, warm, direct.

## Example

Input: "This soul-aligned system will transform your consciousness." →
`review` flags both phrases; `rewrite` → "This system changes how you work:
[specific, demonstrated outcome]."

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
