# Grok Build (xAI)

Grok Build reads Agent Skills natively using the vendor-neutral `SKILL.md` format.

## Discovery Paths

Grok automatically discovers skills in:

1. **Project-local**: `./.grok/skills/<name>/SKILL.md` (walked up to repo root)
2. **Global user**: `~/.grok/skills/<name>/SKILL.md`
3. **Extra directories**: Any paths listed under `[paths] extra_skill_dirs` in `~/.grok/config.toml`

## Install One Skill

```bash
cp -r skills/brand/brand-voice ~/.grok/skills/brand-voice
```

## Install via npx skills

```bash
npx skills add frankxai/creator-skills --dest ~/.grok/skills
```

## Configure Extra Paths (Optional)

In `~/.grok/config.toml`:

```toml
[paths]
extra_skill_dirs = [
  "C:/Users/frank/starlight/repos/creator-skills/skills",
  "C:/Users/frank/starlight/repos/skills/skills"
]
```

## Verification

In Grok Build, prompt:
```
Show active skills or test brand-voice.
```
Grok auto-selects skills based on the YAML `description` trigger line.

## Notes

- Keep Turn 0 context lean: Grok parses skill frontmatter dynamically on startup.
- Never duplicate skill bodies across harnesses; symlink or point `extra_skill_dirs` to your canonical skills repository.
- Use Grok-native features (X search, Imagine, Voice) through dedicated capability skills rather than forking general logic.
