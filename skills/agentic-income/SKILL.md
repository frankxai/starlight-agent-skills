---
name: agentic-income
description: The substrate operating brain for building income systems with AI agents. Use when planning, building, or scaling an affiliate/content/product income network — deciding what to build next, where money actually comes from, how to make it compound, and how the system improves itself. Portable and brand-neutral. Composes affiliate-audit. Trigger phrases: build an income system, make money with agents, scale my content network, what should I build next, passive income with AI, monetize this site, agentic income.
type: agent-orchestration
---

# agentic-income

The brain that turns "make money with AI agents" into a system that scales itself.
One thesis, five principles, four loops. Everything else is execution.

This is the **substrate-level, brand-neutral** version of the operating brain. It carries no
product names of its own — wire it to whatever sites, catalog, and rails your operator owns.

## The thesis

**Honest tool-comparison content is the most scalable, lowest-cost income engine an AI agent can run.**
The frontier tools that drive enormous search volume (the foundation-model and generative leaders)
typically pay nothing. So rank for them, tell the genuine truth, and route to the **adjacent tools
that pay recurring** — the ones the operator actually uses. The reader gets the real answer; the
system earns when they act on it. **Trust is the asset; the link is downstream.**

## The five principles (non-negotiable)

1. **Honest pick always wins.** Recommend what's genuinely best, then link the payer you'd actually buy. A link that overrides the truth burns the only asset that compounds: trust.
2. **Recurring > one-time.** Passive income compounds on subscriptions, not flat bounties. Build around recurring-payers; treat one-time bounties as bonus.
3. **Own the audience.** Every reader is income *or* a future relationship. One email capture per page turns rented traffic (SEO/social) into an owned list you control.
4. **Build the engine once, fork the sites.** One shared catalog + one template; each new site is a config swap. The second site is near-zero marginal cost. Effort goes into the substrate, not the Nth instance.
5. **Compounding over spikes.** Content that ranks for years + recurring commissions + a growing list = income that runs without you. Optimize for the asset that's still earning in 12 months, not the post that spikes today.

## The architecture (hub-and-spoke)

```
income engine (catalog + audit + this brain)   ← the OSS lead-gen substrate
   │
   ├─► hub site            ← the authority brand. Spokes link up to it.
   ├─► spoke site A        ← a distinct search audience / angle
   └─► spoke site B        ← another angle, near-zero overlap
```

One engine, N brands, N search audiences, near-zero overlap. Cross-link spokes→hub for topical
authority + referral flow. If one wins, double down; the losers cost almost nothing.

## The four loops (this is what "agents that learn" means)

The system improves itself because each loop feeds the next. An agent runs these on a cadence —
no human strategy meeting required.

**1. Monetization loop** (weekly): `affiliate-audit` joins the catalog × every site's content × traffic → ranks (a) which programs to join next, (b) which existing posts mention a payer with no link. Join → set the program's link in the catalog → sync → links go live network-wide → re-audit, gap clears.

**2. Content loop** (weekly): pull each site's top-traffic + highest-intent queries → a ranked backlog scores the next post by *opportunity = authority × intent × monetization × low-competition*. Build the top one in the citable shape. The winners tell you what to write next.

**3. Authority loop** (continuous): the OSS engine + public playbook earn stars and inbound links → that authority lifts the sites that consume the engine → more traffic → more audit signal. Giving the method away *is* the distribution.

**4. Learning loop** (monthly): every published post is a labeled example — query × shape × conversion. Feed outcomes back: which hooks/tables/answer-boxes converted, which programs actually paid. Bias the next batch toward what worked. The catalog `status` + the backlog ranking are the memory.

## What to build next (the decision)

When asked "what should I build/do next," rank candidate actions by leverage:

1. **Set a program link** for a tool already mentioned in a high-traffic post → instant revenue on existing traffic. (Run `affiliate-audit` to find these.) Highest ROI, do first.
2. **Write the top backlog post** for the site with the most authority in that cluster.
3. **Fork a spoke** only once the hub has ≥1 ranking post proving the shape works. Don't scale an unproven template.
4. **Join the next recurring-payer** the audit flags as high-mention/no-link.

Never: chase a one-time bounty over a recurring one, link a tool you haven't used, or build site N+1 while site N has un-linked payer mentions.

## The honest shape (every post)

Direct **answer box** up top (what AI search lifts) → **sortable comparison table** (the conversion
surface; renders a CTA only when a program link is set) → the genuine recommendation in prose →
real **FAQ** with FAQPage JSON-LD → one **affiliate disclosure**. Recommend, don't sell. The shape
ranks *and* converts.

## Compose

- `affiliate-audit` — the monetization-loop engine (catalog × content × traffic → gaps). This brain decides *what to do*; affiliate-audit *finds where the money is*.
- `payments-mandate` — when income flows past affiliate links into actual settlement, hand the money step to the payments skill. This brain never moves money itself.

## Guardrails

- One disclosure per page with links (FTC + trust).
- Catalog `status` flags dead-ends (frontier tools with no program) and closed programs — ignore them.
- Re-verify affiliate terms before relying on them; they change often.
- Null program link → plain text, never a dead link.
- This skill plans and routes. It never settles money — that is the payments skill's gated job, behind a human.

## How SIS consumes this

The Starlight Intelligence System loads this as the operating brain behind its **Wealth IS** income
thesis. A stream queen (see `swarm-queen-coordination`) runs the four loops on a cadence; the founder
agent owns capital allocation and the gate ladder. Outputs are SIP-attested.
