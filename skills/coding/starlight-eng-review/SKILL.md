---
name: starlight-eng-review
description: "Stress-test a technical design across data integrity, trust boundaries, concurrency, failure recovery, compatibility, observability, and resource limits. Use before implementing or landing a change whose failure could corrupt state, expose data, break clients, or create operational toil."
metadata: {"version": "0.1.0", "domain": "coding", "tags": ["engineering", "architecture", "security", "reliability", "failure-modes"]}
---

# Starlight Engineering Review

## Purpose

Find architectural failure modes while the design is still cheap to change.

## When it fires

- A change crosses process, network, repository, runtime, database, or trust boundaries.
- It changes schemas, migrations, authentication, permissions, money, or irreversible state.
- Reliability, scale, or backward compatibility is material.

## Inputs

- Architecture and data-flow diagrams or equivalent source evidence.
- State model, API/schema contracts, dependencies, and deployment topology.
- Expected load, failure history, privacy classification, and recovery objectives.

## Workflow

1. Map inputs, state, side effects, trust boundaries, and owners.
2. Check invariants, validation, idempotency, atomicity, and concurrency behavior.
3. Walk failures: timeout, retry, duplicate, partial success, stale state, quota, crash, and dependency drift.
4. Review authentication, authorization, secret handling, data minimization, and abuse controls.
5. Check compatibility, migrations, rollback, and version negotiation.
6. Define observability and tests that falsify the design’s critical assumptions.
7. Classify findings by severity and block landing on unresolved critical risks.

## Output contract

Return verdict, architecture summary, invariants, trust boundaries, failure table, compatibility/migration findings, resource analysis, required tests, rollback, and residual risks with owners.

## Tools & MCP

Inspect actual source, schemas, dependency versions, CI, and deployment configuration. Prefer primary documentation for current protocols. Never paste secrets into the report.

## Quality bar

- Every blocking finding cites a concrete boundary or contract.
- Distributed and serverless limitations are not hidden by in-process assumptions.
- Retries and rollbacks are safe, bounded, and testable.
- “Scalable” and “secure” are replaced by explicit mechanisms and limits.

## Example

Input: “Expose a stateless MCP endpoint.”

Good output: review origin enforcement, content limits, version negotiation, request validation, rate-limit topology, serverless state limits, tool authority, cache behavior, and reproducible protocol fixtures.

---

Built on SIP — Starlight Intelligence Protocol
Vertical: starlight-agent-skills · portable capability layer
