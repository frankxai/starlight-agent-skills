# Starlight operators: execution and integration

This change supplies two portable capabilities and two deterministic, skills-only Codex plugin packages. It does not install a connected ChatGPT app, register a persistent Queen identity, migrate a runtime, or activate Paperclip. Its offline helper prepares review artifacts; it cannot dispatch work.

| Capability | Immediate job | Package |
|---|---|---|
| Starlight | Implement a bounded change in its existing owner; test and prepare release evidence | `plugins/starlight` |
| Starlight Queen | Triage scoped agent work, decisions and blockers; prepare assignments; reconcile outcomes | `plugins/starlight-queen` |

The capabilities have distinct names and each package includes one skill. The existing Product Studios package remains independent. Each host supplies its own authenticated GitHub, Vercel and runtime tools. No `.mcp.json`, fabricated server URL, credential file or new scheduler is packaged.

## Use from the current host

Invoke Starlight for implementation and Starlight Queen for coordination. Personal skill installation and Codex plugin-package publication are separate delivery channels; neither establishes fleet activation. A host must support the package format and pass a native install/invocation smoke test before that package is reported installed there. Claude, OpenCode and Hermes can consume the canonical skill using their supported skill mechanisms; this is not a claim that they support Codex plugin metadata.

Build and verify:

```sh
python3 scripts/build_operator_plugins.py
python3 scripts/validate_operator_plugins.py
python3 scripts/test_operator_plugins.py
python3 scripts/test_queen_intake.py
```

Plugin files are generated from `skills/substrate/{starlight,starlight-queen}` and the compiler's manifest definition. Edit those sources, then rebuild. Personal-host projection removes the canonical metadata frontmatter line only and retains instruction-body/resource bytes. `--check-personal NAME --personal-root EXACT_DIRECTORY` verifies parity without installing or editing anything.

## Systems to reuse

| Owner boundary | Existing system | Next change belongs here |
|---|---|---|
| Portfolio authority | Agentic Ops Registry and admitted dispatch | Artifact placement, runtime identity, policy, scope and release authorization |
| Portable capability source | This repository | Skills, projections, helper, tests and packages |
| Private operator view | Starlight Suite | Scoped observations, decisions and receipt links through existing surfaces |
| Harness configuration | Registered agent-config owner | Queen identity/configuration reconciliation and available adapter bindings |
| Execution records | Upstream Paperclip | Native tasks, runs, decisions and adapters, integrated through a narrow admitted bridge |
| Persistent runtime | Current accepted entity/workflow owner | One Queen entity, one durable orchestrator per workflow |
| Public web surface | Each registered website/Vercel project | Product onboarding and sanitized public projections |
| Personal memory | Private vault authority and scoped projections | Decision/outcome references rather than global raw transcripts |

Create no new repository, backend, queue, catalog or memory authority for this first slice. Resolve current Registry owners and open work before later changes. An upstream Paperclip pin and optional maintained fork are release/dependency choices; copying its whole code into the Suite would create a second maintenance and authority surface.

## Sequential integration slices

1. **Capability/package:** validate these sources, exact-head CI, independent review and host installation. This is the implemented slice.
2. **Admission:** resolve capability/artifact records and one Queen identity. Reuse existing Dispatch work; do not fork draft routing policy. Record current runtime versus accepted target placement.
3. **Observation bridge:** authorize one tenant/project/repository; preserve Paperclip and harness source IDs, observed timestamps, declared state and evidence references. Start read-only. Distinguish managed versus observed sessions. Do not convert native `done` into verified completion or claim every hosted chat is observable.
4. **Decision projection:** expose only authorized source decisions with origin, owner, options, choice, expiry and effect result; submit choices back through the source's admitted authorization. No board impersonation or duplicate approval queue.
5. **Bounded execution pilot:** one explicitly mapped task through the existing consumer. Prove identity, scope, budget, idempotency, lease handling, failure/retry, kill switch and verifier-owned completion. Only the existing scheduler owns that task.
6. **Operator surface and productive loop:** project those receipts into Suite; resolve website/project/alias bindings before public onboarding or release. Measure accepted outcomes, rework, decision wait, cost and time to verified release rather than agent count.

Run one shared-platform primitive in change at a time, using current Registry WIP and budget limits. Independent checks and existing release authorization apply at every slice. A prepared plan, schema-valid event, passing check or READY build never substitutes for admitted runtime behavior.

## Offline boundary

The helper accepts whitelisted metadata and a separately selected scope. Matching does not authorize source access. The authenticated collector must enforce access before export and remove sensitive values. The helper has no DLP engine.

Standalone Queen packets require caller-supplied agent, exact existing absolute checkout, budget and checks. Chain cards and missing mappings are refused. Input files must be regular, bounded JSON; unknown fields and duplicate keys are refused. Output goes to stdout inside a review wrapper. **Do not save it in a live inbox:** the current Queen consumer scans all inbox JSON and does not honor a review-only status as a hold.

See the Queen capability's [offline contract](../skills/substrate/starlight-queen/references/offline-intake.md). Runtime consumers remain authoritative for policy, credentials, approval, queue admission, idempotency history and completion.

## Evidence limits

Local source-content validators, adversarial helper tests, deterministic package drift checks and fresh-agent exercises are different evidence from full-history release checks, native plugin installation or live execution. CI checks release history using a full checkout; never weaken that validator to make a partial local materialization look like a release.
