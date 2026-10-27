# Example

Illustrative data, not a live execution receipt.

## Input

Prepare the next bounded delivery from current source evidence.

## Output

```json
{
  "owner": "frankxai/starlight-agent-skills",
  "state": "review_requested",
  "evidence": {
    "base_sha": "example-base",
    "tested_sha": "example-head",
    "local_checks": "passed",
    "ci": "pending",
    "deployment": "not_applicable"
  },
  "next_action": "Inspect exact-head CI before a release decision."
}
```
