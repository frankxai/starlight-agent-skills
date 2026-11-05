# Starlight Vitality — Agent-Native Plant & Performance Intelligence

Status: proposal / non-production. Product owner: Starlight Intelligence. Acquisition: frankx.ai/vitality. Dedicated app and data service to be decided after repo and deployment audit.

## North star
Help plant-forward athletes, coaches, and biohackers record consumption with minimal friction, assess nutrient adequacy and interaction risks using traceable evidence, and connect training/recovery outcomes. Never imply an unvalidated supplement combination is safe.

## MVP vertical slice
1. Private consented user profile (goals, dietary pattern, allergies, medications voluntarily entered, units, timezone); explicit coach-sharing grants.
2. Quick log by text, barcode, saved meal or photo with user-confirmed portions and timestamp; food and supplement events are distinct.
3. Nutrition engine with food-source version, nutrient quantities, provenance, confidence, missingness; distinguish estimated from measured.
4. Deterministic safety rules for allergies, known contraindications, dosage overlap, and medication/supplement interactions. Critical unknowns -> abstain and professional review, not reassurance.
5. Plant-forward meal planner optimizing protein, energy, fiber, iron, B12, calcium, iodine, omega-3 and practical adherence; do not present unverified clinical dosing.
6. Coach dashboard with consented client trends and read-only default.
7. Evidence ledger: source, publication/update dates, population, strength, limitations, review status, expiry. Human review for high-risk rules.

## Interfaces
MCP read tools: search_foods, get_nutrient_profile, get_evidence, inspect_interactions, summarize_intake, plan_meals. Write tools: log_intake and update_goals require explicit confirmation, scoped authorization, audit log and idempotency key. No autonomous supplement or medication changes.

Agent skills: plant-performance-planner; nutrient-adequacy-auditor; supplement-interaction-reviewer; meal-log-assistant; coach-progress-analyst; evidence-research-curator. Each skill must disclose sources, confidence, limitations and abstention conditions.

## Architecture
Next.js mobile-first PWA on Vercel; Postgres with row-level security and consent grants; Cloudflare Workers for bounded ingestion/rules and R2 for user-controlled media. Canonical normalized food and ingredient IDs; evidence sources may include USDA FoodData Central, NIH ODS, PubMed and EFSA, subject to license/API verification. Rules engine independent of LLM. Versioned event ledger, encrypted sensitive data, export/delete, retention controls, strict separation between public reference data and private health records.

## Acceptance gates
- Source licensing and freshness reviewed; deterministic test fixtures for dangerous combinations, duplicate ingredients, allergies, missing medication context and contradictory evidence.
- No fabricated nutrient precision or green 'safe' verdict when evidence absent.
- Explicit consent and access revocation tested; cross-tenant leakage tests pass.
- WCAG mobile UX, quick log target under 15 seconds for repeat meals, accessibility and low-friction correction.
- No public launch or medical claims until privacy, regulatory, clinical-content and security reviews pass.

## Milestones
M0 audit existing repos and deployments; M1 ingestion and evidence schemas; M2 safe logging and nutrient views; M3 interaction review; M4 coach consent and MCP; M5 private beta with measured usability and safety outcomes.
