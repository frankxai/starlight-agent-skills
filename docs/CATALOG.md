# 🛰️ Starlight Agent Skills — Catalog

The complete index of all **22 skills** in this library. Every skill ships as a self-contained, rich-portable package: a canonical `SKILL.md` (spec-compliant frontmatter), an optional `manifest.json`, and optional `examples/` + `tests/`. Skills run across Claude Code, Codex, Cursor, Gemini, OpenCode, and the Starlight Intelligence System — see [`adapters/`](../adapters/).

> This file is generated. After adding or renaming a skill, run `python3 scripts/generate_catalog.py` to regenerate it, then `python3 scripts/validate_skills.py` to verify compliance.

## 🌌 Cosmos (flagship pack)

_7 skills_

| Skill | Version | Description |
|---|---|---|
| [`apod-to-short`](skills/cosmos/apod-to-short) | 0.1.0 | Turn a NASA Astronomy Picture of the Day (APOD) into a 30â60s vertical short â script, shot list, captions, and a rights line. Use when the user mentions... |
| [`arxiv-space-paper-to-brief`](skills/cosmos/arxiv-space-paper-to-brief) | 0.1.0 | Turn an astrophysics/space-science arXiv paper into a structured brief tuned for space audiences â adds object/mission context, instruments, and observatio... |
| [`cosmic-mythic-overlay`](skills/cosmos/cosmic-mythic-overlay) | 0.1.0 | Layer an Arcanea-style cosmic-mythic framing over a real space object or event, keeping the astronomy intact and separable from the myth. Use when giving a n... |
| [`nasa-image-to-atlas-page`](skills/cosmos/nasa-image-to-atlas-page) | 0.1.0 | Turn a NASA/ESA image into a structured 'cosmic atlas' web page â MDX with hero, plain-language explainer, fact table, sources, and rights. Use when buildi... |
| [`rights-check-nasa-esa`](skills/cosmos/rights-check-nasa-esa) | 0.1.0 | Check usage rights for NASA/ESA/observatory space media and emit a correct attribution line. Use when reusing a space image/video, before publishing a short... |
| [`rocket-launch-to-reel`](skills/cosmos/rocket-launch-to-reel) | 0.1.0 | Turn a rocket launch into a short vertical reel â punchy hook, 30â45s narration, beat-synced captions, and a footage-credit line. Use when making a launc... |
| [`space-social-repurposer`](skills/cosmos/space-social-repurposer) | 0.1.0 | Repurpose a space asset (APOD short, mission brief, launch reel, atlas page) into a coordinated multi-platform pack, preserving image/footage credits across... |

## 🔬 Research

_3 skills_

| Skill | Version | Description |
|---|---|---|
| [`arxiv-paper-to-brief`](skills/research/arxiv-paper-to-brief) | 0.1.0 | Turn an arXiv (or any research) paper into a structured, citation-faithful brief â problem, method, results, limitations, and why it matters. Use when summ... |
| [`claim-verification`](skills/research/claim-verification) | 0.1.0 | Fact-check a claim against sources and return a verdict with evidence and confidence â supported, refuted, partially-supported, or unverifiable. Use when a... |
| [`mission-page-to-summary`](skills/research/mission-page-to-summary) | 0.1.0 | Turn an official mission page (NASA/ESA/JPL spacecraft, instrument, or mission site) into a clean, accurate summary â objective, timeline, instruments, sta... |

## 🎬 Media

_5 skills_

| Skill | Version | Description |
|---|---|---|
| [`caption-and-hashtag`](skills/media/caption-and-hashtag) | 0.1.0 | Write a platform-tuned caption plus a researched, non-spammy hashtag set for a post. Use when finishing a social post, asked for 'caption and hashtags', or o... |
| [`nasa-image-to-short`](skills/media/nasa-image-to-short) | 0.1.0 | Turn any NASA/ESA still image (not just APOD) into a vertical short package â hook, narration, captions, shot list, rights line. Use when making a space sh... |
| [`rocket-launch-to-youtube`](skills/media/rocket-launch-to-youtube) | 0.1.0 | Turn a rocket launch (mission details + footage notes) into a full YouTube package â title options, description, chapters, tags, and a long-form script. Us... |
| [`social-repurposer`](skills/media/social-repurposer) | 0.1.0 | Repurpose one source asset (article, video, paper brief, image) into a platform-tailored social pack â X thread, LinkedIn post, Instagram caption, YouTube... |
| [`thumbnail-concept`](skills/media/thumbnail-concept) | 0.1.0 | Generate high-CTR thumbnail concepts for a video â layout, focal subject, text overlay (â¤4 words), color/contrast, and an image-gen prompt. Use when desi... |

## 🎓 Education

_3 skills_

| Skill | Version | Description |
|---|---|---|
| [`coding-challenge-generator`](skills/education/coding-challenge-generator) | 0.1.0 | Generate a graded set of coding challenges around a topic â progressive difficulty, each with statement, constraints, hidden tests, and solution. Use when... |
| [`explain-like-cosmic-professor`](skills/education/explain-like-cosmic-professor) | 0.1.0 | Explain any concept in the voice of a warm, rigorous cosmic professor â an analogy ladder from intuitive to precise, with a check-for-understanding. Use wh... |
| [`simulation-lab-builder`](skills/education/simulation-lab-builder) | 0.1.0 | Design an interactive simulation lab â a self-contained HTML/JS (or p5.js) sim with tunable parameters, a learning goal, and guided experiments. Use when b... |

## 💻 Coding

_1 skill_

| Skill | Version | Description |
|---|---|---|
| [`cosmic-code-lab`](skills/coding/cosmic-code-lab) | 0.1.0 | Generate a runnable, space-themed coding lab â a problem statement, starter code, hidden tests, and a worked solution â in Python or JavaScript. Use when... |

## ✨ Brand & Voice

_3 skills_

| Skill | Version | Description |
|---|---|---|
| [`arcanea-mythic-overlay`](skills/brand/arcanea-mythic-overlay) | 0.1.0 | Add an Arcanea mythic overlay to factual content â a canon-attributed narrative framing (Guardian/Luminor names, mythic register) layered over the real fac... |
| [`frankx-authority-post`](skills/brand/frankx-authority-post) | 0.1.0 | Write a FrankX authority post â an AI-Architect-voiced LinkedIn/X post that leads with a result, teaches one concrete lesson, and stays humble. Use when dr... |
| [`starlight-voice`](skills/brand/starlight-voice) | 0.1.0 | Apply the Starlight voice to any text â cool, premium, high-intellect, direct, technical, warm, playful; pattern recognition as poetry. Use when writing or... |
