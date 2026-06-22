# Example 01 — "Why Webb sees what Hubble can't"

## Input

```
topic: "Why Webb sees what Hubble can't"
subject: "the same nebula in Hubble (visible) vs Webb (infrared)"
count: 3
```

## Output

```json
{
  "concepts": [
    {
      "layout": "Split-screen: left half visible-light nebula (dustier), right half infrared (stars revealed); thin dividing line down center",
      "overlay_text": "SEE THROUGH DUST",
      "color_logic": "Cool blues (left) vs warm golds (right) for instant contrast",
      "emotional_read": "Curiosity — the reveal of hidden detail",
      "image_prompt": "Diptych of a star-forming nebula: left in visible light with obscuring dust, right in infrared revealing stars behind the dust, clean vertical split, high contrast, no text"
    },
    {
      "layout": "Single infrared nebula filling the frame, one bright newborn star circled",
      "overlay_text": "HIDDEN STARS",
      "color_logic": "Deep background, single high-contrast highlight on the circled star",
      "emotional_read": "Discovery",
      "image_prompt": "Infrared view of a nebula with newborn stars glowing through dust, one star emphasized, dark background, high contrast, no text"
    },
    {
      "layout": "Two telescopes silhouetted lower-third, their 'views' projected above as visible vs infrared",
      "overlay_text": "HUBBLE VS WEBB",
      "color_logic": "Neutral silhouettes; the two projected views carry the color contrast",
      "emotional_read": "Comparison / stakes",
      "image_prompt": "Two space telescope silhouettes at bottom, each projecting a different rendering of the same nebula above, visible vs infrared, high contrast, no text"
    }
  ]
}
```

## Why this is a good result

Each overlay is ≤4 words and legible at small size; concepts match the real
content (visible vs infrared); image prompts request "no text" so the overlay is
added in edit; using real agency imagery would trigger the rights step.
