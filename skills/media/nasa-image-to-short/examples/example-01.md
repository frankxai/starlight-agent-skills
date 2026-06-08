# Example 01 — Hubble image of Saturn

## Input

```
image: "Hubble image of Saturn. Caption: Hubble's view of Saturn shows its rings,
made mostly of ice, and seasonal changes in its atmosphere. Credit: NASA, ESA, and
the OPAL team."
length: 40
voice: starlight
```

## Output

```json
{
  "hook": "Saturn's rings are mostly ice — and Hubble watches them tilt with the seasons.",
  "script": "This is Saturn, seen by Hubble. Those rings aren't solid — they're countless particles, mostly water ice, orbiting the planet. And because Saturn is tilted like Earth, it has seasons. Over the years, Hubble has tracked subtle changes in its atmosphere and the angle of the rings as the seasons turn. One planet, one telescope, patiently watching a world change.",
  "captions": ["Saturn, by Hubble", "Rings = mostly ice", "Saturn has seasons", "Hubble tracks the change"],
  "shot_list": [
    "Slow push toward the planet, 0–10s",
    "Punch-in on the rings, label 'mostly water ice', 10–22s",
    "Pull back, overlay 'seasonal changes', 22–40s"
  ],
  "rights_line": "Credit: NASA, ESA, and the OPAL team",
  "duration_sec": 40
}
```

## Why this is a good result

Facts (icy rings, axial tilt → seasons, OPAL atmospheric monitoring) are all
caption-traceable; the multi-party credit is preserved verbatim and would route
through `rights-check-nasa-esa`.
