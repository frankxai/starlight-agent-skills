# Example — Operator pilot for a four-week cohort

## Input

A brand with an existing audience wants a four-week lab for people who already use AI tools at work. Frank Riemer runs it as the named operator. The cadence is dated: kickoff Monday 9 November 2026, a receipt due every Friday. Demand capture is a waitlist form. The room is Circle. Every lesson source has a rights record. The task envelope sets a token ceiling and a stop condition: halt if any fixture fails.

## Output

```json
{
  "contract_valid_curriculum": [
    {
      "id": "practice-that-remembers",
      "version": "0.1.0",
      "title": "Build a practice that remembers",
      "path": "operator",
      "module": "first-agent-win",
      "timeBudgetMinutes": 45,
      "validator": "node scripts/validate.mjs contract/schemas/lesson.schema.json lessons/practice-that-remembers.json",
      "validator_result": "ok",
      "projections": {
        "appRoute": "/academy/operator/practice-that-remembers",
        "mcpTool": "lesson_practice_that_remembers"
      }
    }
  ],
  "space_plan": {
    "visible_spaces": 12,
    "hidden_until_open": ["week-3-review", "week-4-showcase"],
    "private_spaces_gated_by": "entitlement",
    "interest_tags_grant_access": false
  },
  "staged_agents": {
    "concierge": {
      "state": "staged-not-deployed",
      "tools": [],
      "mcp_servers": [],
      "input": "room adapter, allowlisted spaces only",
      "fixtures_passed": 6,
      "fixtures_total": 6
    },
    "curator": {
      "state": "staged-not-deployed",
      "tools": [],
      "mcp_servers": [],
      "input": "room adapter, featured receipts with consent only",
      "fixtures_passed": 5,
      "fixtures_total": 5
    }
  },
  "walkthrough_evidence": {
    "account": "fresh, unentitled until invited",
    "viewports": [1280, 390],
    "steps_reached": ["invite", "onboarding", "first lesson", "first receipt"],
    "minutes_to_passing_receipt": 41,
    "confusing_words": ["'Receipt' in the onboarding email; replaced with 'proof of your work'"],
    "dead_links": 0
  },
  "evidence_receipt": {
    "contract_repo": "frankxai/starlight-community-builder",
    "contract_revision": "<exact commit sha of the revision the lessons were validated against>",
    "tests": "node --test: all passing at that revision",
    "recorded_by": "community-studio",
    "run_on_invented_fixtures_only": true
  },
  "release_decision": "Held for the operator. Publication, invites, prices and access grants are Frank's decisions; none has been made."
}
```

The example is a proposed handoff. The revision, counts and timings are illustrative values for a run that has not happened, so a real run replaces them with measured ones.
