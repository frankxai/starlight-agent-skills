# Notion OS Patterns

## Audit Schema

| Field | Meaning |
| --- | --- |
| title | Page, database, or data-source title |
| url_or_id | Direct URL or Notion ID |
| object_type | page, database, data-source, connected-source, unknown |
| domain | business, personal, operations, content, knowledge, people, archive, unknown |
| current_role | home, dashboard, database, note, template, project, area, archive, policy, asset |
| privacy_class | private-only, internal, shareable, public-candidate, public-approved |
| health_signal | canonical, useful-fragment, duplicate, stale, sensitive, template-candidate, archive-candidate |
| migration_action | keep-canonical, merge-into-v2, rewrite, templatize, mirror-public, archive, defer |
| confidence | high, medium, low |

Artifact-driven audits should emit at least `estate-map.csv`, `estate-map.md`, `audit-summary.json`, and `red-team.md`. Keep those artifacts inventory-level: titles, IDs/URLs, object types, schema/property names, aggregate counts, classifications, and approval notes. Do not persist raw private page bodies or customer rows.

## Preserve-First Canonical Signals

Mark an existing system `keep-canonical` when it has:

- Clear source-of-truth rules.
- Active operating cadence.
- Linked databases and reusable views.
- Public/private staging separation.
- Source registry, quality gates, metrics loop, or migration control.
- Evidence that other pages feed into it rather than compete with it.

## V2 Database Set

- Projects: outcomes with owner, status, deadline, linked actions, and linked knowledge.
- Areas: durable life/business domains and responsibilities.
- Actions: tasks, follow-ups, reviews, and waiting items.
- Knowledge: source notes, evergreen docs, procedures, and research.
- People/CRM: contacts, partners, customers, and collaborators.
- Content: ideas, scripts, articles, social posts, and releases.
- Assets/Templates: reusable templates, prompts, media, and brand assets.
- Systems/Agents: skills, plugins, automations, and evaluations.
- Decisions/Policies: durable choices and operating rules.
- Archive: preserved inactive material.

## Advanced Modules

- Source Registry: origin, rights, inspiration, and migration action.
- Quality Checklists: safety, voice, accessibility, packaging, and measurement gates.
- Public Staging: sanitized buyer-facing/public-safe mirror.
- Repurpose Queue: derivative content by surface and format.
- Metrics Loop: outcomes and learning by published artifact.
- Migration Control: legacy content routing and approval status.

## Template Rules

- One clear job per template.
- Properties support scanning and review.
- Page body captures context, decision, action, source, and review notes.
- Public variants never contain private examples or live customer/personal data.

## Write Approval Gate

Before any write, state operation, target IDs/URLs, exact change, expected result, rollback path, and schema/view DSL when relevant. Stop if the user has not approved that exact write.
