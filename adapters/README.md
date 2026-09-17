# Adapters — Run Any Skill on Any Runtime

`SKILL.md` is the single source of truth. A skill is **authored once** and runs everywhere; runtimes differ only in *where the folder lives* and *how discovery works*.

These guides document discovery and installation per runtime — so individual skill definitions remain 100% clean, portable, and DRY.

## Supported Runtimes

| Runtime | Guide | Native Discovery Path | Distribution Format |
| :--- | :--- | :--- | :--- |
| **Claude Code** | [`claude.md`](claude.md) | `~/.claude/skills/<name>/SKILL.md` | Direct directory / Claude Plugin |
| **OpenAI Codex** | [`codex.md`](codex.md) | `~/.codex/skills/<name>/SKILL.md` | Direct directory / Agent Plugin (`plugin.json`) |
| **Grok Build (xAI)** | [`grok.md`](grok.md) | `~/.grok/skills/<name>/SKILL.md` | Direct directory / `extra_skill_dirs` |
| **Google Antigravity** | [`antigravity.md`](antigravity.md) | `~/.gemini/antigravity/skills/` | Direct directory / SDK `skills_paths` |
| **Cursor** | [`cursor.md`](cursor.md) | `.cursor/rules/*.mdc` | Agent Plugins / Rule files |
| **Gemini CLI** | [`gemini.md`](gemini.md) | `~/.gemini/skills/` | System instructions / ADK |
| **OpenCode** | [`opencode.md`](opencode.md) | `.opencode/skills/<name>.md` | Project-local markdown |
| **Starlight Intelligence** | [`sis.md`](sis.md) | `starlight-agent-skills/` | SIS memory + skill-rules.json |

---

## Universal Architecture: The 3 Planes

```
PLANE 1 — CANON (Write Once)
  skills/<lane>/<skill>/SKILL.md
  references/  scripts/  assets/
  manifest.json + examples/ + tests/

PLANE 2 — PROJECTORS (Compile Many)
  adapters/*.md          # Per-runtime install docs
  plugins/*              # Agent Plugins 1.0 (plugin.json)
  installers             # npx skills add, agy plugin, codex plugin

PLANE 3 — CONTROL (Compose & Govern)
  SIS memory + evals
  ACOS agents + router
  Hermes routing + PR gates
```

## The Golden Law

**Never fork skill bodies across harnesses.**  
A change to procedural knowledge happens once in the canonical repository. Packaging, paths, and marketplaces are compiled projections.
