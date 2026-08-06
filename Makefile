.PHONY: check validate validate-examples catalog catalog-check rules

# Run the full quality gate (what CI runs).
check: validate validate-examples catalog-check rules

# Frontmatter + attestation + manifest↔SKILL.md↔folder integrity.
validate:
	python3 scripts/validate_skills.py

# Worked examples' output JSON actually matches each skill's manifest contract.
validate-examples:
	python3 scripts/validate_examples.py

# Regenerate the catalog from skill frontmatter.
catalog:
	python3 scripts/generate_catalog.py

# Fail if the committed catalog is stale.
catalog-check: catalog
	@git diff --quiet docs/CATALOG.md \
		&& echo "catalog: up to date" \
		|| (echo "catalog: STALE — commit docs/CATALOG.md" && exit 1)

# Every rule + orchestrator resolves to a real skill; no name collisions.
rules:
	node scripts/check-rules.mjs
