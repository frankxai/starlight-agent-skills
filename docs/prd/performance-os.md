# PRD — Sovereign Performance OS (v0.1)
Status: proposal; no production integration asserted. Owner: Starlight Intelligence. Distribution: FrankX.

## Decision
Ship a portable, user-owned training telemetry skill and verified Google Workspace adapter before building a proprietary fitness app. Primary buyer: strength coaches using Google Sheets; first dogfood: one individual's workout ledger.

## Problem and outcomes
Capture exercise sets with voice or shorthand without interrupting training. Preserve source evidence and correction history. Deliver accurate weekly progression reports that coaches approve. Measure capture accuracy, sync integrity, time saved, 7/30-day retention, and paid pilot conversions.

## Personas
- Solo lifter: offline capture, instant corrections, export, no mandatory subscription.
- Independent coach: existing client Sheets remain usable; multi-client consent, review queue, weekly check-ins.
- Developer/adopter: documented schema, fixtures, portable skill, adapter interface and reproducible tests.

## Scope P0
1. Input: `OHP 40x12x4`, voice transcript, manually entered set; photo interpretation later.
2. Parse into proposed events with units, exercise ID, set count, reps, load, laterality, confidence, raw source, timestamps, timezone.
3. Explicit confirmation for ambiguous inputs; no invented reps, loads, or completion.
4. Append-only canonical event IDs, revisions, idempotency, audit trail; derive set-level rows deterministically.
5. Google Sheets adapter with initial import, outbound sync, conflict/reconciliation queue and user-controlled export.
6. Derived metrics: tonnage and estimated 1RM with calculation method; muscle-group exposure clearly marked as modeled estimates, not biological measurement.
7. Coach report as approval-required draft, never auto-send or auto-prescribe.
8. Consent, tenant isolation, least-privilege OAuth, deletion/export, encryption and retention controls.

## Out of scope P0
Clinical or injury diagnosis, endocrine optimization, automated medical advice, universal hypertrophy set targets, automatic calendar mutation, WhatsApp automation, 3D anatomical accuracy claims, live wearable integrations.

## Acceptance criteria
- >=95% correct structured capture on 30+ pre-registered representative examples; ambiguity is surfaced rather than silently guessed.
- No duplicate set events on replay; sync failures recover without data loss; every derived metric links to inputs and formula version.
- Coach can review and approve changes; no cross-tenant access in tests.
- One real end-to-end capture → persisted event → verified Sheet projection → correction → weekly report.
- Document setup, cost, portability, privacy and recovery paths.

## Data contract
`event_id, tenant_id, athlete_id, session_id, source_channel, source_ref, captured_at, performed_at, timezone, exercise_id, load_kg, reps, set_count, laterality, rpe, rir, tempo, status, confidence, schema_version, revision_of`.
Unknown is null; never zero. Store raw sensitive media only with opt-in and retention expiry. Derived rows carry `calculation_version` and provenance.

## Architecture
Input adapters → parser/validation → typed event ledger → deterministic analytics → Sheets/Calendar/Notion projections → optional PWA and coach cockpit. MCP exposes narrow authorized tools; it is not the data store. Sheets is a portable projection, not a second competing source of truth. Existing Starlight routing, identity, eval and evidence infrastructure should be reused after inspection.

## Rollout and commercial gates
P0: private dogfood and clean export. P1: three coach pilots; quantify hours saved and correction rate. P2: paid blueprint (€79 hypothesis) and coach subscription (€149–299/mo hypothesis) only after willingness-to-pay evidence. Avoid creating new infrastructure repositories until adapter boundaries and ownership are confirmed.

## Scientific integrity
Epley 1RM is an estimate. Tonnage and muscle exposure are proxies, not direct hypertrophy measures. Avoid fixed cold-plunge/mTOR timing mandates or GH/HSP claims as validated outcomes. Health-related recommendations require evidence review, uncertainty labels and human control.
