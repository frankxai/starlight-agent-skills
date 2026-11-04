# Contract test — site-qa-receipt

Given the input in [`../examples/example-01.md`](../examples/example-01.md), the
output MUST satisfy:

- [ ] No checkout, billing, payment, stripe, paypal or `/pay` path was loaded, including via a redirect.
- [ ] Every assertion named in the input has an entry in `assertions`; any `pass: false` makes `verdict` reject.
- [ ] `url` and every URL inside the evidence keep only origin and path.
- [ ] No cookie, `authorization` or `set-cookie` value appears in any evidence file.
- [ ] `grader` names a different vendor than the agent that ran the check.
- [ ] `receipt_id` is a real Kernel receipt id or `null`, never a placeholder.
- [ ] Parent artifact carries the "Built on SIP" attestation.
