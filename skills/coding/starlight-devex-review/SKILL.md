---
name: starlight-devex-review
description: "Developer Experience (DevEx) & Usability Review. Optimizes API ergonomics, CLI usability, error message actionability, and reduces time-to-hello-world."
version: 1.0.0
domain: coding
tags: [devex, ergonomics, cli, api-design, usability, documentation]
---

# Starlight DevEx Review — Usability & Ergonomics Gate

> Eliminate developer friction. Optimize API simplicity, refine CLI flags, and ensure every error message teaches the user how to succeed.

## Review Pillars

1. **Time-to-Hello-World (<60 seconds):**
   - Can a user run `npx @starlight-intelligence/...` and achieve their first win in one command?
   - Are configuration defaults sensible and auto-detecting?
2. **API & CLI Ergonomics:**
   - Are flag names intuitive (e.g. `--query`, `--limit`, `--dir`)?
   - Are function signatures predictable with TypeScript types?
3. **Actionable Error Messages:**
   - Bad: `"Error: Connection failed."`
   - Good: `"Error: Could not reach vault at /path. Run 'starlight-memory wire' to initialize."`

---

Built on SIP — Starlight Intelligence Protocol  
Vertical: starlight-agent-skills · autonomous capability layer
