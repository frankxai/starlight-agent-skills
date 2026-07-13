<!-- GITHUB_VISUALS_START -->
<p align="center">
  <img src="assets/github/header.svg" alt="Starlight Agent Skills - portable skills for the Starlight ecosystem." width="100%">
</p>

<details open>
<summary><strong>How this repo works</strong></summary>
<p align="center">
  <img src="assets/github/how-it-works.svg" alt="Starlight Agent Skills operating map" width="100%">
</p>
</details>

<details>
<summary><strong>Build, deploy, verify path</strong></summary>
<p align="center">
  <img src="assets/github/build-deploy-verify.svg" alt="Starlight Agent Skills build deploy verify path" width="100%">
</p>
</details>

<!-- GITHUB_VISUALS_END -->

<div align="center">

# 🛰️ Starlight Agent Skills

### Portable capability library for AI agents

> Reusable `SKILL.md` capabilities — prompts, manifests, examples, tests, and adapters —
> for Claude Code, Codex, Cursor, Gemini, OpenCode, and the Starlight Intelligence System.

![Skills](https://img.shields.io/badge/skills-26-7fffd4?style=for-the-badge&labelColor=0d1117)
![Domains](https://img.shields.io/badge/domains-7-c084fc?style=for-the-badge&labelColor=0d1117)
[![Built on SIP](https://img.shields.io/badge/Built_on-SIP-78a6ff?style=for-the-badge&labelColor=0d1117)](https://github.com/frankxai/Starlight-Intelligence-System)
[![License: MIT](https://img.shields.io/badge/license-MIT-white?style=for-the-badge&labelColor=0d1117)](https://opensource.org/licenses/MIT)
[![validate](https://github.com/frankxai/starlight-agent-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/frankxai/starlight-agent-skills/actions/workflows/validate.yml)

[**🗂️ Catalog**](docs/CATALOG.md) · [**🧩 Architecture**](docs/ARCHITECTURE.md) · [**🗺️ Roadmap**](docs/ROADMAP.md)

</div>

> **SIS remembers. MCP connects. Skills execute. Engines produce.**
> This repo is the *execute* layer — a sibling to the Starlight Intelligence System, not a folder inside it.

---

## What's inside

**26 production-grade skills across 7 domains**, each a self-contained, rich-portable package.
Browse the full [**Catalog**](docs/CATALOG.md).

| Domain | Skills | Examples |
|--------|:------:|----------|
| 🧩 **substrate** | 4 | `agentic-income`, `affiliate-audit`, `payments-mandate`, `swarm-queen-coordination` |
| 🌌 **cosmos** (flagship) | 7 | `apod-to-short`, `nasa-image-to-atlas-page`, `rights-check-nasa-esa` |
| 🔬 research | 3 | `arxiv-paper-to-brief`, `mission-page-to-summary`, `claim-verification` |
| 🎬 media | 5 | `social-repurposer`, `thumbnail-concept`, `caption-and-hashtag` |
| 🎓 education | 3 | `explain-like-cosmic-professor`, `simulation-lab-builder` |
| 💻 coding | 1 | `cosmic-code-lab` |
| ✨ brand | 3 | `starlight-voice`, `arcanea-mythic-overlay`, `frankx-authority-post` |

The **substrate** domain holds brand-neutral operating skills (income systems, affiliate
monetization, AP2 payment safety, swarm coordination) that feed the Starlight Intelligence
System directly. The creative domains ship worked `examples/` and golden `tests/`. Frontmatter,
the `Built on SIP` footer, and each `manifest.json` are cross-checked against the folder and
`SKILL.md` in CI, so the library can't silently drift.

## The ecosystem

| Layer | Repo | Role |
|-------|------|------|
| Substrate / memory | [`Starlight-Intelligence-System`](https://github.com/frankxai/Starlight-Intelligence-System) | Vaults, retrieval, the SIP protocol |
| **Skills** | **`starlight-agent-skills`** (this repo) | **Portable capability packs** |
| Connectors | `starlight-mcp` | External tool/data senses + hands |
| Domain engine | [`starlight-cosmos-engine`](https://github.com/frankxai/starlight-cosmos-engine) | Consumes `skills/cosmos/*` |
| Operation | [`agentic-creator-os`](https://github.com/frankxai/agentic-creator-os) | Creator productivity OS |

Why separate? SIS is the operating substrate; it shouldn't become a junk drawer for every skill
pack. Keeping skills sovereign lets any consumer pull exactly what it needs, version it
independently, and compose it under SIP attestation. See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Quickstart

```bash
# Claude Code — install one skill
cp -r skills/cosmos/apod-to-short ~/.claude/skills/apod-to-short

# Other runtimes — see adapters/
#   adapters/claude.md  codex.md  cursor.md  gemini.md  opencode.md  sis.md
```

Then, in your agent: *"Turn today's APOD into a 45-second short."* The skill auto-activates from
its `description` (and from [`skill-rules.json`](skill-rules.json) in SIS/ACOS).

## Skill format (rich-portable)

```
skills/<domain>/<skill-name>/
├── SKILL.md        # REQUIRED — canonical instructions + frontmatter
├── manifest.json   # machine-readable I/O + MCP-dependency contract
├── examples/       # worked input → output
└── tests/          # golden-checklist asserting the output contract
```

`SKILL.md` is the **single source of truth** — authored once, runs everywhere. Cross-runtime
guidance lives once in [`adapters/`](adapters/), never duplicated per skill. Full contract:
[`docs/SKILL_SPEC.md`](docs/SKILL_SPEC.md).

## Orchestrators

Skills are the moves; [`agents/`](agents/) holds short **reference orchestrators** that chain
them into end-to-end plays — e.g. `cosmos-content-producer` (`apod-to-short` →
`rights-check-nasa-esa` → `space-social-repurposer` → `thumbnail-concept`). CI verifies each
orchestrator only composes skills that exist.

## Develop

```bash
make check                              # validate + example↔manifest check + catalog drift + rules (what CI runs)
python3 scripts/validate_skills.py      # frontmatter + attestation + manifest↔folder↔SKILL.md
python3 scripts/validate_examples.py    # worked example output actually matches its manifest's contract
python3 scripts/generate_catalog.py     # regenerate docs/CATALOG.md
node    scripts/check-rules.mjs          # every rule/orchestrator resolves; no name collisions
node    scripts/port-skill.mjs <domain/skill> --target=<repo> [--dry-run]
```

CI runs the validators on every push under least-privilege permissions (`contents: read`). The
port script is path-traversal-safe and refuses to write outside `--target` or to port an
un-attested skill. See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`SECURITY.md`](SECURITY.md).

## Built on SIP

Every skill carries a **Built on SIP** attestation — the protocol-level attribution that lets it
compose across the Starlight ecosystem. [`scripts/port-skill.mjs`](scripts/port-skill.mjs)
refuses to port any skill whose footer is missing. Ledger: [`ATTESTATION.md`](ATTESTATION.md).

## License

[MIT](LICENSE). Arcanea canon, where invoked inside the two mythic-overlay skills, is attributed
CC-BY-NC.
