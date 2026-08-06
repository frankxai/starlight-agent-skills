# Example 01 — an exoplanet-atmosphere transmission-spectroscopy paper (illustrative)

## Input

```
paper: arXiv:XXXX.XXXXX  (astro-ph; transit transmission spectrum of a hot Jupiter)
audience: astronomer
```

## Output

```json
{
  "metadata": { "title": "Transmission spectrum of hot Jupiter [name]", "authors": "[team]", "id": "arXiv:XXXX.XXXXX", "date": "2026" },
  "context": {
    "objects": ["hot Jupiter [name] transiting a [type] star"],
    "instruments": ["JWST NIRSpec (illustrative)"]
  },
  "problem": "Constrain the planet's atmospheric composition by measuring how starlight is filtered through its limb during transit.",
  "method": "Transmission spectroscopy: differential flux in- vs out-of-transit across wavelength, fit with atmospheric forward models / retrievals.",
  "results": [
    { "claim": "Detection of a specific molecular absorption feature", "evidence": "Spectrum figure with model fit, §3" },
    { "claim": "Inferred abundance/temperature range", "evidence": "Retrieval posterior, Table/§4" }
  ],
  "caveats": [
    "Detection significance depends on signal-to-noise and the assumed noise model",
    "Retrieved abundances are model-dependent (priors, chemistry assumptions)",
    "Stellar activity / spots can contaminate the transmission signal"
  ],
  "why_it_matters": "Adds a data point to atmospheric composition vs planet/star properties — relevant to formation and migration models.",
  "citations": ["'we detect [feature] at [N]σ' — §3"]
}
```

## Why this is a good result

Instrument and object are named; results are tied to figures/tables; the caveats
are the genuine ones that determine how much to trust an atmospheric detection
(S/N, model dependence, stellar contamination) rather than generic hedging.
Placeholders mark what a real brief must fill from the actual paper.
