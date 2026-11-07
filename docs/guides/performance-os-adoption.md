# Adopt Sovereign Performance OS — starter guide

**Status:** specification/template, not an installed integration.

## Bring your own storage
Start with a copy of your existing workout spreadsheet. Minimum tabs: `Workout Log`, `Exercise Dictionary`, `Derived Analytics`, `Sync & Corrections`. Never publish real client data or OAuth tokens. The reference workbook is private and must not be copied into public examples.

## Minimum workout row
`event_id | performed_at | exercise_id | set_index | weight_kg | reps | rpe | tempo | source | confidence | revision_of`

## Example
Input: `OHP 40x12x4`
Parsed proposal: overhead press, 40 kg, 12 reps, 4 sets; requires exercise mapping confirmation for a new user.
After approval: create four set events; tonnage = 40 × 12 × 4 = 1920 kg; Epley estimate for 12 reps = 56 kg, with limitations displayed.
Input: `LBR 60` → do **not** invent reps or sets. Request clarification or preserve incomplete event.

## Adapter contract
`parseCapture(input) -> ProposedEvent[]`
`confirmCapture(proposals, actor) -> CanonicalEvent[]`
`projectToSheet(events, cursor) -> SyncReceipt`
`reconcileSheetEdits(changes) -> Conflict[]`
`buildCoachDraft(athleteId, period) -> ApprovalRequiredDraft`
All write methods require authenticated actor, authorization, idempotency key and audit receipt.

## Adoption sequence
1. Clone/fork the skill library; select the future `performance-os` skill when implemented.
2. Configure exercise aliases and a private spreadsheet ID in local environment settings; never commit credentials.
3. Run synthetic fixtures and parser/evaluation tests.
4. Enable read-only import, then user-approved writes, then reconciliation.
5. Compare generated weekly report to source rows before inviting clients.
6. Export all data and revoke connector access to test portability.

## Community contribution
Contribute anonymized parser fixtures, language variants, equipment conventions, and documented calculation disputes. Do not submit identifiable workout, medical, calendar, or client data. File an issue with reproduction, expected/actual output and fixture. Proposed changes need tests and an independent review.

## Truthful status
This guide defines the adoption contract. The parser, Sheets sync adapter, production MCP server, and PWA remain implementation work; no deployed service is implied.
