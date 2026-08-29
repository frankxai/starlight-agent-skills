---
name: starlight-autoplan
description: "Review a non-trivial implementation plan through product, engineering, design, and developer-experience lenses, then reconcile the findings into an evidence-gated execution plan. Use when a change crosses multiple systems, carries meaningful risk, or needs an explicit build/no-build decision."
metadata: {"version":"0.1.0","domain":"coding","tags":"planning,review,architecture,design,devex,quality-gate"}
---

# Starlight Autoplan

## Purpose

Turn a rough proposal into a bounded plan whose assumptions, risks, authority limits, and verification gates are visible before implementation begins.

## When it fires

- The user asks to review, harden, or stress-test a plan.
- The work crosses product, data, security, design, runtime, or deployment boundaries.
- A wrong decision would be expensive or difficult to reverse.

Do not invoke the full review for a trivial, reversible edit unless the user asks for it.

## Inputs

- Desired user outcome and explicit non-goals.
- Current repository or system evidence.
- Time, cost, compatibility, privacy, and authority constraints.
- Known failure history and required verification commands.

## Workflow

1. Restate the outcome, success criteria, non-goals, and unresolved assumptions.
2. Select review depth proportional to reversibility and impact.
3. Run four lenses: product value, engineering integrity, design quality, and developer/operator experience.
4. Give every finding an evidence reference, confidence level, and consequence.
5. Reconcile contradictions; never silently average incompatible recommendations.
6. Produce the smallest coherent execution sequence with rollback and promotion gates.
7. Stop for human direction before destructive, costly, public, or credential-bearing actions.

When the same agent performs every lens, disclose that the review was sequential rather than independent.

## Output contract

Return:

- `decision`: build, revise, defer, or stop.
- `scope`: user-visible outcome, non-goals, and affected surfaces.
- `assumptions`: verified, inferred, and unresolved items kept separate.
- `reviews`: findings from each lens with severity and evidence.
- `execution_plan`: ordered, independently verifiable steps.
- `verification`: automated, manual, security, accessibility, and deployment gates as applicable.
- `rollback`: safe recovery path and ownership.
- `human_gates`: decisions the agent may not make.

## Tools & MCP

Use repository search, tests, type/lint gates, preview deployments, and an approved browser connector when relevant. Do not enable connectors, spend money, publish, merge, or mutate external systems merely because a plan mentions them.

## Quality bar

- No claim that AI makes execution free or removes operational ownership.
- No speculative expansion without a stated user outcome.
- Evidence and inference are distinguishable.
- Every high-risk step has a verifier and rollback.
- The plan can be handed to another operator without hidden context.

## Example

Input: “Add a self-service agent marketplace with portable plugins.”

Good output: a revise decision that separates catalog, package, installer, evaluation, and promotion contracts; identifies marketplace approval and credential handling as human gates; and gives exact API, schema, preview, security, and rollback checks.

---

Built on SIP — Starlight Intelligence Protocol
Vertical: starlight-agent-skills · portable capability layer
