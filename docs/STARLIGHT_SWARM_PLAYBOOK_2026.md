# Starlight evidence-gated agent engineering playbook

Status: working operating contract, 2026 edition.

This playbook describes how a small human team can coordinate capable agents without pretending that model output is self-verifying or that automation removes operational ownership.

## Operating thesis

Agent leverage is highest when judgment, authority, state, and evidence are explicit:

- Humans own purpose, irreversible decisions, credentials, budgets, publication, and promotion.
- Agents may inspect, propose, implement, and verify within the authority granted for the task.
- Repository instructions, product truth, and signed or versioned artifacts outrank conversational memory.
- A result is not promoted because it looks complete; it is promoted because the required gates passed on the exact revision.

## The lifecycle

| Stage | Core question | Exit evidence |
|---|---|---|
| Intake | What user outcome and decision are actually in scope? | Outcome, owner, constraints, non-goals |
| Specification | What contracts must remain true? | Testable spec, trust boundaries, human gates |
| Plan review | Is this the right mechanism and sequence? | Reconciled product, engineering, design, and DevEx findings |
| Implementation | What is the smallest coherent change? | Scoped diff, migration and rollback where needed |
| Verification | Does the supported journey work? | Tests, semantic/visual QA, security and preview receipts |
| Review | What did the maker miss? | Independent review or disclosed sequential self-review |
| Landing | May this exact revision merge? | Required checks, clean merge state, release notes |
| Production | Did the promoted revision remain healthy? | Live URL, runtime checks, rollback revision, monitoring |
| Learning | What should change next time? | Evidence draft, exceptions, owner-approved lesson |

## The portable coding skill set

| Skill | Responsibility |
|---|---|
| starlight-spec | Convert approved intent into contracts, tasks, gates, and rollback |
| starlight-autoplan | Reconcile product, engineering, design, and DevEx review lenses |
| starlight-ceo-review | Test user value, strategy, economics, sequencing, and ownership |
| starlight-eng-review | Stress-test data, trust, failure, compatibility, and operations |
| starlight-design-review | Audit hierarchy, system coherence, accessibility, states, and responsive craft |
| starlight-devex-review | Audit install, API/CLI ergonomics, errors, versions, removal, and support |
| starlight-investigate | Diagnose root cause with falsifiable evidence |
| starlight-qa | Exercise real journeys and document tested and untested boundaries |
| starlight-ship | Govern Git, reviews, previews, merge, production, and rollback |

These are composable capabilities, not permanent job titles. Use only the review depth warranted by impact and reversibility.

## Review topology

For high-risk work, separate the maker and verifier when machine capacity and task tooling allow it. Give the verifier the outcome, diff, repository rules, and test evidence, but not a request to confirm the maker’s conclusion.

When independent execution is unavailable:

1. Freeze the candidate revision.
2. Re-read the diff from the reviewer perspective.
3. Run adversarial fixtures and negative-path checks.
4. Disclose that the review was sequential self-review.
5. Keep unresolved high-risk findings as blockers.

Consensus is not proof. A review report must cite code, commands, protocol text, or observed runtime behavior.

## Runtime portability

The canonical skill instructions live in SKILL.md. Runtime adapters define discovery and installation, not a rewritten behavior contract.

Use the best native path available for each host:

- native plugin or skill package when the host supports it;
- reviewed marketplace submission when approval is required;
- a staged profile or adapter when native publication is unavailable;
- MCP for bounded tool access;
- a documented local copy only when no package mechanism exists.

Never market every host as one-click. Authentication, OAuth, admin consent, marketplace review, filesystem permissions, and restart behavior must remain visible and independently verified.

## Authority and side effects

Classify each action before execution:

| Class | Examples | Default |
|---|---|---|
| Read-only | Search, inspect, fetch logs, compare revisions | Agent may proceed in scope |
| Reversible local | Edit a scoped branch, create a preview | Agent may proceed when implementation is requested |
| External reversible | Open/update a PR, send a task message | Require task-level authority and leave a receipt |
| Costly or public | Purchase, publish, production promote, message customers | Human gate unless explicitly authorized |
| Destructive or hard to recover | Delete data, rewrite shared history, rotate live credentials | Resolve exact target and authority first |

## Git and deployment discipline

1. Verify path, repository root, origin, and branch before the first write.
2. Preserve unrelated user changes and active worktrees.
3. Use focused commits and non-interactive Git.
4. Run repository-required tests, secret scans, and diff checks.
5. Prefer a Vercel or equivalent preview when the project is already connected.
6. Review the exact head revision; a later push invalidates earlier evidence.
7. Merge only when required checks and governance pass.
8. Verify the live route after promotion and retain the rollback revision.

## Academy and evidence

Learning material should culminate in work, not passive completion:

- a real decision and bounded source packet;
- a worked example with a rubric;
- a guided lab and an own-work mission;
- artifact references rather than copied secrets;
- evaluation that separates observation, inference, and decision;
- a transfer task under changed constraints;
- a non-canonical evidence draft awaiting separate review.

A generated draft is not a credential, certification, authorization, or proof that the underlying work occurred.

## Claim discipline

Do not claim:

- that AI execution is free;
- equivalence to an unmeasured human team;
- universal runtime compatibility;
- full security, scalability, or test coverage without evidence;
- partner, marketplace, or production approval before it exists.

State the exact revision, environment, test scope, verification date, and untested boundaries instead.

---

Built on SIP — Starlight Intelligence Protocol
