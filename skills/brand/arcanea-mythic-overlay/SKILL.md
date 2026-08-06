---
name: arcanea-mythic-overlay
description: "Add an Arcanea mythic overlay to factual content — a canon-attributed narrative framing (Guardian/Luminor names, mythic register) layered over the real facts, clearly separable from them. Use when giving content an Arcanea mythology flavor, framing a piece in the Arcanea universe, or asked for a 'mythic' treatment."
version: 0.1.0
domain: brand
tags: [arcanea, mythic, canon, narrative, framing]
---

# Arcanea Mythic Overlay

> Factual content → the same facts with an Arcanea mythic framing layered on top,
> kept clearly separable.

## Purpose

Arcanea is the mythic universe register (Guardian/Luminor names, CC-BY-NC canon).
This skill adds an Arcanea narrative overlay to real content — a framing that makes
it feel part of the universe — while keeping the factual layer intact and clearly
distinguishable, so the mythology never overwrites the truth.

## When it fires

- Keyword triggers: `arcanea`, `mythic`, `mythic overlay`, `guardian framing`,
  `universe framing`
- File triggers: `arcanea/**`, `*.myth.md`
- Command triggers: `/arcanea-mythic-overlay`

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| `content` | yes | The factual base (e.g. a space short, a brief). |
| `intensity` | no | `light` (default), `medium`, `full`. |

## Workflow

1. **Lock the facts** — identify the factual claims that must remain true and
   unchanged. ✅ Check: a clean factual layer exists.
2. **Choose canon hooks** — relevant Guardian/Luminor names and motifs (Arcanea
   canon, attributed CC-BY-NC).
3. **Layer the framing** — narrative wrapper at the chosen `intensity`, around
   (not replacing) the facts.
4. **Separation pass** — the output marks which parts are myth and which are fact;
   facts are never altered by the overlay.
5. **Attribution** — note Arcanea canon usage (CC-BY-NC) per the brand register.

## Output contract

```json
{
  "factual_layer": "string — unchanged facts",
  "mythic_overlay": "string — narrative framing",
  "combined": "string — presented piece with myth/fact distinguishable",
  "canon_attribution": "string — Arcanea CC-BY-NC note"
}
```

## Tools & MCP

- Tools: `Read`. MCP: none required.

## Quality bar

- [ ] Factual layer is preserved verbatim in meaning; myth never edits fact.
- [ ] Myth and fact are distinguishable in the output.
- [ ] Arcanea canon is attributed (CC-BY-NC).
- [ ] Register is Arcanea-mythic, not Starlight-substrate.

## Example

Input: the APOD "Pillars of Creation" short → `factual_layer` keeps the science +
credit; `mythic_overlay` frames the pillars in Arcanea canon; `combined` keeps
them separable.

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
