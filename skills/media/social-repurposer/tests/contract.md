# Contract test — social-repurposer

Given the input in [`../examples/example-01.md`](../examples/example-01.md), the
output MUST satisfy:

- [ ] Only the requested `platforms` are populated; others are `null`.
- [ ] `core_message` is true to the source; every variant agrees with it.
- [ ] No statistic/fact appears in any variant that is absent from the source.
- [ ] Each variant respects platform norms (X posts terse; LinkedIn 120–200 words;
      IG caption + hashtags).
- [ ] `rights_line` from the source asset is carried into the variants that show
      the image.
- [ ] Parent artifact carries the "Built on SIP" attestation.
