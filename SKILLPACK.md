# Starlight skill pack

**Repo:** `frankxai/starlight-agent-skills` (this tree)  
**Not an awesome-* catalog.** This is the Starlight execute layer (SIS sibling).

```sh
npx skills add frankxai/starlight-agent-skills
```

## Include

Starlight voice, coding, cosmos, research, media, education, and substrate ops that are brand-neutral Starlight:

- `starlight-voice`
- `cosmic-code-lab`
- cosmos: `apod-to-short`, `arxiv-space-paper-to-brief`, `cosmic-mythic-overlay`, `nasa-image-to-atlas-page`, `rights-check-nasa-esa`, `rocket-launch-to-reel`, `space-social-repurposer`
- research / media / education in `skills/`
- substrate: `swarm-queen-coordination`, `payments-mandate`, `notion-operating-system`

## Exclude (other brands own these)

- `arcanea-mythic-overlay` → Arcanea pack
- `frankx-authority-post` → FrankX, not this pack
- `agentic-income`, `affiliate-audit` → Agentic Income / Passive Income packs
- `templates/skill-template`

## MCP pair

context7 (docs). Queen/Railway stay host runtime, not this pack.

## Maintain

1. One skill = one folder = `SKILL.md` with trigger `description`.
2. No host paths, no Phone Link, no secrets.
3. After a hard session: patch the skill in **this repo**, not Hermes dump, not awesome lists.
4. `npx skills add frankxai/starlight-agent-skills --list` must only be installed via `--skill` when excluding the four foreign names above — or install all then ignore foreign brands.
5. skills.sh unlisted URL: founder creates at https://skills.sh/packs/create pointing at **this GitHub repo**, not awesome-hermes-*.
