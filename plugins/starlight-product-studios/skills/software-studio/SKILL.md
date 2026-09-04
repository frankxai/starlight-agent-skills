---
name: software-studio
description: "Build and release secure applications, mobile products, games, plugins, MCP servers, agents, SDKs and platform modules with professional SDLC evidence. Use when a software product needs bounded architecture, implementation, adversarial review, exact-revision verification, deployment packaging or marketplace preparation."
metadata: {"version":"0.1.0","domain":"studios","tags":"software,apps,plugins,mcp,agents,platforms,security,sdlc"}
---

# Software Studio

## Purpose

Turn a product claim into a bounded, secure, observable and maintainable software release while preserving portable domain contracts and exact operational evidence.

## When it fires

- Building or materially changing an application, mobile app, game, plugin, MCP server, agent, SDK or platform module.
- Preparing a Vercel, Railway, Apple App Store, Google Play, itch.io or owned-product release.
- Repairing a failing, stale, unlinked or unverifiable software release.

## Inputs

- Product manifest, repository instructions, exact base revision and accepted architecture decisions.
- Software Studio task envelope with scope, non-goals, token/cost ceilings, permissions, target channels, acceptance, rollout and stop conditions.
- Threat context, data/identity/tool contracts, supported-version matrix and existing runtime evidence.

## Workflow

1. Resolve the canonical product repository, Software Studio pack, architecture decisions and channel adapters. Do not create another platform, service or repository from naming convenience.
2. Define the measurable user job, critical path, non-goals, interfaces, state, failure behavior, security boundary, telemetry and release evidence before implementation.
3. Assign product architecture, implementation, security/reliability review, product-quality review and exact-revision verification to non-overlapping owners.
4. Work on a reviewable branch. Preserve unrelated changes; keep secrets out of source; use reversible migrations, idempotency and explicit rollback.
5. Run format, lint, type, unit, integration, permission, retry, malformed-input, dependency, secret and migration gates proportional to risk.
6. Verify accessibility, responsive behavior, performance, compatibility, empty/loading/error/recovery paths, observability, model/runtime cost and support boundaries.
7. Build a preview or installable package from the exact revision. Compile requested store, template or integration packages using the registered adapters.
8. Record tests, independent review, preview/deployment, smoke evidence, known limitations, rollback and human-governed actions in the release receipt.

## Output contract

Return architecture decision, reviewable revision, test/security/quality evidence, preview or installable artifact, channel packages, SLO/cost/rollback record, exact-revision release receipt and release decision.

## Tools and MCP

Use GitHub for source, review and CI; Vercel for Next.js experiences and application-local jobs; Cloudflare for accepted persistent entity or edge boundaries; Supabase/Postgres for shared business truth; Linear for execution projection; and browser/runtime tools for observable smoke evidence. MCP is a typed boundary, not product authority.

## Quality bar

- Architecture, permissions, data ownership, failure modes and recovery are explicit.
- Required gates pass on the exact release revision.
- Preview, production and public availability are reported as different states.
- Operability, observability, cost, rollback, support and compatibility are owned.
- Merge, production promotion, store submission, pricing, spending and external contact follow their authorization gates.

---

Built on SIP — Starlight Intelligence Protocol
Vertical: federated-product-studios · portable capability layer
