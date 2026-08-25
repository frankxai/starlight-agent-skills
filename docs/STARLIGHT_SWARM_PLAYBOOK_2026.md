# The Starlight Swarm Playbook (2026 Edition)
## The Sovereign Operating System for 1-Person Unicorns & Autonomous Engineering Swarms

> *"When marginal execution cost drops to zero, the only remaining bottlenecks are judgment, taste, architecture, and memory."*

---

## 1. Executive Philosophy: The 1-Person Unicorn

The traditional software organization required product managers, engineering directors, QA leads, design critics, and devops engineers.

With **Starlight Intelligence System (SIS)**, a single founder commands a coordinated, adversarial swarm of specialized agents that execute with the quality, rigor, and velocity of a 50-person elite engineering team.

```
                     ┌──────────────────────────────────────┐
                     │            FOUNDER / CEO             │
                     │    (Vision, Judgment, Sovereignty)   │
                     └──────────────────┬───────────────────┘
                                        │
             ┌──────────────────────────┴──────────────────────────┐
             │                                                     │
┌────────────▼────────────┐                               ┌────────▼────────────┐
│   4-STAGE AUTOPLAN      │                               │   SOVEREIGN MEMORY  │
│ • CEO "Boil the Lake"   │                               │ • Embedded PGLite   │
│ • Eng Architecture Gate │                               │ • AST Symbol Graph  │
│ • Design & Taste Gate   │                               │ • Git Cross-Machine │
│ • DevEx Ergonomics Gate │                               │ • Zero Cloud Daemon │
└────────────┬────────────┘                               └────────┬────────────┘
             │                                                     │
             └──────────────────────────┬──────────────────────────┘
                                        │
                     ┌──────────────────▼───────────────────┐
                     │      EXECUTION & VERIFICATION        │
                     │ • Atomic Commits   • 100% Test Pass  │
                     │ • Centralized CDP  • Anti-Slop UI    │
                     └──────────────────────────────────────┘
```

---

## 2. Pillar I: The 4-Stage Adversarial Review Swarm

Most AI coding agents generate code on first instinct. The result is shallow: missing edge cases, generic styling, brittle data models, and unhandled failure paths.

**Never write code without running the 4-Stage Review Swarm:**

### Stage 1: CEO & Founder Review (`/starlight-ceo-review`)
- **The Completeness Principle ("Boil the Lake"):** In legacy software, teams cut scope to save developer hours. With AI, a 150-line complete feature takes minutes. Always build the full lake: 100% test coverage, comprehensive error recovery, responsive breakpoints, polished micro-interactions.
- **Dual-Scale Effort Scoring:** Evaluate every feature in both *Human Team Time* (e.g. 2 weeks) and *Agent Time* (e.g. 20 minutes).
- **Sovereignty & BYOK:** Zero multi-tenant server liability. The customer runs the agent runtime with their own private keys.

### Stage 2: Engineering Architecture Review (`/starlight-eng-review`)
- **Failure Paths & Error Recovery:** What happens when an external API times out or returns 429?
- **State Atomicity & Concurrency:** Are file writes atomic (write to temp file then rename)?
- **Memory & Resource Caps:** Keep process counts bounded and memory buffers capped to prevent OOM errors.

### Stage 3: Design & Taste Review (`/starlight-design-review`)
- **Zero AI Slop:** No default browser fonts, generic Tailwind gradients, or un-grained flat containers.
- **Calibrated Typography Pairings:** Inter/Geist, Outfit/Plus Jakarta Sans, Space Grotesk/Instrument Serif.
- **Component States:** Every button and card must have defined hover, active, focus, loading, and error states.
- **Responsive Viewports:** Verified across mobile (375px), tablet (768px), and desktop (1440px).

### Stage 4: Developer Experience Review (`/starlight-devex-review`)
- **Time-to-Hello-World (<60 seconds):** One-command setups (`npx ...`).
- **Actionable Error Messages:** Bad: `"Error: Failed"`. Good: `"Error: Could not reach vault. Run 'starlight-memory wire' to initialize."`

---

## 3. Pillar II: Sovereign Local Memory & Symbol Graph

Large language models suffer from session amnesia. Cloud vector databases add recurring subscriptions, latency, and privacy risks.

**The Starlight Solution:**
1. **Embedded PGLite Vector Database:** Runs WASM PostgreSQL with `pgvector` directly inside the Node.js/agent process. Zero Docker containers, zero cloud accounts, sub-millisecond cosine similarity recall.
2. **AST Code Symbol Graph (`code_def`, `code_refs`, `code_callers`):** Parses syntax trees to find exact function declarations, interfaces, types, and call hierarchies across the workspace without guessing with regex.
3. **Git-Backed Federated Sync:** Memory atoms are stored as human-readable markdown files committed to private git repositories, syncing seamlessly across machines.

---

## 4. Pillar III: Harness Integration Guide

### Claude Code Setup
Add to your project's `.claude/config.json` or `~/.claude/skills/`:
```bash
# Clone and symlink skills
git clone https://github.com/frankxai/starlight-agent-skills.git ~/.starlight-agent-skills
cp -r ~/.starlight-agent-skills/skills/coding/starlight-* ~/.claude/skills/
```

### Cursor & Windsurf Setup
Add to `.cursorrules` or `.windsurfrules`:
```markdown
# Starlight Swarm Rules
- Before writing code for any complex task, execute the 4-Stage Review Protocol:
  1. CEO Strategy Review (Boil the Lake)
  2. Engineering Architecture Review (Failure modes & atomicity)
  3. Design Taste Review (Anti-Slop typography & states)
  4. DevEx Usability Review (Ergonomics & <60s time-to-hello-world)
- Always verify changes with automated unit tests before reporting completion.
```

### Antigravity & OpenClaw MCP Setup
Add to `mcp_servers`:
```json
{
  "starlight-memory": {
    "command": "node",
    "args": ["path/to/starlight-memory/bin/starlight-memory.mjs", "mcp", "serve"]
  }
}
```

---

## 5. Summary of Core Commands

| Command | Harness | Purpose |
|---|---|---|
| `/starlight-autoplan` | Any | Full 4-Stage Adversarial Review Swarm |
| `/starlight-spec` | Any | 5-Phase PRD & Task Decomposition Engine |
| `/starlight-investigate` | Any | Evidence-driven root-cause debugging |
| `/starlight-ship` | Any | Clean commits, test verification, and landing gate |
| `/starlight-qa` | Any | Autonomous dogfooding via CDP Multiplexer Hub |
| `starlight-memory code-def <sym>` | CLI/MCP | AST Symbol Definition Lookup |
| `starlight-memory code-callers <sym>` | CLI/MCP | AST Call-Graph Caller Tracing |
| `starlight-memory vector-recall <q>` | CLI/MCP | In-Process PGLite Vector Similarity Recall |

---

*Starlight Intelligence Protocol (SIP) · Sovereign Agent Infrastructure for Builders*
