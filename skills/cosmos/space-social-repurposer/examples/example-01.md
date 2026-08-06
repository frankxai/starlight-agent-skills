# Example 01 — repurpose the Saturn short with credit propagation

## Input

```
source: the nasa-image-to-short output for Saturn (Credit: NASA, ESA, and the
OPAL team)
platforms: [x, linkedin, instagram]
voice: starlight
```

## Output

```json
{
  "core_message": "Saturn's rings are mostly ice, and Hubble tracks its seasonal changes over the years.",
  "x_thread": [
    "Saturn's rings aren't solid — they're countless particles, mostly water ice. And Hubble has been watching them tilt with the seasons. 🪐",
    "Saturn is tilted like Earth, so it has seasons. Over years, Hubble tracks subtle changes in its atmosphere and ring angle.",
    "Image: NASA, ESA, and the OPAL team."
  ],
  "linkedin": "Saturn's rings look solid, but they're countless particles — mostly water ice — orbiting the planet. Because Saturn is tilted like Earth, it has seasons, and Hubble has spent years tracking subtle changes in its atmosphere and the angle of its rings.\n\nImage: NASA, ESA, and the OPAL team",
  "instagram": {
    "caption": "Saturn's rings are mostly ice 🧊 — and Hubble watches them tilt with the seasons. Image: NASA, ESA, and the OPAL team",
    "hashtags": ["#Saturn", "#Hubble", "#astronomy", "#nasa", "#space", "#planets", "#cosmos", "#astrophotography"]
  },
  "youtube_short": null,
  "newsletter": null,
  "rights_line": "Image: NASA, ESA, and the OPAL team"
}
```

## Why this is a good result

The image credit rides along on every populated variant; facts agree across
variants and with the source; only the requested platforms are filled.
