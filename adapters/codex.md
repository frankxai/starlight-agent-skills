# Codex (OpenAI)

Codex has no native skill loader. Two supported paths:

## 1. Paste into `AGENTS.md`

Copy the body of `SKILL.md` (drop the YAML frontmatter) into the project's
`AGENTS.md` under a heading, so Codex picks it up as standing instructions.

## 2. Wrap as MCP

If the skill declares `mcp_dependencies` in `manifest.json`, run it behind an MCP
server and register that server in Codex's config. The skill body becomes the
tool's instruction set.

## Notes

- Keep the `manifest.json` `inputs`/`outputs` as the tool schema when wrapping.
- The "Built on SIP" footer should remain in any artifact the skill generates.
