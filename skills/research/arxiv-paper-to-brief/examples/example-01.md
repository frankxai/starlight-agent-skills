# Example 01 — a retrieval-augmented generation paper

## Input

```
paper: arXiv:2005.11401  (illustrative)
audience: practitioner
depth: standard
```

## Output

```json
{
  "metadata": {
    "title": "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks",
    "authors": "Lewis et al.",
    "id": "arXiv:2005.11401",
    "date": "2020"
  },
  "problem": "Parametric language models store knowledge in weights, which is hard to update and to attribute. The paper asks whether coupling generation with a non-parametric retrieval store improves knowledge-intensive tasks.",
  "method": "RAG combines a pretrained seq2seq generator with a dense retriever over a Wikipedia index; retrieved passages condition generation, trained end-to-end.",
  "results": [
    { "claim": "State-of-the-art on several open-domain QA benchmarks", "evidence": "Results tables, §4" },
    { "claim": "More specific and factual generations than a parametric-only baseline", "evidence": "Human eval, §4" }
  ],
  "limitations": [
    "Quality bounded by the retrieval corpus and retriever recall",
    "Evaluated on a fixed Wikipedia snapshot — staleness not addressed",
    "Compute/latency overhead of retrieval not deeply analyzed"
  ],
  "why_it_matters": "For practitioners, RAG is the canonical pattern for grounding LLM output in updatable, attributable sources — directly relevant to building reliable assistants.",
  "citations": ["'we combine a pretrained retriever ... with a pretrained seq2seq model' — Abstract"]
}
```

## Why this is a good result

Results are each tied to a section; limitations are substantive (retriever
recall, corpus staleness), not boilerplate; the identifier is preserved.
