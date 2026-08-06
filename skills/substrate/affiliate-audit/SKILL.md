---
name: affiliate-audit
description: Map which content mentions paying tools but lacks affiliate links, and which programs to join first. Use when monetizing tool-comparison content, choosing affiliate programs, or auditing a passive-income site's link coverage. Portable and brand-neutral. Trigger phrases: affiliate audit, affiliate link, affiliate program, monetization gap, link coverage, which programs to join, missing affiliate links, audit my content, program catalog.
type: agent-orchestration
version: 0.1.0
domain: substrate
---

# affiliate-audit

Connect the affiliate catalog to a site's content and surface monetization gaps.
The monetization loop's engine: **catalog × content × traffic → ranked gaps.**

## Run

```bash
node scripts/affiliate-audit.mjs --content=<site>/content --traffic=<traffic.json> --write
```

Reads the program catalog (`data/programs.json` or operator equivalent, expecting fields like `status` and `disclosure`) + the content dir +
optional traffic → ranks (1) programs to join first, (2) posts to add links to. Writes `AUDIT.md`.

If no runtime is wired, the audit can also be run as a reasoning pass: read the catalog, scan the
content for tool mentions, cross-reference against which mentions carry a live program link, and
rank the gaps by traffic × payer value.

## Strategy rules (apply when recommending or placing links)

1. **Frontier names rank, adjacents pay.** The largest foundation-model and generative leaders usually have NO affiliate program. Capture their traffic; monetize via the recurring payers the post recommends.
2. **Highest-ticket recurring tool the operator actually uses, first.** Then the recurring spine of subscription payers. Authenticity beats commission rate.
3. **Recurring > one-time.** Passive income compounds on subscriptions, not flat bounties.
4. **One disclosure per page.** FTC + trust. Use the catalog's `disclosure` string.
5. **Never link a tool you can't vouch for**, and never let a link override the honest pick — say what's actually best, then point to the payer you'd actually buy.
6. **Ignore dead-ends/closed** (`status` in the catalog): frontier tools with no program, programs closed to new affiliates, deprecated tools.

## The loop

Audit → join top program → set the program link in the catalog → add link + disclosure to the
named posts → re-audit (gap clears).

## Compose

- `agentic-income` — the operating brain that decides *what to do* with the gaps this audit surfaces.

## How SIS consumes this

The Affiliate stream queen runs this on the weekly monetization-loop cadence. The audit produces
recommendations only; placing links and joining programs runs through the queen's gate, and any
revenue that flows downstream into settlement is handled by `payments-mandate`, never here.

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
