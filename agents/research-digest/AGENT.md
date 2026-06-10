---
name: research-digest
description: "Reference orchestrator that turns one research paper into a verified brief and a publish-ready authority post. Use when a creator wants to read, fact-check, and share a paper in one pass."
type: orchestrator
composes: [arxiv-paper-to-brief, claim-verification, frankx-authority-post]
---

# Research Digest

> One paper → a citation-faithful brief + a verified authority post.

## What it does

Chains three skills so that nothing gets shared before it's checked. The brief's
headline claim is verified independently before it becomes a public post.

## Pipeline

1. **`arxiv-paper-to-brief`** — produce a structured brief (problem, method,
   results-with-evidence, limitations, why-it-matters, citations).
2. **`claim-verification`** — take the brief's single headline claim and verify it
   against sources. **Gate:** if the verdict is `refuted` or `unverifiable`, revise
   the brief before proceeding; never post an unverified headline.
3. **`frankx-authority-post`** — turn the verified takeaway into an authority post
   that leads with the result and stays humble.

## Inputs

- `paper` (required) — arXiv URL/ID, PDF, or text.
- `audience` (optional) — `expert` (default), `practitioner`, `general`.
- `platform` (optional) — `linkedin` (default) or `x`.

## Output

A bundle: `{ brief, verification, post }`. The verification verdict travels with
the post so the human sees the evidence behind the claim.

## Guarantees

- The posted headline claim is verified, not assumed.
- Every result in the brief is tied to a figure/table/section.
- The post leads with a demonstrated result; no grandiose claims.

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
