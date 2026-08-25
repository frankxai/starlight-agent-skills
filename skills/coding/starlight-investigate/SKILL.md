---
name: starlight-investigate
description: "Systematic root-cause debugging without speculative trial-and-error. Formulates hypotheses, collects deterministic evidence, isolates failure boundaries, and verifies fixes."
version: 1.0.0
domain: coding
tags: [investigate, debugging, root-cause, diagnostic, quality-gate]
---

# Starlight Investigate — Systematic Root-Cause Debugger

> Stop speculative trial-and-error. Formulate hypotheses, isolate the minimal reproducible failure, patch the root cause, and verify regression boundaries.

## Purpose

When bugs occur, novice agents thrash: randomly editing code, changing unrelated imports, or adding speculative null-checks. `starlight-investigate` forces an evidence-driven scientific debugging protocol:

1. **Step 1: Reproduce & Capture Evidence** — Formulate the exact command or test case that fails deterministically.
2. **Step 2: Isolate the Boundary** — Trace the call stack to the precise function, line number, and variable state where the expectation deviates from reality.
3. **Step 3: Formulate & Test Hypotheses** — State the root cause in one sentence before proposing edits.
4. **Step 4: Minimal Root-Cause Patch** — Apply the smallest possible fix that addresses the structural cause.
5. **Step 5: Regression Test & Verification** — Re-run the reproduction command to prove the fix works, then run the full test suite to guarantee zero regressions.

---

Built on SIP — Starlight Intelligence Protocol  
Vertical: starlight-agent-skills · autonomous capability layer
