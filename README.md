# starlight-agent-skills

> Skill registry for Starlight agents.

> **STATUS: INCUBATING** — this repo is an intent marker. There is no registry here yet. The design below is the target, not a description of what exists today.

## Looking for usable skills today?

→ **[`frankxai/claude-skills-library`](https://github.com/frankxai/claude-skills-library)** is the live, public skill library (100+ skills, multi-runtime, spec-validated). Use that. This repo does not yet contain anything you can install.

## What this will become

An **agent-facing** skill registry for the Starlight ecosystem — distinct from `claude-skills-library`, which is human-facing and runtime-oriented:

- **Portable skill definitions** consumed by SIS and ACOS agents at runtime.
- **Registry semantics** — versioning, resolution, and dependency rules so agents can request a skill by name + version rather than copying files.
- **Substrate alignment** — skills attested against the Starlight Intelligence Protocol (SIP) and discoverable through the SIS agent layer.

The line: `claude-skills-library` is the *catalog humans browse and install from*; this repo would be the *registry agents resolve against*. Until that distinction is implemented in code, the catalog is the only real surface — use it.

## Where it sits

| Repo | Role |
|------|------|
| [`claude-skills-library`](https://github.com/frankxai/claude-skills-library) | Live public skill catalog (use this today) |
| [`Starlight-Intelligence-System`](https://github.com/frankxai/Starlight-Intelligence-System) | Substrate — agents, vaults, SIP contracts |
| [`agentic-creator-os`](https://github.com/frankxai/agentic-creator-os) | Consumes skills through Claude Code |
| **starlight-agent-skills** | This repo — agent-facing registry (target state) |

## What exists today

This README. See the Incubating tier in the SIS [`ECOSYSTEM_ARCHITECTURE.md`](https://github.com/frankxai/Starlight-Intelligence-System/blob/main/ECOSYSTEM_ARCHITECTURE.md).

## Activation criteria

This repo moves out of incubation when:

1. A registry schema exists (how a skill is named, versioned, and resolved).
2. At least one SIS/ACOS agent resolves a skill from here at runtime.
3. There is a clear, non-overlapping contract with `claude-skills-library`.

Until then, treat this as a placeholder. Install from `claude-skills-library`.
