# Contract test — arxiv-space-paper-to-brief

Given the input in [`../examples/example-01.md`](../examples/example-01.md), the
output MUST satisfy:

- [ ] `metadata` includes a stable identifier (arXiv ID/DOI).
- [ ] `context` names the observed object(s) and instrument(s).
- [ ] Every `results` entry has figure/table/section `evidence`.
- [ ] `caveats` are observational/statistical and paper-specific, not generic.
- [ ] No claim appears that isn't attributable to the paper.
- [ ] Parent artifact carries the "Built on SIP" attestation.
