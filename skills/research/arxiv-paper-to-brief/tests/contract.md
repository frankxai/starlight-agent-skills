# Contract test — arxiv-paper-to-brief

Given the input in [`../examples/example-01.md`](../examples/example-01.md), the
output MUST satisfy:

- [ ] `metadata` includes a stable identifier (arXiv ID/DOI/URL).
- [ ] Every entry in `results` has non-empty `evidence` (figure/table/section).
- [ ] `limitations` contains at least one substantive, paper-specific item.
- [ ] No numeric claim appears that is not attributable to the paper.
- [ ] `citations` quote text/figures that actually exist in the source.
- [ ] Parent artifact carries the "Built on SIP" attestation.
