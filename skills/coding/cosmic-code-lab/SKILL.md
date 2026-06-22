---
name: cosmic-code-lab
description: "Generate a runnable, space-themed coding lab — a problem statement, starter code, hidden tests, and a worked solution — in Python or JavaScript. Use when creating coding exercises, a 'code lab', an interactive tutorial, or a space/astronomy programming challenge."
version: 0.1.0
domain: coding
tags: [education, coding, exercise, lab, astronomy]
---

# Cosmic Code Lab

> A learning objective → a self-contained, auto-checkable coding lab with a
> space-science backdrop.

## Purpose

Space data makes great programming practice (orbital math, image stats, light
travel time, catalog parsing). This skill produces a complete lab — a clear
problem, runnable starter code, a hidden test suite, and a reference solution —
so an educator or platform can drop it into a course without writing the
scaffolding by hand.

## When it fires

- Keyword triggers: `code lab`, `coding challenge`, `exercise`, `kata`,
  `tutorial`, `cosmic code`
- File triggers: `labs/**`, `*.lab.md`, `test_*.py`, `*.test.js`
- Command triggers: `/cosmic-code-lab`

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| `objective` | yes | The concept/skill to teach (e.g. "parse a star catalog"). |
| `language` | no | `python` (default) or `javascript`. |
| `level` | no | `intro`, `intermediate` (default), `advanced`. |

## Workflow

1. **Frame the problem** — a concrete, space-flavored task that isolates the
   `objective`. State inputs, outputs, and constraints precisely. ✅ Check: a
   competent student could implement it from the statement alone.
2. **Write starter code** — minimal scaffold with a clearly marked TODO and a
   stable function signature.
3. **Write hidden tests** — a runnable suite (pytest / a tiny JS harness) covering
   the happy path, an edge case, and an error case. Tests must pass on the
   solution and fail on the empty starter.
4. **Write the reference solution** — clean, idiomatic, commented at decision points.
5. **Add the science note** — 2–3 lines on the real astronomy behind the problem,
   factually correct.
6. **Self-verify** — confirm the solution passes the tests and the starter does not.

## Output contract

```json
{
  "title": "string",
  "language": "python | javascript",
  "problem_statement": "string",
  "starter_code": "string",
  "tests": "string — runnable test source",
  "solution": "string",
  "science_note": "string"
}
```

## Tools & MCP

- Tools: `Write` (lab files), `Bash` (run the tests to self-verify).
- MCP dependencies: none required.

## Quality bar

- [ ] Solution passes the tests; empty starter fails them.
- [ ] Problem statement is implementable from text alone.
- [ ] Tests cover happy path + at least one edge + one error case.
- [ ] Science note is factually correct.

## Example

See [`examples/example-01.md`](examples/example-01.md).

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
