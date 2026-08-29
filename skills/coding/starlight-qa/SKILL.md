---
name: starlight-qa
description: "Exercise a web experience or API through real user flows, semantic accessibility checks, responsive viewports, console/network inspection, and release-specific assertions. Use when a preview or deployed surface needs evidence-based QA; use the host-approved browser connector and avoid unauthorized external side effects."
metadata: {"version": "0.1.0", "domain": "coding", "tags": ["qa", "browser", "accessibility", "responsive", "api", "visual-regression"]}
---

# Starlight QA

## Purpose

Prove that the supported journey works on the candidate revision, not merely that a page renders.

## When it fires

- A web, mobile-web, API, installer, or marketplace flow is ready for verification.
- Responsive, accessibility, network, or state regressions are possible.
- A preview must be checked before merge or production.

## Inputs

- Exact candidate URL or revision and supported environments.
- Critical journeys, expected outcomes, and side-effect boundaries.
- Test accounts or fixtures explicitly approved for the run.
- Accessibility, performance, and browser support requirements.

## Workflow

1. Confirm the candidate revision and environment.
2. Load each critical route and inspect status, console, and failed requests.
3. Exercise the journey with role/label-based interactions and observable assertions.
4. Test validation, loading, empty, error, success, refresh, and back-navigation states as relevant.
5. Verify keyboard access, focus, names, heading order, reduced motion, contrast, and image alternatives.
6. Check representative phone, tablet, and desktop viewports for overflow and occlusion.
7. Capture the smallest useful screenshot or payload receipt for each material finding.
8. Re-run focused checks after fixes and report anything not tested.

## Output contract

Return candidate revision/URL, environments, journeys, pass/fail assertions, console/network findings, accessibility findings, responsive findings, evidence references, defects with reproduction, and untested boundaries.

## Tools & MCP

Use the browser or computer-use capability approved by the active host. Reuse existing sessions where policy requires it. Never hardcode a local CDP endpoint as a portable dependency. Do not submit real purchases, publish content, send messages, or alter production data without explicit authorization.

## Quality bar

- Assertions target user-observable outcomes.
- Semantic checks complement visual screenshots.
- The report distinguishes automated, manual, and inferred results.
- No “fully tested” claim when environments or destructive paths were skipped.

## Example

Input: “QA the Academy evidence export on the PR preview.”

Good output: fill the labeled fields, complete the evidence phases, prepare the JSON, validate its schema/counts/approval state, verify the download link, inspect mobile overflow and semantics, and name any browser-download limitation.

---

Built on SIP — Starlight Intelligence Protocol
Vertical: starlight-agent-skills · portable capability layer
