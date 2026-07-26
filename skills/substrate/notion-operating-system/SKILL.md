---
name: notion-operating-system
description: Design safe, private-first Notion operating systems, estate audits, parallel rebuilds, template systems, and public mirrors. Use when asked to map a Notion workspace, clean or restructure Notion, create business/personal Notion dashboards, build reusable Notion templates, or turn private Notion content into sanitized public docs. Portable and brand-neutral. Trigger phrases: map my Notion, Notion estate audit, restructure Notion, Notion operating system, Notion dashboard, Notion template system, publish Notion docs.
type: substrate
version: 0.1.0
domain: substrate
---

# Notion Operating System

## Policy

Start read-only. Search, fetch, team lookup, and aggregate data-source queries are safe for audits. Do not create, update, move, duplicate, publish, apply templates to, create databases/views, alter schemas, or delete Notion content until the user approves exact targets and changes in the current thread.

## Workflow

1. Audit current state with search/fetch before designing a rebuild.
2. Create an estate map with source citations, privacy class, health signal, database health, and migration action. When a local compiler exists, generate deterministic CSV, Markdown, summary JSON, and red-team artifacts from inventory-level evidence.
3. Identify existing canonical systems before designing anything new. Preserve hubs/databases with clear source-of-truth rules, active operating views, public/private staging, source registries, quality gates, and metrics loops.
4. Design a parallel v2 hub instead of mutating the old workspace in place.
5. Use a small set of canonical databases: Projects, Areas, Actions, Knowledge, People/CRM, Content, Assets/Templates, Systems/Agents, Decisions/Policies, and Archive.
6. Add advanced modules only when justified: Source Registry, Quality Checklists, Public Staging, Repurpose Queue, Metrics Loop, and Migration Control.
7. Make templates sparse, useful, and reviewable; every template needs a clear job and privacy class.
8. Publish only curated mirrors or sanitized templates by default.
9. Keep an approval log for every write action.

## Estate Map Fields

Use `references/notion-os-patterns.md` for schema and patterns. At minimum capture: title, URL/ID, object type, domain, current role, privacy class, health signal, migration action, confidence, and notes.

## Default Architecture

Use a parallel parent page named `Notion OS v2 Draft` unless the user gives a specific name. Build dashboards as operating views, not decorative homepages.

## Public Boundary

Classify content as `private-only`, `internal`, `shareable`, `public-candidate`, or `public-approved`. Public outputs must be sanitized and approved before publication.

## Output Contract

Return:

- Estate summary.
- Sitemap or database map.
- Duplicate/stale clusters.
- Database health and aggregate counts where safe.
- V2 architecture.
- Template plan.
- Public/private matrix.
- Migration waves and approval gates.
- Red-team findings and low-confidence rows.

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
