# Codex (OpenAI)

Codex loads native Agent Skills. Place a capability folder containing `SKILL.md`
in the repository's `.agents/skills/` or the user's `~/.agents/skills/`. These
are local discovery locations, not an automatic installation on another host.

For reusable distribution, package skills as a Codex plugin. This repository
generates `plugins/starlight` and `plugins/starlight-queen` from their canonical
skills; run `python3 scripts/build_operator_plugins.py --check` to verify parity.
The packages contain no live MCP endpoint or credentials. Install/enable them
through the target host's plugin flow and test invocation there separately.

Use `AGENTS.md` for repository-wide instructions. An authenticated MCP connector
provides tools and data independently of the portable skill body; wrapping prose
as a tool is not necessary for native skill discovery.

Verified 2026-09-30 against https://learn.chatgpt.com/docs/build-skills.
Re-check host documentation before changing installation paths or packaging.

Retain the canonical skill’s "Built on SIP" footer in exported artifacts. This
adapter updates discovery guidance without changing the attestation contract.
