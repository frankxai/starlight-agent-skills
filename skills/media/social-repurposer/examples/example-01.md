# Example 01 — repurpose the APOD "Pillars of Creation" short

## Input

```
source: the apod-to-short output for "Pillars of Creation — JWST" (see
skills/cosmos/apod-to-short/examples/example-01.md)
platforms: [x, linkedin, instagram]
voice: starlight
```

## Output

```json
{
  "core_message": "Webb's infrared view of the Pillars of Creation shows star birth and erosion in the same frame, 6,500 light-years away.",
  "x_thread": [
    "These gas columns are taller than our solar system is wide. And Webb just looked straight through them. 🧵",
    "The Pillars of Creation sit in the Eagle Nebula, ~6,500 light-years away — towers of cold gas and dust.",
    "In infrared, Webb cuts through the dust and reveals what's inside: brand-new stars glowing red at the tips.",
    "The same UV light from nearby young stars that lights this scene is also slowly evaporating it. Creation and erosion, one frame.",
    "Image: NASA, ESA, CSA, STScI. More space breakdowns to come."
  ],
  "linkedin": "The Pillars of Creation are taller than our solar system is wide — and Webb just looked straight through them.\n\nIn the Eagle Nebula, ~6,500 light-years away, three towers of cold gas and dust are being lit and slowly eroded by ultraviolet light from nearby young stars. Webb's infrared eyes cut through the dust to reveal new stars forming at the tips: creation and destruction in the same frame.\n\nWhat's the most useful mental model you've found for explaining infrared astronomy to non-experts?\n\nImage: NASA, ESA, CSA, STScI",
  "instagram": {
    "caption": "Taller than our solar system is wide — and Webb saw straight through. The Pillars of Creation, 6,500 light-years away: new stars forming as the towers slowly evaporate. 🌌 Image: NASA, ESA, CSA, STScI",
    "hashtags": ["#JWST", "#PillarsOfCreation", "#astronomy", "#nasa", "#space", "#nebula", "#cosmos", "#astrophotography"]
  },
  "youtube_short": null,
  "newsletter": null,
  "rights_line": "Image: NASA, ESA, CSA, STScI"
}
```

## Why this is a good result

Every variant carries the same true facts and the full image credit; each fits
its platform; only the requested platforms are populated.
