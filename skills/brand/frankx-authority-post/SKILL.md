---
name: frankx-authority-post
description: "Write a FrankX authority post — an AI-Architect-voiced LinkedIn/X post that leads with a result, teaches one concrete lesson, and stays humble. Use when drafting a thought-leadership post as FrankX, sharing a build/insight, or asked for an 'authority post'."
version: 0.1.0
domain: brand
tags: [frankx, authority, linkedin, thought-leadership, ai-architect]
---

# FrankX Authority Post

> An insight or shipped result → a FrankX-voiced authority post.

## Purpose

FrankX's positioning is *elite creator, AI architect, humble*. This skill drafts
authority content in that voice: lead with a demonstrated result, extract one
concrete, teachable lesson, and let the work speak — no guru cadence, no grandiose
claims. Output is ready to post on LinkedIn or X.

## When it fires

- Keyword triggers: `authority post`, `frankx post`, `thought leadership`,
  `linkedin post`, `share this insight`
- File triggers: `posts/**`
- Command triggers: `/frankx-authority-post`

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| `seed` | yes | The result/insight/build to post about. |
| `platform` | no | `linkedin` (default) or `x`. |
| `cta` | no | Optional soft call-to-action. |

## Voice rules

Lead with results and demonstrated expertise; precise/technical where useful;
show don't tell; confident but understated. **Avoid:** spiritual/consciousness
language, grandiose impact claims, over-explaining motivation, self-help cadence.
Every claim must be earned and specific.

## Workflow

1. **Find the result** — the concrete, true thing that earns attention. ✅ Check:
   it's demonstrated, not asserted.
2. **Hook** — first line states the result or the surprising lesson.
3. **Body** — the one lesson, with enough specifics to be useful; humble about scope.
4. **Close** — optional soft CTA or open question.
5. **Voice pass** — strip guru/grandiose phrasing; verify every claim is earned.

## Output contract

```json
{
  "platform": "linkedin | x",
  "post": "string",
  "hook": "string — first line",
  "lesson": "string — the one teachable point",
  "claims_checked": ["string — each claim + why it's earned"]
}
```

## Tools & MCP

- Tools: `Read`. MCP: none required.

## Quality bar

- [ ] Leads with a demonstrated result, not a claim.
- [ ] Exactly one clear, concrete lesson.
- [ ] No spiritual/guru/grandiose language.
- [ ] Humble in tone; specifics over superlatives.

## Example

Input: "Shipped a 6-skill portable library that runs across 5 runtimes" → a
LinkedIn post leading with that result, teaching one lesson about portable skill
design, with a soft question close.

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
