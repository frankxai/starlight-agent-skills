---
name: coding-challenge-generator
description: "Generate a graded set of coding challenges around a topic — progressive difficulty, each with statement, constraints, hidden tests, and solution. Use when building a problem set, a challenge ladder, interview prep, or a curriculum of exercises."
version: 0.1.0
domain: education
tags: [coding, challenges, problem-set, curriculum, assessment]
---

# Coding Challenge Generator

> A topic + difficulty range → a graded ladder of auto-checkable challenges.

## Purpose

Single exercises are easy; a *coherent ladder* that builds a skill is hard. This
skill emits a set of challenges of rising difficulty around one topic, each fully
specified and testable — ready to drop into a course, a bootcamp, or interview
prep. (For a single richly-scaffolded space-themed lab, use
[`../../coding/cosmic-code-lab`](../../coding/cosmic-code-lab).)

## When it fires

- Keyword triggers: `coding challenges`, `problem set`, `exercises`,
  `challenge ladder`, `interview prep`
- File triggers: `challenges/**`, `problems/**`
- Command triggers: `/coding-challenge-generator`

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| `topic` | yes | Skill/concept the set trains (e.g. "recursion"). |
| `language` | no | `python` (default) or `javascript`. |
| `count` | no | Number of challenges, default `5`. |
| `range` | no | Difficulty span, default `intro→advanced`. |

## Workflow

1. **Decompose the topic** into a rising sequence of sub-skills. ✅ Check: each
   step depends on the prior.
2. **Per challenge:** statement, constraints, input/output spec, hidden tests
   (happy + edge + error), and a reference solution that passes them.
3. **Grade the ladder** — assign a difficulty label; verify monotonic increase.
4. **Self-verify** — each solution passes its tests; each empty starter fails.

## Output contract

```json
{
  "topic": "string",
  "challenges": [{
    "title": "string",
    "difficulty": "intro | easy | medium | hard | advanced",
    "statement": "string",
    "starter_code": "string",
    "tests": "string",
    "solution": "string"
  }]
}
```

## Tools & MCP

- Tools: `Write`, `Bash` (run tests). MCP: none required.

## Quality bar

- [ ] Difficulty increases monotonically and is justified.
- [ ] Each solution passes its tests; each starter fails them.
- [ ] Statements are implementable from text alone.

## Example

Input: topic "recursion", count 5 → five Python challenges from factorial to a
tree traversal, each with hidden tests and a passing solution.

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
