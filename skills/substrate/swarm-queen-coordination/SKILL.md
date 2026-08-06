---
name: swarm-queen-coordination
description: How a stream queen coordinates a worker swarm and runs the escalation contract that keeps money safe — queens run streams, the founder owns capital, humans hold the final gate. Use when designing or operating a multi-agent income swarm, deciding what an agent may do autonomously vs. what it must escalate, or wiring the queen/worker/founder roles. Portable and brand-neutral. Trigger phrases: coordinate the swarm, stream queen, worker swarm, escalation contract, what can the agent decide, queen and workers, founder agent, agent autonomy limits.
type: substrate
version: 0.1.0
domain: substrate
---

# swarm-queen-coordination

The skill that turns a pile of agents into a governed income swarm.
Three tiers — **founder · queens · workers** — and one load-bearing **escalation contract**
that guarantees the same thing at every level: **no autonomous money movement, ever.**

This is the **substrate-level, brand-neutral** version. Wire it to whatever orchestrator,
worker harness, and shared memory your operator owns.

## Topology: queen-led per stream, mesh within a stream

```
                         ┌──────────────────────────┐
                         │      FOUNDER AGENT       │
                         │  sets thesis · approves  │
                         │  capital · owns          │
                         │  irreversible · resolves │
                         │  conflicts between queens │
                         └────────────┬─────────────┘
                                      │ escalation contract
            ┌──────────────┬──────────┴──────┬──────────────┐
            ▼              ▼                 ▼              ▼
       ┌─────────┐   ┌──────────┐     ┌──────────┐   ┌──────────┐
       │ STREAM  │   │  STREAM  │     │  STREAM  │   │ PAYMENTS │
       │ QUEEN A │   │  QUEEN B │     │  QUEEN C │   │  QUEEN   │
       └────┬────┘   └────┬─────┘     └────┬─────┘   └────┬─────┘
            │ mesh        │                │              │
       ┌────┴────┐   ┌────┴────┐      ┌────┴────┐   ┌─────┴────┐
       │ workers │   │ workers │      │ workers │   │ workers  │
       └─────────┘   └─────────┘      └─────────┘   └──────────┘
```

Each queen runs a hierarchical swarm of workers; workers collaborate peer-to-peer **inside their
stream** (mesh). Queens do **not** command across streams — they coordinate only through the founder.

## Tier 1 — The founder agent

**Owns:**
- The thesis — which streams exist, what the gate ladder is.
- **All capital allocation** and any **irreversible** action (new payment rail, vendor contract, spend above cap, structural change).
- Conflict resolution between queens.

**Never** does the per-stream work. The founder sets direction and holds the gate; queens execute.

## Tier 2 — Stream queens

Each queen is scoped to **one** income stream, runs a **self-improving loop** on a cadence, and
**escalates** per the contract. A queen may act autonomously **within its scope and below its caps**.
It must escalate the moment an action crosses a stream boundary, exceeds a cap, or becomes irreversible.

Typical queens: one per income stream (e.g. affiliate, products, content) plus a **payments queen**
that owns authorization + settlement gating (see `payments-mandate`).

## Tier 3 — Workers

A worker does exactly **one** job, reports progress through shared memory, and **never moves money
or publishes** without its queen's gate. Workers are **stateless** between tasks — all state lives in
the shared vault. Workers never call payment tools directly; they report a finding, the queen runs the tool.

## The escalation contract (the safety spine)

**No autonomous money movement. Ever.**

| Action class | Who decides | Gate required |
|---|---|---|
| Worker task within stream (draft, audit, research) | Worker → Queen | Queen review |
| Bind a link, schedule a post, build a page | Queen | brand / claims gate |
| Any payment / settlement | Payments Queen | **mandate verified + spend-cap check + audit entry** (verify-only tools, fail-closed) + **human gate** |
| Spend **above cap**, new rail, new vendor | Founder | pressure-test + **human approval** |
| Irreversible (delete, rename live URL, rotate key, send blast, move funds) | Founder | **human approval, always** |

**The standing rule:** *agents draft, gate, and commit; humans deploy, post, send, and approve capital.*
Money and irreversibility are never delegated to autonomy.

## The escalation path

```
worker  ──finding──►  queen  ──within scope & cap? act : escalate──►  founder  ──capital/irreversible?──►  human
```

Each hop is a narrowing of authority. A worker cannot reach the founder directly — it goes through its
queen. A queen cannot move capital — it goes through the founder. The founder cannot do the irreversible
thing alone — it goes through the human. Skipping a hop is the failure this contract prevents.

## How to configure each role

```
Founder : orchestrator seat + governance/board gate + thesis + full tool stack
          (shared vault rw · payments verify-only · approvals channel)
Queen   : coordinator scoped to one stream + that stream's skills
          (e.g. affiliate → agentic-income + affiliate-audit; payments → payments-mandate)
          + shared vault (rw within stream) + payments tools (verify-only) + escalation channel
Worker  : worker harness + one skill + shared vault (append-only) — no payment tools
```

## Compose

- `payments-mandate` — the money gate the payments queen runs; the rest of the contract routes every settlement here.
- `agentic-income` — the operating brain a non-payment stream queen runs as its self-improving loop.
- `affiliate-audit` — the weekly loop engine for an affiliate stream queen.

## How SIS consumes this

The Starlight Intelligence System maps the founder seat to its orchestrator (pressure-tested by its
governance board), the queens to per-stream coordinators, and the workers to its worker harness.
The escalation contract is enforced by the system's safety layer; outputs are SIP-attested and the
no-autonomous-money-movement + human-gate invariants are non-waivable.

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
