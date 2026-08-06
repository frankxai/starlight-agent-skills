# Starlight Intelligence System (SIS) & ACOS

SIS and ACOS consume skills as first-class verticals. Use the port script rather
than copying by hand — it rewrites self-referential paths and verifies the SIP
attestation footer.

## Port a single skill into SIS

```bash
node scripts/port-skill.mjs cosmos/apod-to-short \
  --target=/path/to/Starlight-Intelligence-System
```

This copies the skill into `<target>/skills/<domain>/<name>/`, rewrites internal
links, and checks the `Built on SIP` footer is present.

## Port into ACOS

```bash
node scripts/port-skill.mjs media/social-repurposer \
  --target=/path/to/agentic-creator-os --dest=.claude/skills
```

## Auto-activation

[`../skill-rules.json`](../skill-rules.json) uses the same schema as ACOS
`.claude/skill-rules.json` and SIS `skills/skill-rules.json`
(`activation_rules[]` of `{ skill, triggers, priority }`). Merge the relevant
entries into the consumer's rules file so skills fire on keyword / file / command
context.

## Dry run

Add `--dry-run` to print the planned destination and attestation check without
writing anything.
