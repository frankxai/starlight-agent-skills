# Contributing

Starlight Agent Skills is a curated, production-grade capability library. The bar
is high and the format is strict so every skill composes across runtimes and the
Starlight ecosystem.

## The skill standard

Every skill MUST:

- Live at `skills/<domain>/<skill-name>/SKILL.md` where `<domain>` is one of
  `research`, `media`, `education`, `coding`, `brand`, `cosmos`.
- Start with YAML frontmatter: `name`, `description`, `version`, `domain`
  (`tags` optional). See [`docs/SKILL_SPEC.md`](docs/SKILL_SPEC.md).
- Use a `name` that is lowercase, kebab-case, ≤64 chars (`^[a-z0-9][a-z0-9-]*$`).
- Give a specific `description` (≤1024 chars) that tells the model **when** to fire
  ("Use when …") with real trigger keywords.
- Follow the body skeleton: Purpose · When it fires · Inputs · Workflow · Output
  contract · Tools & MCP · Quality bar · Example.
- Carry the `Built on SIP` attestation footer.
- Pass `python3 scripts/validate_skills.py`.

Strongly recommended: a `manifest.json`, plus `examples/` and `tests/` for any
skill people will actually run.

## Quality bar

- ✅ **Accurate** — every claim verifiable; cite sources; respect content rights.
- ✅ **Actionable** — the workflow is a checkable procedure, not vibes.
- ✅ **Grounded** — no spiritual/guru language; show, don't tell (see Frank DNA).
- ✅ **Portable** — works from a single `SKILL.md` across runtimes.
- ❌ No marketing filler, unverified claims, or low-effort single-typo PRs.

## Workflow

```bash
# 1. Branch
git checkout -b feature/<short-name>

# 2. Start from the template
cp -r templates/skill-template skills/<domain>/<skill-name>

# 3. Author SKILL.md (+ manifest/examples/tests), add a skill-rules.json entry

# 4. Validate + regenerate the catalog
python3 scripts/validate_skills.py
python3 scripts/generate_catalog.py
node scripts/check-rules.mjs

# 5. Commit the skill AND the regenerated docs/CATALOG.md, open a PR
```

## Adding a skill-rules.json entry

Add one object to `activation_rules[]` (schema in
[`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)). The `skill` id must equal the
skill's `name`. `check-rules.mjs` fails CI if it doesn't resolve to a real skill.
