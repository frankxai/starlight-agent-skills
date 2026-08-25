---
name: starlight-spec
description: "Author a rigorous, backlog-ready 5-Phase Product Specification & Task Breakdown. Turns vague intent or high-level features into executable, test-driven PRDs."
version: 1.0.0
domain: coding
tags: [spec, prd, requirements, task-breakdown, product-management]
---

# Starlight Spec — 5-Phase PRD & Task Decomposition Engine

> Transform vague feature requests into structured, executable specifications with clear verification contracts.

## Purpose

Engineering friction occurs when agents or builders begin writing code before defining requirements, constraints, and success criteria. `starlight-spec` guides the formulation of specifications through five structured phases:

1. **Phase 1: Intent & Problem Statement** — Who is this for, what pain is eliminated, and why does this exist?
2. **Phase 2: Clarification & Boundaries** — Non-negotiable constraints, out-of-scope declarations, and data contracts.
3. **Phase 3: Technical Architecture** — Component models, API endpoints, file modifications, and state machines.
4. **Phase 4: Task Decomposition** — Logical, sequential units of work that can be committed incrementally.
5. **Phase 5: Verification Contract** — Automated tests, manual walkthrough steps, and exit criteria.

## Workflow

```
[Intent] ──> [Clarification] ──> [Architecture] ──> [Tasks] ──> [Verification]
```

1. **Frame the User Outcome:** Define the user-visible delta before touching code.
2. **Identify Touchpoints:** List every file, type, function, and config that will be touched.
3. **Draft Unit Tasks:** Group work into commits of ≤150 lines with clean diff boundaries.
4. **Define the Verification Suite:** Name the exact test commands and visual inspection points that prove completion.

---

Built on SIP — Starlight Intelligence Protocol  
Vertical: starlight-agent-skills · autonomous capability layer
