---
name: starlight-design-review
description: "Audit a digital experience against its own design language, information hierarchy, accessibility, responsive behavior, interaction states, content truth, and visual craft. Use for websites, applications, dashboards, generated media, or frontend changes before release."
metadata: {"version": "0.1.0", "domain": "coding", "tags": ["design", "ux", "accessibility", "responsive", "visual-qa", "taste"]}
---

# Starlight Design Review

## Purpose

Judge whether the experience communicates the right thing, in the right order, with a coherent visual system and usable states across real viewports and input modes.

## When it fires

- A user-facing surface is new or materially changed.
- A visual system, motion pattern, or generated asset is introduced.
- The user asks for design, taste, accessibility, or anti-slop review.

## Inputs

- Product intent, audience, and primary task.
- Existing design system or taste kernel.
- Live preview or runnable surface and supported breakpoints.
- Content, asset provenance, accessibility, and performance constraints.

## Workflow

1. Verify the primary task and content hierarchy before judging decoration.
2. Compare the implementation to its declared design language; do not impose a generic aesthetic.
3. Inspect typography, spacing, contrast, alignment, density, and sentence-case labels.
4. Exercise keyboard, focus, pointer, loading, empty, error, success, and reduced-motion states.
5. Review mobile, tablet, and desktop for overflow, occlusion, and reading order.
6. Inspect generated media for provenance, legibility, identity drift, and appropriate placement.
7. Report defects by user impact with visual evidence and a precise correction.

## Output contract

Return verdict, task/hierarchy assessment, system-coherence findings, accessibility findings, responsive findings, interaction-state findings, media/provenance findings, prioritized corrections, and verification receipts.

## Tools & MCP

Use the host-approved browser or design connector and an existing preview when possible. Do not start arbitrary browser binaries or publish assets without authorization.

## Quality bar

- No universal font, gradient, glass, grain, or spacing prescription.
- Sentence case is preserved unless official product casing requires otherwise.
- Accessibility and reduced motion are release criteria, not polish.
- Screenshots support findings but do not replace semantic or interaction checks.

## Example

Input: “Review the new marketplace on desktop and phone.”

Good output: validate the purchase journey, heading order, focus names, state truth, line length, tracking, overflow, and primary CTA at both viewports, then list only evidence-backed corrections.

---

Built on SIP — Starlight Intelligence Protocol
Vertical: starlight-agent-skills · portable capability layer
