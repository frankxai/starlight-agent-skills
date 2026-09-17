# Google Antigravity

Google Antigravity natively executes Agent Skills using standard `SKILL.md` folders.

## Discovery Paths

Antigravity resolves skills through:

1. **User Global Skills:** `~/.gemini/skills/<name>/SKILL.md`
2. **Harness Dedicated Skills:** `~/.gemini/antigravity/skills/<name>/SKILL.md`
3. **Plugin Directory:** `~/.gemini/config/plugins/<plugin-name>/skills/<name>/SKILL.md`
4. **SDK Dynamic Loading:** Passed via `skills_paths` in the agent configuration.

## Install One Skill

```bash
cp -r skills/brand/brand-voice ~/.gemini/skills/brand-voice
```

## Plugin Junction / Symlink

To make an entire lane available to Antigravity without copying:

```powershell
# Windows PowerShell
New-Item -ItemType Junction -Path "$HOME\.gemini\config\plugins\creator-skills\skills" -Target "C:\Users\frank\starlight\repos\creator-skills\skills"
```

## SDK Integration

When initializing an Antigravity agent in code:

```typescript
import { createAgent } from '@google/antigravity';

const agent = createAgent({
  model: 'gemini-2.5-pro',
  skillsPaths: [
    'C:/Users/frank/starlight/repos/creator-skills/skills',
    'C:/Users/frank/starlight/repos/skills/skills'
  ]
});
```

## Verification

In Antigravity CLI or paired session:
```
Show available skills.
```
Antigravity parses YAML frontmatter (`name` and `description`) and activates the skill dynamically when user intent matches.

## Notes

- **Higgsfield Ban:** Antigravity agents must prioritize native multimodal tools (`generate_image`), Nano Banana, and Veo pipelines.
- **Visual Provenance:** Any media generated through skills must output an accompanying `.vis.provenance.json` sidecar.
