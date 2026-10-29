# Starlight Second Brain

The consumer workflow over existing knowledge and memory owners. This release adds six source-backed skills and a bounded offline knowledge explorer. It does not create another canonical database or hosted memory service.

## Use

- “Resume this project from its latest source-backed context.”
- “Trace which architecture decisions are accepted, superseded or still disputed.”
- “Turn these selected sources into an interactive knowledge map.”

The plugin discovers available authorized source tools. It can operate on supplied files when connectors are absent. Its deterministic compiler uses Python 3.11+ without third-party dependencies; the generated HTML has no external dependencies or background requests. A file explorer is not an MCP App. A connector being available is not proof it has been searched or its data imported.

## Source ownership

Canonical skills live in `skills/substrate/`. `scripts/build_second_brain_plugin.py` compiles their byte-identical flat projection into `plugins/starlight-second-brain/skills/`. Edit the canonical skill and rebuild; do not author a second version in the plugin.

Starlight Memory supplies infrastructure and authenticated scoped recall when connected. Second Brain OS owns its local ingestion implementation and two-vault boundary. Portfolio Registry and product repositories retain their separate authorities. The plugin supplies working knowledge and proposals, not new portfolio truth. No vendor is selected, configured or paid for by installing it.

## Workflows

| Skill | Accepted output |
| --- | --- |
| run-second-brain | Bounded source inventory, current context, gaps, next action |
| distill-brain-sources | Cited atomic proposals with source branches, revisions and dates preserved |
| reconcile-brain-decisions | Scoped decision history, explicit supersession and unresolved conflict |
| reflect-on-knowledge | At most three evidence-backed hypotheses and one recommended test |
| visualize-knowledge | Validated packet and searchable offline graph/list/timeline/source explorer |
| compile-brain-context | Portable, labeled context handoff with source and relationship provenance |

See `skills/substrate/visualize-knowledge/references/packet-contract.md` for the exact interchange. Privacy/acceptance classifications are supplied evidence, not an automatic authorization or truth attestation. Unknown source locators and unavailable access remain representable.

## Verification

```
python3 scripts/build_second_brain_plugin.py --check
python3 -m unittest discover -s skills/substrate/visualize-knowledge/tests -v
make check
```

The compiler's 30 checks include mixed-scope rejection, citation requirements, acceptance provenance, raw-payload rejection, source access states, unknown locators, relationship provenance, preserved historical identities, source-link restrictions, HTML script-termination escaping, duplicate keys, bounds and output roundtrip. UI JavaScript syntax was checked. A fresh-agent synthetic handoff preserved the accepted raw-chat boundary against a newer conflicting assistant summary; its findings produced regression checks.

Browser preview was unavailable in the build environment. No pixel-level or live browser interaction pass is claimed. Existing source-connector flows were inspected but a newly installed session has not been tested. Public directory submission and hosted sync remain outside this release.

## Next acceptance boundary

Validate the saved plugin in a fresh session against one explicitly selected project. Require the agent to recover one current decision with its original locator, preserve one contrary draft, create one useful handoff, and reproduce it from the source packet. Evaluate successful recall, citation correctness, contradictions retained, useful next action and time/cost observed. Do not promote broad ingestion, additional providers or live writes until this slice is accepted.

Any hosted extension must preserve existing source ownership and use a qualified authenticated projection from the existing memory owner. Require tenant-isolation, revocation, deletion propagation, source-version fidelity and recovery tests. Visual flow animation must represent actual events; it cannot imply traffic that has not been measured.

Built on SIP.
