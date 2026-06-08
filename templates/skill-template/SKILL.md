---
name: skill-name-here
description: "One or two sentences. Lead with what it does, then the trigger: 'Use when …' with concrete keywords the model will match on. Keep under 1024 characters."
version: 0.1.0
domain: research
tags: [tag-one, tag-two]
---

# Skill Name Here

> One-line statement of the transformation this skill performs: input → output.

## Purpose

What this skill is for, in two or three sentences. What problem it removes, and
who benefits. Grounded and concrete — no claims you can't demonstrate.

## When it fires

- Keyword triggers: `keyword`, `another keyword`
- File triggers: `*.ext`, `path/pattern/**`
- Command triggers: `/some-command`

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| `source` | yes | What the user supplies (URL, file, topic). |
| `options` | no | Tunable parameters and their defaults. |

## Workflow

1. **Step one** — what to do, and the check that proves it worked.
2. **Step two** — …
3. **Step three** — …

Keep this section as a checkable procedure, not prose. Each step should have an
observable result so the agent can verify before moving on.

## Output contract

Describe exactly what the skill produces. If it emits structured output, show the
shape (matches `manifest.json` → `outputs`):

```json
{
  "field": "type — meaning"
}
```

## Tools & MCP

- Tools used: `Read`, `WebFetch`, …
- MCP dependencies (if any): name them and what they provide. List the same set in
  `manifest.json` → `mcp_dependencies`.

## Quality bar

- [ ] A specific, checkable criterion the output must meet.
- [ ] Another one. Facts verifiable, rights respected, voice on-brand.

## Example

See [`examples/`](examples/). Show one real input and the resulting output.

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
