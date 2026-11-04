# Example 01 — launch page with a dead primary button

## Input

```
url: "https://example.org/launch"
test_email: "waitlist-test@example.org"
```

## Output

```json
{
  "page": "https://example.org/launch",
  "doors": [
    { "severity": "P0", "label": "Join the waitlist", "target": "/join", "result": "404", "fix": "Point the button at /waitlist, which serves the form." },
    { "severity": "P0", "label": "Buy now", "target": "/checkout", "result": "not opened: refused path on a product with no passed release gate", "fix": "Replace Buy now with the waitlist call to action until the gate passes." },
    { "severity": "P1", "label": "Waitlist form", "target": "/api/signup", "result": "accepted the test address but sent no product id", "fix": "Send the product id with every signup." },
    { "severity": "P2", "label": "Docs", "target": "/docs", "result": "404", "fix": "Link the docs page that exists or remove the link." }
  ],
  "p0_count": 2,
  "not_opened": ["/checkout"]
}
```

## Why this is a good result

The dead primary button is found and ranked first, the checkout door is reported without being
requested, the form is checked with the owner's test address only, and every finding has a
one-line fix.
