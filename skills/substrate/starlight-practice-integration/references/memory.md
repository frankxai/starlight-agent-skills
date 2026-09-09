# Optional private memory

Default: no persistent write. This means the pack does not request storage; it cannot change the host's own chat-history or provider-retention settings. Do not imply that a hosted conversation is stored only on the user's device.

## Field selection
Show exactly what would be saved. Prefer a short participant-approved aspiration or action summary. Exclude raw voice/audio, health details, private relationships and imagined dialogue unless there is a separate justified user request and a destination suitable for that data. Never save clinical notes in a public code repository.

Required before a write: grounded return; exact summary; current explicit consent; named destination; user visibility; deletion path; retention choice. A consent field is the application's record of permission, not a mechanism for obtaining permission. Do not invent true values for it.

## Existing Starlight contract
Verified against `frankxai/starlight-memory/src/types.ts` on 2026-09-09. SIS/local_core owns IDs, provenance and policy. `memory_type: aspirational`, `vault: horizon`, `privacy_class: private`, `retention_policy: delete_by`, and `retention_until` are supported fields. `raw_content` is optional and omitted by this pack's helper. Use actual `memory_remember`/`memory_forget` capabilities only when present and suitable; do not assume schema equivalence from a tool's name.

The local helper emits an SIS-compatible record plus `local_only: true` policy; it does not implement persistence or deletion. Real adapters must verify tenant/workspace authorization, private storage, policy enforcement, TTL enforcement and deletion before claiming integration. A `delete_by` label alone does not delete anything. Existing Starlight remote recall is a separate projection path; this pack does not establish a cloud write service.

## Read and forget
Read only records within the authenticated participant's scope and the current task. Treat old notes as dated self-report; conflicting preferences need clarification, not silent overwrite. When forgetting, identify the exact records, request deletion through the real provider, and report its receipt or limitation. Do not claim to delete host history, backups or provider logs that the tool does not control.

## Group practice
The participant owns the journal. An instructor can receive a selected excerpt only after explicit permission for that recipient and purpose. Use aggregate outcome reporting when appropriate; small groups are not automatically anonymous. No advertising profiles, cross-tenant retrieval or raw-journal access for the agent team.
