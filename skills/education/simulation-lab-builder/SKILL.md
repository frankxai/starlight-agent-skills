---
name: simulation-lab-builder
description: "Design an interactive simulation lab — a self-contained HTML/JS (or p5.js) sim with tunable parameters, a learning goal, and guided experiments. Use when building an interactive demo, a physics/astronomy sandbox, or a 'simulation' / 'interactive lab' for teaching."
version: 0.1.0
domain: education
tags: [simulation, interactive, lab, physics, p5js]
---

# Simulation Lab Builder

> A learning goal → a runnable interactive simulation with guided experiments.

## Purpose

Some concepts only click when you can *play* with them (orbits, gravity, wave
interference, scale). This skill produces a self-contained interactive simulation
— parameters the learner can tune, plus a short set of guided experiments that
lead to the intended insight — runnable from a single HTML file.

## When it fires

- Keyword triggers: `simulation`, `interactive lab`, `sandbox`, `interactive demo`,
  `visualize this`
- File triggers: `sims/**`, `*.sim.html`
- Command triggers: `/simulation-lab-builder`

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| `goal` | yes | The insight the sim should produce. |
| `params` | no | Variables to expose as sliders/inputs. |
| `stack` | no | `p5js` (default) or `vanilla` HTML/Canvas. |

## Workflow

1. **State the insight** — the one thing a learner should walk away understanding.
   ✅ Check: the sim can actually demonstrate it.
2. **Model** — the minimal correct model (equations/rules) that produces the
   behavior. Keep physics honest within stated simplifications.
3. **Build the sim** — single-file HTML/JS (or p5.js sketch) with tunable
   controls and clear rendering.
4. **Guided experiments** — 2–4 prompts ("set gravity to 0 — what happens?") that
   surface the insight.
5. **Self-check** — the sim runs without errors; controls visibly affect behavior.

## Output contract

```json
{
  "goal": "string",
  "model_notes": "string — equations/rules + simplifications",
  "code": "string — single-file HTML/JS or p5.js sketch",
  "experiments": ["string — guided prompts"],
  "stack": "p5js | vanilla"
}
```

## Tools & MCP

- Tools: `Write`, `Bash`/browser to smoke-test. MCP: none required.

## Quality bar

- [ ] Runs from a single file without external build steps.
- [ ] Model is physically honest within its stated simplifications.
- [ ] Controls measurably change the simulation.
- [ ] Experiments lead to the stated insight.

## Example

Input: goal "show how orbital speed changes with distance" → a p5.js two-body sim
with a distance slider and three guided experiments.

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
