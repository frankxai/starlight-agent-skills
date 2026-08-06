# Example 01 — a heavy-lift launch (illustrative)

## Input

```
mission: "Falcon Heavy, [payload], [date], outcome: successful — side boosters
recovered. Source: provider webcast/press kit."
length: 35
voice: starlight
```

## Output

```json
{
  "hook": "Three rocket cores, 27 engines, one liftoff.",
  "script": "This is Falcon Heavy — three first-stage cores firing together, 27 engines at liftoff. Today it carried [payload] to orbit, and the two side boosters came back to land. The hard part isn't just the power. It's bringing most of the rocket home to fly again.",
  "captions": ["3 cores · 27 engines", "Liftoff", "Payload to orbit", "Side boosters land", "Built to fly again"],
  "rights_line": "Launch footage: SpaceX webcast (credit per provider terms)",
  "duration_sec": 35
}
```

## Why this is a good result

The hook uses a true, striking fact (three cores / 27 engines); narration fits 35s
at ~2.5 words/sec; outcome is sourced; footage credit is included. Bracketed
placeholders mark facts to confirm before publishing.
