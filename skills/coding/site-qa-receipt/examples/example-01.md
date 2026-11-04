# Example 01 — waitlist page after a deploy

## Input

```
url: "https://frankx.ai/"
assertions: ["waitlist form present", "no console errors"]
allowed_hosts: ["frankx.ai", "www.frankx.ai"]
viewports: ["1440x900", "390x844"]
```

## Output

```json
{
  "url": "https://frankx.ai/",
  "verdict": "accept",
  "assertions": [
    { "name": "waitlist form present", "expected": true, "actual": true, "pass": true },
    { "name": "no console errors", "expected": 0, "actual": 0, "pass": true }
  ],
  "evidence_folder": "~/.starlight/evidence/frankx-home-2026-11-04",
  "evidence_files": [
    { "path": "manifest.json", "role": "manifest", "sha256": "<64 hex>" },
    { "path": "timeline.json", "role": "timeline", "sha256": "<64 hex>" },
    { "path": "screenshot-desktop.png", "role": "screenshot-desktop", "sha256": "<64 hex>" },
    { "path": "screenshot-mobile.png", "role": "screenshot-mobile", "sha256": "<64 hex>" },
    { "path": "console.json", "role": "console", "sha256": "<64 hex>" },
    { "path": "network.json", "role": "network", "sha256": "<64 hex>" },
    { "path": "assertions.json", "role": "assertions", "sha256": "<64 hex>" }
  ],
  "grader": "openai/codex (the check ran under an Anthropic model)",
  "receipt_id": null
}
```

## Why this is a good result

Both contracted assertions have results and pass, the grader is a different vendor than the
agent that ran the check, the evidence list covers every role the Kernel adapter expects, and
the receipt is honestly reported as pending rather than invented.
