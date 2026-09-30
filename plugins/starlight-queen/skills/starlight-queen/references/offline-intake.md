# Offline intake and packet review

The helper has no network, credentials, queue writes, scheduling or execution. Run with Python 3.11+:

```
python3 scripts/queen_intake.py evidence intake.json --tenant frank --project starlight --repository frankxai/starlight-agent-skills
python3 scripts/queen_intake.py packet envelope.json --repo-root /explicit/checkout
```

Outputs are JSON to stdout. Keep any saved output in a preparation directory outside the live queue. The live Queen consumer scans all `inbox/*.json`; status labels do not provide an execution hold. The outer review artifact is not an envelope, and structural validity is not approval.

Evidence input has exactly `schema`, `scope`, and `observations`. Use schema `starlight.operator_intake.v1`; scope has exactly nonempty `tenant`, `project`, `repository`. Each observation has exactly `source`, `id`, `scope`, `kind`, `declared_state`, `observed_at`, `refs`. `kind` is `work`, `decision`, `run` or `release`; `observed_at` is UTC ISO with milliseconds. `refs` is a nonempty list of references with `kind`, `id`, and optional SHA-256 hash. No prompt/log/credential fields or arbitrary extra fields are accepted. The collector must remove secrets before export; the metadata allowlist is not a secret detector. IDs are opaque IDs, not paths or URLs. Use source links in the manager brief through the authorized connector, rather than smuggling URLs/credentials through this metadata format.

The same source/kind/id replay with identical body is deduplicated. A conflicting body for that key is rejected: reconcile versions at the source before resubmitting. The CLI requires a separately supplied tenant/project/repository selection. Every observation must exactly match that selection. Matching is not authorization; the authenticated collector must enforce access before producing input. Output preserves source-declared status and labels verification `not_evaluated`; it never equates `done` with verified completion.

Packet input is a fully mapped strict existing Queen `envelope:"v1"` with `kind:"task"`. Only standalone tasks are supported; chain/dependency cards are rejected. Required fields: `kind`, `id`, `slug`, `producer`, `status`, `createdAt`, `agent`, integer `priority`, numeric `maxMinutes` from 1 to 25, explicit existing absolute `repo`, `risk`, and `prompt`. The caller must supply these; the helper never chooses a lane, agent or budget. `--repo-root` is the separately supplied allowed checkout and must resolve to exactly `repo`; containment in a broad root is insufficient.

Optional existing contract fields: `idempotencyKey`, `needs`, `allowedChecks`, `requiredChecks`, `baseRef`, `assignedRef`, `requiredAncestors`, `snapshotPaths`. Git-write needs an explicit `assignedRef` in `<remote>/agent/<harness>/<slug>` and nonempty allowed checks. Required checks must be contained in allowed checks. Path/ref syntax is validated but check strings are not executed or authorized. Reject unknown fields, unsafe snapshot paths and oversized/nonregular-file input. The local runtime verifier remains authoritative and can add checks this offline reviewer does not perform.

Pinned consumer: Agentic Ops `fe1ca6449b585fd28ce15ad26c06d4d43e3937d5`, `lifecycle/queen-verify.js` and `lifecycle/wire/Invoke-StarlightQueenLoop.ps1`. Registry, branch ownership, credentials, capacity, approvals, policy, queue admission and actual verification are outside this helper.

Suite daemon schema `starlight.agent_event.v1` is a separate contract. Do not feed this sidecar to it. Built-in adapters at Suite `c9a3f7493a634565ced47578bb1c6c7386d585bb` accept Codex/Hermes/Gemini sources only. A future Paperclip adapter needs explicit source admission, identity mapping, contiguous sequence, immutable replay, cursor checks and verifier-owned outcomes. No automatic status-to-terminal-event conversion is provided here.
