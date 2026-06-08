# Contract test — space-social-repurposer

Given the input in [`../examples/example-01.md`](../examples/example-01.md), the
output MUST satisfy:

- [ ] The image/footage credit appears on EVERY populated variant that shows the
      media (the defining behavior of this skill).
- [ ] Only the requested `platforms` are populated; others are `null`.
- [ ] `core_message` is true to the source; all variants agree with it.
- [ ] No fact appears in any variant that is absent from the source.
- [ ] Each variant fits platform norms.
- [ ] Parent artifact carries the "Built on SIP" attestation.
