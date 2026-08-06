# Example 01 — a Falcon 9 Starlink launch (illustrative)

## Input

```
mission: "Falcon 9, Starlink batch, [date], outcome: nominal — booster landed on
droneship. Source: provider launch webcast/press kit."
footage: "Liftoff, max-Q, stage sep, booster landing, fairing deploy."
length: 8
```

## Output

```json
{
  "titles": [
    "Falcon 9 Flies Again: Starlink Launch + Booster Landing",
    "How SpaceX Reuses a Rocket: This Starlink Mission, Explained",
    "Starlink Launch: From Liftoff to Droneship Landing"
  ],
  "script": "[0:00] Cold open on liftoff. Today, a Falcon 9 carried another batch of Starlink satellites to orbit — and brought its first stage back to land on a droneship. [0:30] Context: what Starlink is and why these batches launch so often. [2:00] The launch, beat by beat: liftoff, max-Q, stage separation, the booster's flip and landing burn, and fairing deploy. [6:00] Why reuse matters for launch cadence and cost. [7:30] Outro + subscribe.",
  "chapters": [
    { "time": "0:00", "title": "Liftoff" },
    { "time": "0:30", "title": "What is Starlink?" },
    { "time": "2:00", "title": "The launch, beat by beat" },
    { "time": "6:00", "title": "Why reusability matters" },
    { "time": "7:30", "title": "Outro" }
  ],
  "description": "A Falcon 9 launched another batch of Starlink satellites and landed its first stage on a droneship. In this video we break down the flight from liftoff to landing and explain why booster reuse drives launch cadence.\n\nChapters:\n0:00 Liftoff\n0:30 What is Starlink?\n2:00 The launch, beat by beat\n6:00 Why reusability matters\n7:30 Outro\n\nSources: provider launch webcast and press kit.",
  "tags": ["spacex", "falcon 9", "starlink", "rocket launch", "booster landing", "reusable rockets"],
  "rights_line": "Launch footage: SpaceX webcast (credit per provider terms)"
}
```

## Why this is a good result

Titles are compelling but honest (no fabricated stakes); chapters align with the
script timing; the description cites the source; footage credit is included.
Bracketed placeholders mark the facts a producer must confirm before publishing.
