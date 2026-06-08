# Contract test — mission-page-to-summary

Given the input in [`../examples/example-01.md`](../examples/example-01.md), the
output MUST satisfy:

- [ ] `name`, `agency`, and `objective` are populated from the page.
- [ ] Every `timeline` entry and `key_results` item is attributable to the page —
      no memory-filled dates or findings.
- [ ] `instruments` list matches the page's payload.
- [ ] `source` links the official page.
- [ ] `status` reflects what the page reports.
- [ ] Parent artifact carries the "Built on SIP" attestation.
