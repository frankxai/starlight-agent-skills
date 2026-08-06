# Example 01 — shipped a portable skills library

## Input

```
seed: "Shipped a 22-skill portable library that runs across 5 runtimes from one
SKILL.md per skill, with validation + attestation enforced in CI."
platform: linkedin
cta: "soft question"
```

## Output

```json
{
  "platform": "linkedin",
  "post": "I shipped a 22-skill agent library that runs unchanged across Claude, Codex, Cursor, Gemini, and OpenCode — one SKILL.md per skill, no per-runtime forks.\n\nThe lesson that made it portable: treat the skill file as the single source of truth and push every runtime difference into a thin adapter layer. The moment you start maintaining a separate copy per tool, the library rots. CI enforces the contract — frontmatter spec, catalog freshness, and an attestation footer on every skill — so quality doesn't depend on remembering to check.\n\nWhat's your rule for keeping a capability library from fragmenting across tools?",
  "hook": "I shipped a 22-skill agent library that runs unchanged across Claude, Codex, Cursor, Gemini, and OpenCode.",
  "lesson": "Make the skill file the single source of truth; push runtime differences into a thin adapter layer, and enforce the contract in CI.",
  "claims_checked": [
    "22 skills — count is exact and verifiable in the repo",
    "5 runtimes — adapters exist for each",
    "CI enforces the contract — validate_skills.py + catalog check run on every push"
  ]
}
```

## Why this is a good result

Leads with the demonstrated result; teaches exactly one concrete lesson; stays
humble (no grandiose impact claims); every claim is checked and earned.
