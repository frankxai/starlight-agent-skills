# Example

Illustrative data, not a live execution receipt.

## Input

Prepare the next bounded delivery from current source evidence.

## Output

```json
{
  "work": [
    {
      "source": "paperclip",
      "id": "task-22",
      "declared_state": "done",
      "verification": "not_evaluated"
    }
  ],
  "decisions": [
    {
      "source": "paperclip",
      "id": "decision-4",
      "owner": "user",
      "state": "pending"
    }
  ],
  "packets": [],
  "capability_gaps": [
    "No admitted agent/repository mapping; prepare scope and acceptance criteria first."
  ]
}
```
