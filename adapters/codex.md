# OpenAI Codex CLI & Desktop

OpenAI Codex natively loads Agent Skills (`SKILL.md`) and distributes bundles via Agent Plugins (`plugin.json`).

## 1. Native Skill Directory (Direct Install)

Codex automatically discovers skills in:

- **Global Skills:** `~/.codex/skills/<name>/SKILL.md`
- **Project Skills:** `./.codex/skills/<name>/SKILL.md`

### Install One Skill

```bash
cp -r skills/brand/brand-voice ~/.codex/skills/brand-voice
```

### Install a Full Lane (Symlink / Junction)

```powershell
# Windows PowerShell
New-Item -ItemType Junction -Path "$HOME\.codex\skills\creator-skills" -Target "C:\Users\frank\starlight\repos\creator-skills\skills"
```

---

## 2. Agent Plugin Distribution (Recommended for Production)

OpenAI Codex uses Agent Plugins as the vendor-neutral distribution unit. A plugin bundles skills, optional MCP tools, and metadata:

```
starlight-creator/
├── plugin.json          # Agent Plugins 1.0 manifest
├── .codex-plugin/       # Optional marketplace metadata
├── skills/              # Agent Skills (SKILL.md)
└── mcp.json             # Optional MCP tools
```

Install via Codex CLI:
```bash
codex plugin install frankxai/creator-skills
```

---

## 3. Context Budget & Performance Protection

Codex eager discovery scans all installed skills. To prevent Turn 0 context saturation, enforce a catalog budget in `~/.codex/config.toml`:

```toml
[skills]
max_context_tokens = 8000
```

For routine editing, use `model_reasoning_effort = "medium"`. Reserve `xhigh` or Sol Ultra for architecture and complex migrations.

---

## Verification

In Codex:
```
Show active skills or test brand-voice.
```
Codex matches intent against the skill's YAML `description` line and injects the procedure just-in-time.
