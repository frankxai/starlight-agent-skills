---
name: payments-mandate
description: How an agent safely handles a payment mandate — verify authorization before any settlement, hold the spend cap, fail closed on doubt, and keep a human on every money decision. Use when an agent is asked to authorize, settle, charge, or release funds, or when wiring a payments step into an income system. Portable and brand-neutral. Trigger phrases: handle a payment, authorize a charge, verify a mandate, settle money, AP2 mandate, spend cap, can the agent pay, autonomous payment.
type: substrate
---

# payments-mandate

The skill that lets an agent touch money **without ever moving it autonomously.**
You answer two questions — *was this authorized?* and *is it within cap?* — **before**
any settlement rail runs. You produce verdicts and pending-approval objects, never transfers.

This is the **substrate-level, brand-neutral** payments skill. Wire it to whatever
mandate issuer, cap config, and settlement rail your operator owns.

## The one rule above all

**No autonomous money movement. Ever.** There is no `transfer` / `pay` / `settle` /
`move_funds` step in this skill — none exists, by design. The skill owns *authorization*
and *cap enforcement*; the settlement rail (run elsewhere, behind a human) reads the verdict
as a precondition and never bypasses it.

```
AP2 mandate ("was this authorized?")  ──verified──►  spend-cap check  ──within cap──►  settlement runs (elsewhere, gated)
     │                                       │
  reject on doubt                       over cap → escalate to human
```

## What AP2 is (and is not)

AP2 (Agent Payments Protocol, the Google-originated open standard) uses **signed mandates**
to prove that a human authorized a specific charge. The mandate is the proof of authorization.

- AP2 **proves authorization**. It does **not** move money — settlement is a separate rail
  (e.g. an onchain rail or a shared-payment-token rail) that runs only after a mandate verifies.
- A verified mandate is a green light to *proceed to the cap check*, not a green light to spend.
- Verify the mandate **before** any settlement. Settlement that runs ahead of verification is
  the failure mode this skill exists to prevent.

> Implementation note: a real deployment swaps in production AP2 cryptographic verification
> behind the verify step. Until that is wired and audited, do not point this at live funds.

## Verify a mandate (first failure rejects, in order)

1. **Signed?** No signature, or signature does not verify against the issuer key → **REJECT**.
2. **Unexpired?** No expiry, or expiry ≤ now → **REJECT**. A *missing* expiry is a reject, not a pass.
3. **Amount-matched?** Charge amount ≠ mandate amount, or currency mismatch → **REJECT**.
4. **Well-formed?** Missing mandate id / subject, or malformed payload → **REJECT**.

Only a mandate that clears all four is `verified`. Everything else rejects with a one-line reason.

## Hold the spend cap (after a mandate verifies)

Three caps — all must pass:

- **per-transaction** — this charge alone ≤ the per-tx ceiling.
- **per-day** — this charge + today's already-approved spend on this stream ≤ the daily ceiling.
- **per-stream** — this charge + the stream's running total ≤ the stream ceiling.

Plus a **replay guard:** a mandate is **single-use**. If its id was already consumed → **REJECT** (replay).

**Over any cap → ESCALATE to a human. Never auto-approve an over-cap spend.** Escalation returns
a pending-approval object; a human resolves it.

## Fail closed (the load-bearing rule)

When uncertain, **reject** — never pass. "Reject on doubt" beats "approve and apologize":
a false reject costs a retry; a false approve costs money that does not come back.

| Situation | Action |
|---|---|
| Unsigned / invalid / unverifiable mandate | REJECT |
| Expired or no-expiry mandate | REJECT |
| Amount or currency mismatch | REJECT |
| Replayed (already-consumed) mandate | REJECT |
| Over any cap | **ESCALATE** — never auto-approve |
| Audit-log write fails | **FAIL the action** — no money action without a prior audit entry |
| Anything malformed or ambiguous | REJECT and surface to the operator |

## Audit before action

Every money-relevant decision writes to an **append-only** log *first*. No money action exists
without a prior audit entry. If the audit write fails, the whole action fails. Never edit or
delete a log entry.

## Reject vs. escalate (do not collapse them)

- **REJECT** = the request is *invalid* (forged/expired mandate, replay, malformed). Caller fixes and retries.
- **ESCALATE** = the request is *valid but exceeds autonomy* (over cap, new rail, new vendor). A human decides.

A forged mandate is rejected, not escalated. An over-cap spend is escalated, not rejected.

## Refuse outright

Refuse and surface to the operator — do not work around — when asked to: move/transfer/settle/release
funds; raise a cap, skip verification, or approve an own over-cap spend; (as a worker) call the
payments tools directly; or route toward confidential financial data. Guessing on money is forbidden.

## Compose

- `swarm-queen-coordination` — in a swarm, only the payments **queen** runs the verify/cap/audit
  tools; workers report findings, the queen renders the verdict, the founder owns caps and rails.
- `agentic-income` — the income brain routes the *money step* of any stream to this skill; it never settles money itself.

## How SIS consumes this

The Starlight Intelligence System loads this behind its **Payments** stream. The Payments queen
calls verify-only tools (verify mandate / check cap / record audit / require human approval); the
founder agent owns cap raises, new rails, and any irreversible action under a human gate. Outputs
are SIP-attested; the fail-closed and human-gate invariants are non-waivable.
