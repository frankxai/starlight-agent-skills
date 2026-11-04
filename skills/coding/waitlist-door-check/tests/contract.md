# Contract test — waitlist-door-check

Given the input in [`../examples/example-01.md`](../examples/example-01.md), the
output MUST satisfy:

- [ ] Every checkout, billing, payment, stripe, paypal or `/pay` target appears in `not_opened` and was never requested, including via a redirect.
- [ ] A primary call to action returning 404 is ranked P0.
- [ ] The signup form's submit target and fields are reported; any test submission used only `test_email`.
- [ ] `p0_count` equals the number of P0 entries in `doors`.
- [ ] Every entry in `doors` has a one-line `fix`.
- [ ] Parent artifact carries the "Built on SIP" attestation.
