# Example 01 — "The JWST orbits the Earth"

## Input

```
claim: "The James Webb Space Telescope orbits the Earth."
strictness: standard
```

## Output

```json
{
  "claim": "The James Webb Space Telescope (JWST) is in orbit around the Earth.",
  "verdict": "refuted",
  "confidence": "high",
  "evidence": [
    {
      "quote": "Webb will orbit the Sun 1.5 million kilometers (1 million miles) away from the Earth at what is called the second Lagrange point or L2.",
      "source": "https://webb.nasa.gov/content/about/orbit.html (NASA — 'Webb's Orbit')"
    }
  ],
  "rationale": "JWST is not in Earth orbit; it orbits the Sun–Earth L2 point ~1.5 million km from Earth, keeping the Sun, Earth, and Moon on the same side of its sunshield.",
  "caveats": ["L2 is a point in the Sun–Earth system; Webb makes a 'halo' orbit around it, not around Earth."]
}
```

## Why this is a good result

The verdict (`refuted`) matches authoritative evidence, confidence is `high` and
justified, and the caveat clarifies the L2 halo-orbit nuance rather than
overstating certainty.
