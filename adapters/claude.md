# Claude Code (native)

Claude Code reads skills natively. `SKILL.md` is already in the right format.

## Install one skill

```bash
cp -r skills/cosmos/apod-to-short ~/.claude/skills/apod-to-short
```

## Install the whole library

```bash
for d in skills/*/*/; do
  name=$(basename "$d")
  cp -r "$d" ~/.claude/skills/"$name"
done
```

Claude auto-activates a skill from its `description` (lead with "Use when …").
For project-scoped install, copy into `<project>/.claude/skills/` instead.

## Notes

- `examples/`, `tests/`, and `references/` travel with the skill and are loaded
  on demand.
- No conversion needed — this is the canonical runtime.
