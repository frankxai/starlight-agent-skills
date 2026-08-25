---
name: starlight-ship
description: "Pre-landing quality gate, commit squashing, verification suite runner, and clean landing workflow for agent development branches."
version: 1.0.0
domain: coding
tags: [ship, landing, git-ops, verify, squash, quality-gate]
---

# Starlight Ship — Pre-Landing & Clean Commit Gate

> Verify the complete build, run unit tests, clean WIP commits into crisp conventional commits, and prepare for landing.

## Pre-Flight Checklist

1. **Verify Automated Tests:** Run `npm test` or the repository verification command.
2. **Lint & Typecheck:** Run `npm run lint` / `tsc --noEmit`.
3. **Secret Scan:** Ensure zero API keys, tokens, or private credentials are in git staging.
4. **Clean Commit History:** Squash intermediate `WIP:` commits into clean, semantic commit messages (`feat: ...`, `fix: ...`, `chore: ...`).
5. **Report Outcome:** State what shipped, verification proofs, and post-ship steps.

---

Built on SIP — Starlight Intelligence Protocol  
Vertical: starlight-agent-skills · autonomous capability layer
