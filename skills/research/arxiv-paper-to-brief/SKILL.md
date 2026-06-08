---
name: arxiv-paper-to-brief
description: "Turn an arXiv (or any research) paper into a structured, citation-faithful brief — problem, method, results, limitations, and why it matters. Use when summarizing a paper, building a literature digest, or asked to 'explain this paper' / 'TL;DR this arxiv link'."
version: 0.1.0
domain: research
tags: [arxiv, research, summary, brief, literature]
---

# arXiv Paper → Brief

> A research paper → a structured brief a busy expert can trust.

## Purpose

Researchers and builders need to triage papers fast without losing rigor. This
skill produces a structured brief that separates what the paper *claims* from
what it *shows*, surfaces limitations honestly, and keeps every assertion tied to
the source — so the reader can decide whether to go deeper.

## When it fires

- Keyword triggers: `arxiv`, `paper`, `summarize this paper`, `TL;DR`,
  `literature`, `research brief`
- File triggers: `*.pdf`, `papers/**`, `*.bib`
- Command triggers: `/arxiv-paper-to-brief`

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| `paper` | yes | arXiv URL/ID, PDF, or pasted text. |
| `audience` | no | `expert` (default), `practitioner`, or `general`. |
| `depth` | no | `tldr`, `standard` (default), or `deep`. |

## Workflow

1. **Extract metadata** — title, authors, venue/date, arXiv ID. ✅ Check: stable
   identifier captured.
2. **State the problem** — what gap the paper addresses, in one paragraph.
3. **Summarize the method** — the actual approach, faithfully; name the key idea.
4. **Report results** — headline numbers/claims, each tied to a figure/table/section.
   Distinguish *claimed* from *demonstrated*.
5. **List limitations** — stated and evident (data, baselines, scope). Be candid.
6. **Why it matters** — implications for the reader's audience; what to do next.
7. **Pull citations** — exact quotes/figures the brief relies on, with locations.

## Output contract

```json
{
  "metadata": { "title": "string", "authors": "string", "id": "string", "date": "string" },
  "problem": "string",
  "method": "string",
  "results": [{ "claim": "string", "evidence": "string — figure/table/section" }],
  "limitations": ["string"],
  "why_it_matters": "string",
  "citations": ["string — quote/figure + location"]
}
```

## Tools & MCP

- Tools: `WebFetch` (arXiv abstract/HTML), `Read` (PDF/text).
- MCP dependencies: optional docs/library MCP for related-work resolution.

## Quality bar

- [ ] Every result is tied to a specific figure/table/section.
- [ ] Claimed vs. demonstrated is explicitly distinguished.
- [ ] Limitations are honest, not perfunctory.
- [ ] No fabricated numbers or citations; identifier is correct.

## Example

See [`examples/example-01.md`](examples/example-01.md).

---

Built on SIP — Starlight Intelligence Protocol
Substrate: starlightintelligence.org/protocol v1.1.0
Layers used: [file-contract, attestation, sovereignty]
Vertical: starlight-agent-skills · portable capability layer
