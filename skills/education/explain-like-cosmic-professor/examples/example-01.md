# Example 01 — redshift

## Input

```
concept: "redshift"
level: curious-beginner
```

## Output

```json
{
  "hook": "The color of a galaxy's light tells you whether it's running away from you — and how fast.",
  "ladder": [
    { "level": "intuitive", "text": "You know how a siren sounds lower-pitched as the ambulance drives away? Light does something similar: when a source moves away, its waves get 'stretched' toward the red end of the spectrum." },
    { "level": "mechanistic", "text": "Wavelength is stretched as the source recedes, shifting features in its spectrum toward longer (redder) wavelengths. Astronomers measure this by how far known spectral lines have moved." },
    { "level": "precise", "text": "Redshift z = (λ_observed − λ_emitted) / λ_emitted. For distant galaxies, cosmological redshift comes from the expansion of space itself stretching the light in transit — not simply local motion through space." }
  ],
  "misconception": "Redshift is NOT just the Doppler effect for everything. Nearby objects show a Doppler shift from their motion, but the redshift of distant galaxies is dominated by cosmological expansion — space stretching, not the galaxy speeding through space.",
  "check": {
    "question": "Two galaxies have z = 0.01 and z = 0.10. Which is receding faster / is farther in the expanding-universe picture?",
    "answer": "z = 0.10 — larger redshift means its light was stretched more, corresponding to greater recession velocity / distance."
  },
  "go_deeper": "Look up the difference between Doppler redshift, gravitational redshift, and cosmological redshift."
}
```

## Why this is a good result

The precise rung is correct (z definition; cosmological vs Doppler distinction);
the analogy (siren) illuminates without misleading; the misconception named is the
genuine common error.
