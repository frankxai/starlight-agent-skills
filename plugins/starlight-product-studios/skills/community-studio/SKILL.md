---
name: community-studio
description: "Build a working community or academy from one curriculum contract: a named operator, a dated cadence, lessons as code, member-owned receipts, a room such as Circle, and read-only operating agents. Use when a brand or buyer needs a cohort, community, academy or learning lab that members can join and finish, with proof of what they made."
metadata: {"version":"0.1.0","domain":"studios","tags":"community,academy,cohort,curriculum,circle,receipts,agents"}
---

# Community Studio

## Purpose

Turn a community idea into a room people can join on day one and leave four weeks later with work they made and receipts that prove it. One curriculum contract feeds every surface; the operator stays human.

## When it fires

- A brand wants a cohort, lab, academy, membership community or learning path.
- An existing community has spaces but no members finishing anything.
- A buyer wants a done-for-you community built in their own tenant.

## Inputs

- Product manifest and exact source revision of `frankxai/starlight-community-builder` (contract schemas, validator, agent definitions).
- Community Studio task envelope: buyer job, named operator, dated cadence, room choice, segment, token ceiling, acceptance and stop conditions.
- Rights record for every lesson source, and the brand's design pack.

## Workflow

1. Resolve the product, repository, Community Studio pack and room adapter from reviewed Registry state. Stop if no named operator, dated cadence or demand capture exists (estate AGENTS.md §12).
2. Pick one segment. Write the member's job, the first result they can reach in one session, and the four-week arc.
3. Write lessons as code against `lesson.schema.json`; run `node --test` and the validator on every lesson. One lesson id is used in the room, the app and the MCP tool.
4. Plan the room: keep about 15 visible spaces, hide paths that are not open, and gate private spaces by entitlement, never by interest tag.
5. Stage the operating agents from the kit (Concierge, Curator) with read-only room tools. Run runbook phase 1 on invented fixtures; record cost.
6. Walk the path with a fresh account on desktop and at 390 px: invite, onboarding, first lesson, first receipt. Record every confusing word and dead link.
7. Hand the release decision to the operator: publication, invites, prices and access grants stay human.
8. After the cohort, report activation (first passing receipt), retention (passing receipts in two weeks), help load and interview quotes, and feed them back into the curriculum.

## Output contract

Return contract-valid lessons, a space plan, staged agents with fixture results, fresh-member walkthrough evidence, cohort measures and an exact-revision release receipt.

## Tools and MCP

Use GitHub for the curriculum and contract; Circle MCP read tools for room state; Claude Managed Agents for staged operating agents; Polar for entitlements once a paid path passes its gate; browser verification for the member walkthrough.

## Quality bar

- A new member reaches a passing receipt in one session without help.
- Member records carry no email, name or payment data; receipts are exportable by the member.
- Agents never write to the room without an approved runbook phase.
- Every claim in member copy is true on the day it is published.
- Publication, invites, pricing and access remain separate human-authorized gates.

---

Built on SIP — Starlight Intelligence Protocol
Vertical: federated-product-studios · portable capability layer
