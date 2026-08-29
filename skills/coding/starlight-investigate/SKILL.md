---
name: starlight-investigate
description: "Diagnose a reproducible software failure by separating observations from hypotheses, locating the failing boundary, and defining regression evidence. Use when a bug, failed check, production incident, or unexpected behavior needs a root-cause report; modify code only when the user also authorizes a fix."
metadata: {"version":"0.1.0","domain":"coding","tags":"diagnosis,debugging,root-cause,evidence,regression"}
---

# Starlight Investigate

## Purpose

Find the smallest evidence-supported explanation for a failure without speculative edits or unrelated cleanup.

## When it fires

- A test, build, deployment, API, UI flow, or runtime behavior fails.
- The failure is intermittent and needs boundary isolation.
- The user asks for diagnosis, root cause, or incident analysis.

## Inputs

- Expected and observed behavior.
- Reproduction steps, logs, timestamps, environment, and relevant revision.
- Repository instructions and known constraints.

## Workflow

1. Capture the exact failure and determine whether it reproduces.
2. Reduce it to the smallest safe reproduction while preserving the failing condition.
3. Trace inputs, state transitions, and outputs across the suspected boundary.
4. List competing hypotheses and the observation that would falsify each one.
5. Run the cheapest discriminating checks first.
6. State the root cause only when evidence rules out plausible alternatives.
7. If a fix is authorized, apply the smallest causal change and run focused plus regression checks.
8. Record residual uncertainty, monitoring, and rollback needs.

## Output contract

Return:

- `symptom` and reproducibility;
- `evidence` with commands, locations, and relevant revisions;
- `hypotheses_tested` and falsification results;
- `root_cause` or `not_yet_proven`;
- `impact_boundary`;
- `recommended_fix` without implementation when diagnosis-only;
- `verification` and `residual_risk`.

## Tools & MCP

Prefer repository search, focused tests, logs, and read-only platform inspection. Redact credentials and personal data. Do not alter production state to make a diagnosis easier.

## Quality bar

- Observation, inference, and decision are clearly separated.
- “Could be” is not presented as root cause.
- The reproduction and verification are copyable.
- The proposed fix addresses the causal boundary rather than masking the symptom.
- Unrelated working-tree changes remain untouched.

## Example

Input: “The preview works, but the production API returns 415.”

Good output: evidence showing the exact content-type mismatch at the request boundary, alternatives ruled out, a minimal header-validation fix, and focused plus production-preview checks.

---

Built on SIP — Starlight Intelligence Protocol
Vertical: starlight-agent-skills · portable capability layer
