---
name: starlight-spec
description: "Convert an approved product intent into a backlog-ready specification with boundaries, contracts, tasks, verification, rollback, and human approval points. Use when requirements are ambiguous, multiple components must change, or implementation needs a durable handoff."
metadata: {"version":"0.1.0","domain":"coding","tags":"specification,requirements,architecture,task-breakdown,verification"}
---

# Starlight Spec

## Purpose

Create an executable specification before code when the cost of ambiguity is greater than the cost of writing the contract.

## When it fires

- A feature spans more than one component or repository.
- Inputs, outputs, states, permissions, or failure behavior are unclear.
- The user asks for a PRD, technical design, or implementation plan.

## Inputs

- User outcome, audience, and decision owner.
- Existing architecture, conventions, and repository instructions.
- In-scope and out-of-scope behavior.
- Data sensitivity, runtime targets, compatibility, and delivery constraints.

## Workflow

1. Define the user-visible outcome and measurable acceptance criteria.
2. Record non-goals, assumptions, unknowns, and authority boundaries.
3. Map existing components and identify the smallest required change surface.
4. Specify data shapes, state transitions, APIs, errors, and compatibility behavior.
5. Decompose work by dependency and verification boundary, not an arbitrary line count.
6. Define tests, preview checks, observability, rollback, migration, and promotion gates.
7. Mark any unresolved choice that would materially change the design for human decision.

## Output contract

Return a specification containing:

- problem and user outcome;
- scope and non-goals;
- current-state evidence;
- functional and non-functional requirements;
- data, API, state, trust, and compatibility contracts;
- ordered implementation tasks with ownership;
- acceptance tests and manual verification;
- rollout, rollback, and migration plan;
- open decisions and human gates.

## Tools & MCP

Read the repository and its local instructions before naming files or commands. Browse primary documentation when an external API or current standard is involved. Use read-only inspection by default.

## Quality bar

- File and symbol references exist.
- Requirements are testable and do not smuggle in a preferred implementation.
- Failure, empty, loading, offline, and permission states are considered where relevant.
- No invented APIs, versions, metrics, or approvals.
- A different implementer can execute the spec without guessing the intent.

## Example

Input: “Let customers install one department on Codex and Claude.”

Good output: separate package, host adapter, installation, verification, rollback, and publication contracts, with marketplace approval and credentials explicitly outside autonomous authority.

---

Built on SIP — Starlight Intelligence Protocol
Vertical: starlight-agent-skills · portable capability layer
