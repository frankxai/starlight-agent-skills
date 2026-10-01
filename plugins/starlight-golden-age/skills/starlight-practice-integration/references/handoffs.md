# Brain and agent handoffs

## State flow
Preparation → authorized practice outside AI control (optional) → return → participant-selected reflection → action draft → optional separately consented memory → review.

Any stage can stop. Visualization can stand alone. An incomplete session does not lose the participant's right to rest or decline.

## Logical roles
These are roles for an orchestrator, not a claim that several agents are running.

| Role | Receives | Produces | Boundary |
|---|---|---|---|
| Integration guide | Participant's chosen detail | Reflection/action draft | No external action |
| Evidence reviewer | Scientific claim and source | Supported/uncertain/unsupported assessment | No journal access needed |
| Visual creator | Approved scene brief | Requested image or prompt | No raw session history |
| Action builder | Approved action, budget, acceptance | Small draft artifact | No escalation to publication |
| Memory adapter | Approved selected summary and destination | Receipt or honest failure | No unapproved mirrors |

Use one conversational agent for a simple session. Delegate only where the requested task and available runtime justify it. The Brain owns task routing and priority, not what a vision means. A symbolic mentor is not an authorized tool actor.

## Action card
Fields: chosen action; artifact type; who benefits; cue; obstacle; maximum minutes; completion evidence; permission scope. Example: “Draft a one-page accessible garden-workshop plan; when tomorrow's first work block begins; limit 20 minutes; done when the plan states materials, access needs and one question for participants.”

## Local preview helper
When `scripts/session_bridge.py` is available, pass a synthetic or participant-approved session JSON to its `preview` subcommand. It validates readiness, builds an action-only agent envelope and optionally projects a minimal SIS memory record after exact consent checks. It never saves or dispatches. The runtime is a contract proof; language-model guidance and clinical safety are not proven by passing its tests.

Session fields and an executable synthetic example live in `references/session-example.json`. The helper deliberately does not accept free-form health or journal fields. Keep them out of agent handoffs. Do not use preview as an emergency triage system: it only checks explicit state fields.

## Follow-through
Review the chosen action at the participant's requested time. Ask what happened, what got in the way and what to keep or change. No automatic seven-day streak, no penalty for rest. Instructor pilots measure returned action reports and usability; they do not establish medical efficacy.
