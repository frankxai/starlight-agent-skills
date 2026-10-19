---
name: queen-operator
description: "How to operate a Starlight Queen session: write the Brief before any dispatch, keep maker and checker apart, credit work only from a re-run receipt, and record one signed receipt per dispatch. Use when running or reviewing a multi-agent session, when a task is about to be handed to another agent, or when deciding whether a swarm's output counts as done. Portable and brand-neutral. Trigger phrases: run the queen, brief the swarm, who verifies this, is this task credited, dispatch receipt, maker checker, arm a queen session, queen operator."
metadata: {"version": "0.1.0", "domain": "substrate", "type": "substrate"}
---

# queen-operator

`swarm-queen-coordination` says who decides. This skill says how the Queen runs a
session so that what she dispatches is bounded, what comes back is verified, and
what she records can be checked by someone who was not there. Four rules, each
with a file shape and a gate.

## The four rules

| Rule | In one line | Gate |
|---|---|---|
| **Brief or refuse** | Nothing is handed to another agent without a complete Brief. A gap is a refusal, not a default. | task creation |
| **Maker ≠ Checker** | The actor who credits the work is not the actor who did it: different id, and a different model when both are models. | task creation and completion |
| **A receipt is a claim** | A worker saying "done" credits nothing. Credit comes from checks the verifier re-runs: exact command strings from an allowlist, evidence re-digested, a commit named for code. | task completion |
| **One receipt per dispatch** | Every dispatch ends in a signed receipt that names the model that actually ran, whether it was a fallback, what it cost, who decided at each gate, and what evidence remains. | the ledger |

Human-gated actions (moving funds, bulk sends, key rotation, force-pushing a
protected branch, switching to emergency governance) are prepared by agents and
committed by a person. The Queen's personality never widens her permissions.

## The Brief

```json
{
  "schema": "starlight.queen-brief.v1",
  "id": "task-12",
  "objective": "One sentence: what done looks like, not how to get there.",
  "acceptance": ["Checkable statements the verifier re-runs."],
  "output": { "format": "markdown", "maxBytes": 20000 },
  "tools": ["Read", "Grep"],
  "boundaries": ["What the maker must not do. At least one line."],
  "budget": { "microUsd": 2000000, "wallTimeMs": 600000 },
  "maker": { "id": "teammate:hermes", "model": "gemini-2.5-flash" },
  "verifier": { "id": "teammate:sentinel", "model": "claude-opus-4-6" },
  "allowedChecks": ["npm test"]
}
```

`allowedChecks` are exact strings: no globs, no shell metacharacters. An empty
list is allowed and means nothing can be credited by re-run, so the task cannot
complete. Budgets are integer micro-USD and milliseconds; no doubt about cents.

## Running a session

1. **Arm.** A Queen session is armed, not assumed. Where the `queen-ops` hooks
   are installed, `.starlight/queen/active.json` turns the gates on.
2. **Brief first.** One Brief per task, written before the task exists. Pick the
   maker for the work and a verifier that is independent of it.
3. **Dispatch inside the Brief.** Makers hold the tool allowlist and boundaries.
   Routing is reported, never silent: council-tier and high-risk lanes refuse
   rather than fall back to a weaker model.
4. **Verify, do not trust.** The verifier re-runs the allowed checks, re-digests
   the evidence, and writes the verify receipt. The taste reviewer applies the
   repo's taste contract and writes the taste receipt.
5. **Credit and record.** The task completes only from those two receipts. One
   signed dispatch receipt (`starlight.run-receipt.v1`) goes to the ledger.
6. **Stop on purpose.** At the budget ceiling, stand down with a note that names
   what was credited and what was not. An unfinished swarm is visible, never
   silent.

## What the receipts say

- **Verify receipt**: `credited`, `reruns[]` (command, exitCode), `verifier`,
  `evidence[]` (ref, sha256). Issued by the Brief's verifier, nobody else.
- **Taste receipt**: `verdict` (pass or ship), `pack` (which contract), `reviewer`.
- **Dispatch receipt**: DSSE-signed `starlight.run-receipt.v1`; first stage is
  the route (`usedModel`, fallback flag, reason). PASS is refused without evidence.

## Compose

- `swarm-queen-coordination` — the escalation contract this skill operates inside.
- `payments-mandate` — the money gate; audit entry first, then mandate and cap.
- `queen-ops` (claude-skills-library) — the hooks that enforce these rules on a
  developer machine; `@starlight-intelligence/queen` (starlight-swarm) — the
  kernel with `briefProblems()`, `verifyClaim()` and the receipt issuer.

## How SIS consumes this

The Starlight Intelligence System runs the Queen as its coordinator seat with
Domain Generals under her. Its mission shape is a strict subset of the Brief,
its review receipts and run receipts are the two receipt formats named here, and
its independent-review policy is the Maker ≠ Checker rule. The private runtime
holds dispatch authority; this skill describes the operator's discipline, not a
scheduler.

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
