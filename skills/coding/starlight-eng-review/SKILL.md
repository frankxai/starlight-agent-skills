---
name: starlight-eng-review
description: "Engineering Architecture review. Stress-test data models, concurrency boundaries, network failure modes, state atomicity, and memory limits."
version: 1.0.0
domain: coding
tags: [engineering, architecture, stress-test, failure-modes, data-model]
---

# Starlight Engineering Review — Architectural Stress-Tester

> Ruthlessly evaluate technical designs before implementation. Find bugs in the architecture before they become bugs in production.

## Review Pillars

1. **State Atomicity & Concurrency:**
   - Are file writes atomic (temp file + rename)?
   - Can concurrent agents corrupt shared state?
   - Are mutations idempotent and recoverable on crash?
2. **Failure Modes & Error Paths:**
   - What happens when external APIs timeout or return 429/500?
   - Are error messages actionable, pinpointing the exact remediation?
3. **Resource & Memory Guardrails:**
   - Does this keep process count bounded?
   - Are buffers capped to prevent out-of-memory errors?

---

Built on SIP — Starlight Intelligence Protocol  
Vertical: starlight-agent-skills · autonomous capability layer
