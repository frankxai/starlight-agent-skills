# Adapters — run any skill on any runtime

`SKILL.md` is the single source of truth. A skill is **authored once** and runs
everywhere; runtimes differ only in *where the file lives* and *how discovery
works*. These guides document that per runtime — so the per-skill folders stay
clean and DRY.

| Runtime | Guide | Discovery |
|---------|-------|-----------|
| Claude Code | [`claude.md`](claude.md) | `~/.claude/skills/<name>/SKILL.md` (native) |
| Codex | [`codex.md`](codex.md) | paste into `AGENTS.md` or wrap as MCP |
| Cursor | [`cursor.md`](cursor.md) | convert to `.cursor/rules/*.mdc` |
| Gemini CLI | [`gemini.md`](gemini.md) | system-prompt content / ADK |
| OpenCode | [`opencode.md`](opencode.md) | `.opencode/skills/<name>.md` |
| Starlight Intelligence System | [`sis.md`](sis.md) | `scripts/port-skill.mjs` + `skill-rules.json` |

Universal bridge: every runtime supports **MCP**. Any skill whose `manifest.json`
declares `mcp_dependencies` can be driven through an MCP server for maximum
portability.
