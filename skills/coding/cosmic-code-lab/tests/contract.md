# Contract test — cosmic-code-lab

Given the input in [`../examples/example-01.md`](../examples/example-01.md), the
output MUST satisfy:

- [ ] `solution` passes every test in `tests`.
- [ ] The `starter_code` (unmodified) fails the tests.
- [ ] `tests` includes a happy-path, an edge case, and an error case.
- [ ] `problem_statement` fully specifies inputs, outputs, and error behavior.
- [ ] `science_note` is factually correct.
- [ ] Parent artifact carries the "Built on SIP" attestation.

Manual run:
```bash
# write solution.py from `solution`, test_lab.py from `tests`
pytest -q   # expect: all pass
# then replace solution.py body with `starter_code`
pytest -q   # expect: failures / NotImplementedError
```
