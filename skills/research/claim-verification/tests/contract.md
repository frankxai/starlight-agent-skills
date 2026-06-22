# Contract test — claim-verification

Given the input in [`../examples/example-01.md`](../examples/example-01.md), the
output MUST satisfy:

- [ ] `verdict` is one of `supported | refuted | partially-supported | unverifiable`.
- [ ] `confidence` is calibrated to the evidence, not defaulted to `high`.
- [ ] Every entry in `evidence` has a real, located `source`.
- [ ] `rationale` explains the verdict in terms of the evidence.
- [ ] `unverifiable` is used honestly when sources are absent/insufficient.
- [ ] Parent artifact carries the "Built on SIP" attestation.
