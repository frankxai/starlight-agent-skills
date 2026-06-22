# Contract test — nasa-image-to-short

Given the input in [`../examples/example-01.md`](../examples/example-01.md), the
output MUST satisfy:

- [ ] All six fields present (`hook`, `script`, `captions`, `shot_list`,
      `rights_line`, `duration_sec`).
- [ ] Every fact in `script` traces to the caption — no invented numbers.
- [ ] `rights_line` reproduces the credit verbatim; non-NASA parties preserved.
- [ ] `script` word count ≈ `duration_sec` × 2.5 (±15%).
- [ ] Parent artifact carries the "Built on SIP" attestation.
