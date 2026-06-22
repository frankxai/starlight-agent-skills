# 🛰️ Starlight Agent Skills — Catalog

The complete index of all **26 skills** in this library. Every skill ships as a self-contained, rich-portable package: a canonical `SKILL.md` (spec-compliant frontmatter), an optional `manifest.json`, and optional `examples/` + `tests/`. Skills run across Claude Code, Codex, Cursor, Gemini, OpenCode, and the Starlight Intelligence System — see [`adapters/`](../adapters/).

> This file is generated. After adding or renaming a skill, run `python3 scripts/generate_catalog.py` to regenerate it, then `python3 scripts/validate_skills.py` to verify compliance.

## 🧩 Substrate (income · payments · swarm)

_4 skills_

| Skill | Version | Description |
|---|---|---|
| [`affiliate-audit`](../skills/substrate/affiliate-audit) | 0.1.0 | Map which content mentions paying tools but lacks affiliate links, and which programs to join first. Use when monetizing tool-comparison content, choosing af... |
| [`agentic-income`](../skills/substrate/agentic-income) | 0.1.0 | The substrate operating brain for building income systems with AI agents. Use when planning, building, or scaling an affiliate/content/product income network... |
| [`payments-mandate`](../skills/substrate/payments-mandate) | 0.1.0 | How an agent safely handles a payment mandate — verify authorization before any settlement, hold the spend cap, fail closed on doubt, and keep a human on eve... |
| [`swarm-queen-coordination`](../skills/substrate/swarm-queen-coordination) | 0.1.0 | How a stream queen coordinates a worker swarm and runs the escalation contract that keeps money safe — queens run streams, the founder owns capital, humans h... |

## 🌌 Cosmos (flagship pack)

_7 skills_

| Skill | Version | Description |
|---|---|---|
| [`apod-to-short`](../skills/cosmos/apod-to-short) | 0.1.0 | Turn a NASA Astronomy Picture of the Day (APOD) into a 30–60s vertical short — script, shot list, captions, and a rights line. Use when the user mentions APO... |
| [`arxiv-space-paper-to-brief`](../skills/cosmos/arxiv-space-paper-to-brief) | 0.1.0 | Turn an astrophysics/space-science arXiv paper into a structured brief tuned for space audiences — adds object/mission context, instruments, and observationa... |
| [`cosmic-mythic-overlay`](../skills/cosmos/cosmic-mythic-overlay) | 0.1.0 | Layer an Arcanea-style cosmic-mythic framing over a real space object or event, keeping the astronomy intact and separable from the myth. Use when giving a n... |
| [`nasa-image-to-atlas-page`](../skills/cosmos/nasa-image-to-atlas-page) | 0.1.0 | Turn a NASA/ESA image into a structured 'cosmic atlas' web page — MDX with hero, plain-language explainer, fact table, sources, and rights. Use when building... |
| [`rights-check-nasa-esa`](../skills/cosmos/rights-check-nasa-esa) | 0.1.0 | Check usage rights for NASA/ESA/observatory space media and emit a correct attribution line. Use when reusing a space image/video, before publishing a short... |
| [`rocket-launch-to-reel`](../skills/cosmos/rocket-launch-to-reel) | 0.1.0 | Turn a rocket launch into a short vertical reel — punchy hook, 30–45s narration, beat-synced captions, and a footage-credit line. Use when making a launch re... |
| [`space-social-repurposer`](../skills/cosmos/space-social-repurposer) | 0.1.0 | Repurpose a space asset (APOD short, mission brief, launch reel, atlas page) into a coordinated multi-platform pack, preserving image/footage credits across... |

## 🔬 Research

_3 skills_

| Skill | Version | Description |
|---|---|---|
| [`arxiv-paper-to-brief`](../skills/research/arxiv-paper-to-brief) | 0.1.0 | Turn an arXiv (or any research) paper into a structured, citation-faithful brief — problem, method, results, limitations, and why it matters. Use when summar... |
| [`claim-verification`](../skills/research/claim-verification) | 0.1.0 | Fact-check a claim against sources and return a verdict with evidence and confidence — supported, refuted, partially-supported, or unverifiable. Use when ask... |
| [`mission-page-to-summary`](../skills/research/mission-page-to-summary) | 0.1.0 | Turn an official mission page (NASA/ESA/JPL spacecraft, instrument, or mission site) into a clean, accurate summary — objective, timeline, instruments, statu... |

## 🎬 Media

_5 skills_

| Skill | Version | Description |
|---|---|---|
| [`caption-and-hashtag`](../skills/media/caption-and-hashtag) | 0.1.0 | Write a platform-tuned caption plus a researched, non-spammy hashtag set for a post. Use when finishing a social post, asked for 'caption and hashtags', or o... |
| [`nasa-image-to-short`](../skills/media/nasa-image-to-short) | 0.1.0 | Turn any NASA/ESA still image (not just APOD) into a vertical short package — hook, narration, captions, shot list, rights line. Use when making a space shor... |
| [`rocket-launch-to-youtube`](../skills/media/rocket-launch-to-youtube) | 0.1.0 | Turn a rocket launch (mission details + footage notes) into a full YouTube package — title options, description, chapters, tags, and a long-form script. Use... |
| [`social-repurposer`](../skills/media/social-repurposer) | 0.1.0 | Repurpose one source asset (article, video, paper brief, image) into a platform-tailored social pack — X thread, LinkedIn post, Instagram caption, YouTube sh... |
| [`thumbnail-concept`](../skills/media/thumbnail-concept) | 0.1.0 | Generate high-CTR thumbnail concepts for a video — layout, focal subject, text overlay (≤4 words), color/contrast, and an image-gen prompt. Use when designin... |

## 🎓 Education

_3 skills_

| Skill | Version | Description |
|---|---|---|
| [`coding-challenge-generator`](../skills/education/coding-challenge-generator) | 0.1.0 | Generate a graded set of coding challenges around a topic — progressive difficulty, each with statement, constraints, hidden tests, and solution. Use when bu... |
| [`explain-like-cosmic-professor`](../skills/education/explain-like-cosmic-professor) | 0.1.0 | Explain any concept in the voice of a warm, rigorous cosmic professor — an analogy ladder from intuitive to precise, with a check-for-understanding. Use when... |
| [`simulation-lab-builder`](../skills/education/simulation-lab-builder) | 0.1.0 | Design an interactive simulation lab — a self-contained HTML/JS (or p5.js) sim with tunable parameters, a learning goal, and guided experiments. Use when bui... |

## 💻 Coding

_1 skill_

| Skill | Version | Description |
|---|---|---|
| [`cosmic-code-lab`](../skills/coding/cosmic-code-lab) | 0.1.0 | Generate a runnable, space-themed coding lab — a problem statement, starter code, hidden tests, and a worked solution — in Python or JavaScript. Use when cre... |

## ✨ Brand & Voice

_3 skills_

| Skill | Version | Description |
|---|---|---|
| [`arcanea-mythic-overlay`](../skills/brand/arcanea-mythic-overlay) | 0.1.0 | Add an Arcanea mythic overlay to factual content — a canon-attributed narrative framing (Guardian/Luminor names, mythic register) layered over the real facts... |
| [`frankx-authority-post`](../skills/brand/frankx-authority-post) | 0.1.0 | Write a FrankX authority post — an AI-Architect-voiced LinkedIn/X post that leads with a result, teaches one concrete lesson, and stays humble. Use when draf... |
| [`starlight-voice`](../skills/brand/starlight-voice) | 0.1.0 | Apply the Starlight voice to any text — cool, premium, high-intellect, direct, technical, warm, playful; pattern recognition as poetry. Use when writing or r... |
