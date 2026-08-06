# Example 01 — review then rewrite

## Input

```
text: "This soul-aligned system will awaken your consciousness and transform your
entire creative journey into something truly magical."
mode: review
```

## Output (review mode)

```json
{
  "mode": "review",
  "result": null,
  "flags": [
    { "span": "soul-aligned", "rule": "no spiritual/consciousness language", "fix": "name the concrete mechanism" },
    { "span": "awaken your consciousness", "rule": "no spiritual/consciousness language", "fix": "state the specific capability gained" },
    { "span": "transform your entire creative journey", "rule": "no vague transformation claims", "fix": "describe the actual before→after" },
    { "span": "truly magical", "rule": "claims must be earned/specific", "fix": "show the result; don't label it" }
  ]
}
```

## Same input, `mode: rewrite`

```json
{
  "mode": "rewrite",
  "result": "This system changes how you work: you go from manually assembling content piece by piece to running one pipeline that drafts, checks, and packages it. Same inputs, a fraction of the time.",
  "flags": []
}
```

## Why this is a good result

Every off-register phrase is flagged against the specific rule it breaks; the
rewrite is cool, premium, and specific — claims are earned, facts unchanged.
