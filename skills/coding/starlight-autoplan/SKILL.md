---
name: starlight-autoplan
description: "Execute the Starlight 4-Stage Adversarial Plan Review Pipeline: CEO Strategy, Engineering Architecture, Design Taste, and Developer Experience. Enforces the Completeness Principle ('Boil the Lake') to produce hardened implementation specs."
version: 1.0.0
domain: coding
tags: [autoplan, review, architecture, ceo, engineering, design, devex, quality-gate]
---

# Starlight Autoplan — 4-Stage Adversarial Review Swarm

> Transform any rough implementation idea or technical plan into a battle-tested, 10/10 complete implementation specification through four specialized review gates.

## Purpose

The difference between a mediocre software release and a category-defining product is systematic pre-flight scrutiny. `starlight-autoplan` chains four independent reviewer perspectives:

1. **Gate 1: CEO / Founder Review** — Rethink the problem, find the 10-star product, challenge scarcity premises, enforce the Completeness Principle ("Boil the Lake").
2. **Gate 2: Engineering Architecture Review** — Stress-test data models, concurrency boundaries, edge cases, error recovery, and failure modes.
3. **Gate 3: Design & Taste Review** — Audit visual hierarchy, typography, responsive breakpoints, UX state transitions, and anti-slop compliance.
4. **Gate 4: Developer Experience (DevEx) Review** — Scrutinize API ergonomics, CLI flags, time-to-hello-world, and documentation clarity.

## When it fires

- Command triggers: `/starlight-autoplan`, `/autoplan`, `/plan-review`
- Context triggers: "review this plan", "stress test our architecture", "make this 10x better", "autoplan", "is this ready to build"

## The 4-Stage Review Protocol

```
                        ┌────────────────────────────────────────┐
                        │        INPUT IMPLEMENTATION PLAN       │
                        └──────────────────┬─────────────────────┘
                                           │
                        ┌──────────────────▼─────────────────────┐
                        │        GATE 1: CEO STRATEGY REVIEW     │
                        │ • 10-Star Experience • Boil the Lake   │
                        │ • Monetization & Value Alignment       │
                        └──────────────────┬─────────────────────┘
                                           │
                        ┌──────────────────▼─────────────────────┐
                        │       GATE 2: ENGINEERING ARCHITECTURE │
                        │ • Edge Cases • Concurrency • Failures  │
                        │ • Data Models & Security Perimeter     │
                        └──────────────────┬─────────────────────┘
                                           │
                        ┌──────────────────▼─────────────────────┐
                        │        GATE 3: DESIGN & TASTE REVIEW   │
                        │ • Impeccable UX • Typography Hierarchy │
                        │ • Anti-Slop Check • Micro-Interactions │
                        └──────────────────┬─────────────────────┘
                                           │
                        ┌──────────────────▼─────────────────────┐
                        │         GATE 4: DEVEX ERGONOMICS       │
                        │ • API Simplicity • Time-to-Hello-World │
                        │ • CLI Usability • Error Actionability  │
                        └──────────────────┬─────────────────────┘
                                           │
                        ┌──────────────────▼─────────────────────┐
                        │     ## STARLIGHT REVIEW REPORT         │
                        │ Consolidated Action Plan & Green Light │
                        └────────────────────────────────────────┘
```

### Stage 1: CEO / Founder Strategy Review
- **Completeness Principle:** AI makes marginal coding cost near-zero. Did we build the full lake (all edge cases, full test coverage, complete workflows), or did we take false shortcuts?
- **Ambition:** Is this the simplest version of a 10-star product, or merely a 3-star incremental patch?
- **BYOK / Business Alignment:** Does this preserve user sovereignty, require zero multi-tenant server liability, and create compounding enterprise value?

### Stage 2: Engineering & Architecture Review
- **Failure Modes:** What happens when networks drop, tokens expire, or rates are limited?
- **Data Integrity:** Are mutations atomic? Are state transitions idempotent?
- **Resource Constraints:** Does it respect RAM, connection limits, and token budgets?

### Stage 3: Design, Taste & UX Review
- **Anti-Slop Standard:** Zero unformatted divs, generic Tailwind gradients, or default system fonts.
- **Hierarchy:** Is the primary call-to-action unmistakable? Is secondary information progressively disclosed?
- **Feedback States:** Are loading, empty, success, and error states designed and handled?

### Stage 4: DevEx & Usability Review
- **Time to Hello World:** Can a new developer or user get value in under 60 seconds?
- **Error Clarity:** Every error message must tell the user or agent exactly how to resolve it.

## Output Contract

Every Autoplan run updates the implementation plan with a terminal review report:

```markdown
## STARLIGHT REVIEW REPORT

### 1. CEO Strategy Verdict
- **Completeness Score:** [X/10]
- **Key Expansions:** [What was added to make the product exceptional]

### 2. Engineering Architecture Verdict
- **Verdict:** [APPROVED | BLOCKED | APPROVED WITH CONCERNS]
- **Mitigated Risks:** [Edge cases and failure paths patched]

### 3. Design & Taste Verdict
- **Anti-Slop Compliance:** [PASSED]
- **UX Refinements:** [Hierarchy and responsive notes]

### 4. DevEx Usability Verdict
- **Time to First Action:** [<60s]
- **API/CLI Polish:** [Flag and syntax simplifications]

---
**FINAL ACTION PLAN:** [Step-by-step verified execution order]
```

---

Built on SIP — Starlight Intelligence Protocol  
Vertical: starlight-agent-skills · autonomous capability layer
