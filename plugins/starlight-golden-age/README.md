# Starlight Golden Age

**Prepare. Imagine. Return. Create.**

Three independent skills compose into one practice companion:

| Skill | Useful result |
|---|---|
| `starlight-practice-preparation` | Preparation card and evidence-aware answers about breathwork |
| `starlight-golden-age` | Original future visualization, optional imagined mentor, visual brief |
| `starlight-practice-integration` | One action, draft artifact and optional private memory proposal |

Start here: “Use the three Starlight practice skills to prepare me, guide a brief original
Golden Age visualization after I return, and turn one insight into a useful act today.”

No breathwork is required for the visualization. An authorized instructor or recording
owns any SOMA practice. This independent package is not endorsed by SOMA Breath or Niraj
Naik and does not contain SOMA's Golden Age script, music or licensed protocols.

## Install and use

ChatGPT/Codex: this directory contains a validated `.codex-plugin/plugin.json` and
self-contained `skills/`. Personal skills can be installed independently; public directory
publication is a separate operation, not implied by this repository. There is no bundled
remote MCP server, account system or automatic journal storage.

Claude Code, local checkout:

```sh
claude --plugin-dir ./plugins/starlight-golden-age
```

Invoke `/starlight-golden-age:starlight-golden-age` for the visualization or the corresponding
namespaced preparation/integration skill. To register the repository marketplace after the
branch is available on your chosen ref:

```text
/plugin marketplace add /absolute/path/to/starlight-agent-skills
/plugin install starlight-golden-age@starlight-practice
```

These are documented install paths; a live Claude runtime install has not been verified
in this build environment. After merge, the repository URL can replace the local path.

## Local handoff demonstration

From repository root:

```sh
python3 plugins/starlight-golden-age/skills/starlight-practice-integration/scripts/session_bridge.py preview \
  --input plugins/starlight-golden-age/skills/starlight-practice-integration/references/session-example.json \
  --tenant demo --workspace practice
```

Outputs a bounded action-builder brief and no memory by default. The helper is a pure
preview, not a persistence service or medical screening tool. Existing Starlight Memory
can be connected by a host that enforces its real schema, consent, identity and retention.

## Maintenance and evidence

Edit canonical `skills/education/starlight-*` and
`skills/substrate/starlight-practice-integration` in this repository. Compile with
`python3 scripts/build_golden_age_plugin.py`; verify with
`python3 scripts/test_golden_age.py`. Installed personal skills are versioned snapshots,
not a second source to edit independently.

[Product and pilot](../../docs/golden-age/PRODUCT.md) ·
[Instructor kit](../../docs/golden-age/INSTRUCTOR-KIT.md) ·
[Verification](../../docs/golden-age/VERIFICATION.md)

MIT for original code and text under the repository license. Third-party trademarks,
SOMA materials and any separately introduced Arcanea canon retain their own rights.
