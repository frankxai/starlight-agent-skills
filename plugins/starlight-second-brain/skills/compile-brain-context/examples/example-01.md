# Synthetic example

## Input

Compile the current project context for a fresh agent session. Selected source: fixture:source-one, revision r1.

## Output

```json
{
  "context_pack": {
    "status": "proposal",
    "source": "fixture:source-one"
  },
  "coverage": [
    {
      "source": "fixture:source-one",
      "status": "inspected",
      "note": "Synthetic example; no live access asserted."
    }
  ],
  "next_action": {
    "status": "proposal",
    "source": "fixture:source-one"
  },
  "evidence": [
    {
      "source": "fixture:source-one",
      "status": "inspected",
      "note": "Synthetic example; no live access asserted."
    }
  ]
}
```
