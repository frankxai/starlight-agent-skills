---
name: explain-like-cosmic-professor
description: "Explain any concept in the voice of a warm, rigorous cosmic professor — an analogy ladder from intuitive to precise, with a check-for-understanding. Use when asked to 'explain', 'ELI5/ELI-professor', teach a concept, or make a hard idea accessible without dumbing it down."
version: 0.1.0
domain: education
tags: [explainer, teaching, analogy, pedagogy]
---

# Explain Like a Cosmic Professor

> A concept → a layered explanation that climbs from intuition to precision.

## Purpose

Good teaching meets the learner where they are and lifts them up — without
sacrificing accuracy. This skill explains a concept as a warm, exacting professor
would: a hook, an analogy ladder (intuitive → mechanistic → precise), the common
misconception named and corrected, and a check-for-understanding.

## When it fires

- Keyword triggers: `explain`, `eli5`, `teach me`, `make this simple`,
  `intuition for`
- File triggers: `lessons/**`, `*.lesson.md`
- Command triggers: `/explain-like-cosmic-professor`

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| `concept` | yes | What to explain. |
| `level` | no | `curious-beginner` (default), `student`, `practitioner`. |
| `domain_flavor` | no | Optional space/cosmic framing for analogies. |

## Workflow

1. **Hook** — one line that makes the concept feel worth understanding.
2. **Analogy ladder** — start intuitive, then add mechanism, then state it
   precisely. Each rung must remain *true* (analogies that mislead are cut). ✅
   Check: the precise statement is correct.
3. **Name the misconception** — the common wrong model, and why it's wrong.
4. **Check for understanding** — one question (with answer) that tests the idea.
5. **Going deeper** — one pointer for the curious.

## Output contract

```json
{
  "hook": "string",
  "ladder": [{ "level": "intuitive | mechanistic | precise", "text": "string" }],
  "misconception": "string",
  "check": { "question": "string", "answer": "string" },
  "go_deeper": "string"
}
```

## Tools & MCP

- Tools: `Read`, optional `WebSearch`. MCP: none required.

## Quality bar

- [ ] The precise rung is factually correct.
- [ ] Analogies illuminate without introducing falsehoods.
- [ ] Misconception is real and corrected.
- [ ] Tone is warm and respects the learner.

## Example

Input: "redshift" → hook, 3-rung ladder ending in the precise definition, the
"it's just Doppler for everything" misconception named, plus a check question.

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
