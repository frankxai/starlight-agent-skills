---
name: cosmos-content-producer
description: "Reference orchestrator that turns one NASA/ESA image into a rights-cleared vertical short plus a multi-platform launch pack. Use when a creator wants the full cosmos content pipeline from a single image, end to end."
type: orchestrator
composes: [apod-to-short, rights-check-nasa-esa, space-social-repurposer, thumbnail-concept]
---

# Cosmos Content Producer

> One NASA/ESA image → a rights-cleared short + a ready-to-post launch pack.

## What it does

Chains four skills into a single producer play. The defining discipline: the
rights check runs **before** distribution, and the verified credit line is
propagated into every downstream artifact.

## Pipeline

1. **`apod-to-short`** — turn the image into a 30–60s vertical short package
   (hook, script, captions, shot list, draft rights line).
2. **`rights-check-nasa-esa`** — resolve usage rights for the asset. **Gate:** if
   the verdict is `do-not-publish-yet` or `restricted` for the intended use, stop
   and surface it; do not proceed to distribution.
3. **`space-social-repurposer`** — expand the short into a coordinated X /
   LinkedIn / Instagram pack, with the verified credit propagated to every variant.
4. **`thumbnail-concept`** — produce thumbnail concepts for the short (overlay
   ≤4 words, honest to the content).

## Inputs

- `image` (required) — NASA/ESA image URL/page with caption + credit.
- `platforms` (optional) — distribution targets; default X + LinkedIn + Instagram.
- `voice` (optional) — `starlight` (default), `arcanea`, `frankx`.

## Output

A bundle: `{ short, rights_verdict, social_pack, thumbnails }`. The rights verdict
is included explicitly so the human approves before anything publishes.

## Guarantees

- Rights are cleared before distribution (the gate is non-skippable).
- The exact credit line appears on every artifact that shows the image.
- No fact is introduced that isn't traceable to the source caption.

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
