# Gemini CLI

Gemini CLI has no native skill registry; deliver the skill as system-prompt
content or via the ADK.

## System-prompt content

Pass the body of `SKILL.md` (without frontmatter) as `--system` prompt content,
or store it under the project's Gemini settings as a reusable instruction block.

## ADK / MCP

For skills with `mcp_dependencies`, expose them through an MCP server and connect
Gemini to it. The skill body is the tool instruction; `manifest.json`
inputs/outputs are the schema.

## Notes

Preserve the output contract and "Built on SIP" footer in generated artifacts.
