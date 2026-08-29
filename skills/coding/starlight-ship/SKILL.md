---
name: starlight-ship
description: "Prepare an authorized change for review or landing by checking repository state, required gates, secrets, diff scope, deployment evidence, rollback, and merge policy. Use when a branch or pull request is ready for a release decision; never rewrite, merge, deploy, or publish without the authority granted for that action."
metadata: {"version": "0.1.0", "domain": "coding", "tags": ["release", "git", "pull-request", "verification", "rollback", "deployment"]}
---

# Starlight Ship

## Purpose

Turn “the code seems done” into a reproducible release decision while preserving unrelated work and repository governance.

## When it fires

- A change is ready to commit, push, open for review, merge, or deploy.
- The user asks for release, landing, PR, or Git/Vercel operations.
- A stale or failing PR needs evidence-based disposition.

## Inputs

- Repository instructions, branch policy, and required checks.
- Exact diff, test results, review findings, deployment state, and rollback path.
- User authority for commit, push, merge, production, publication, and cleanup.

## Workflow

1. Verify path, repository root, origin, branch, and working-tree ownership.
2. Inspect the complete diff and exclude unrelated user changes.
3. Run proportionate tests, lint/type gates, secret scan, and diff checks.
4. Use a preview deployment for web changes when the repository supports it.
5. Record independent review findings and resolve blockers.
6. Confirm mergeability, required checks, release notes, rollback, and post-merge monitoring.
7. Execute only the authorized Git or deployment action; never force-push or rewrite shared history by default.

## Output contract

Return revision, diff scope, gates and results, review status, preview/production state, known limitations, rollback, action taken, and remaining human decisions.

## Tools & MCP

Use non-interactive Git, the repository’s CI, secret scanner, and hosting connector. Preserve dirty worktrees, avoid destructive reset/checkout commands, and stop session-owned servers.

## Quality bar

- “Green” means required gates passed on the exact head revision.
- Skipped or unavailable checks are explicit.
- A successful preview is not called a production release.
- Merge or deployment follows branch protection and human authority.

## Example

Input: “Land PR 21 if it is ready.”

Good output: verify the exact head, required CI and security reviews, run release smoke tests against the preview, resolve comments, merge using repository policy, verify production, and retain a rollback revision.

---

Built on SIP — Starlight Intelligence Protocol
Vertical: starlight-agent-skills · portable capability layer
