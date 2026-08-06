# Example 01 — light travel time (Python, intro)

## Input

```
objective: "compute how long light takes to reach us from a star, given its distance"
language: python
level: intro
```

## Output

```json
{
  "title": "How Old Is the Light?",
  "language": "python",
  "problem_statement": "Implement light_travel_years(distance_ly) which returns the number of years light has been traveling to reach us from a star at the given distance in light-years. A light-year is defined as the distance light travels in one year, so the answer equals the distance numerically. Raise ValueError for negative distances.",
  "starter_code": "def light_travel_years(distance_ly):\n    # TODO: return the travel time in years; raise ValueError if distance_ly < 0\n    raise NotImplementedError\n",
  "tests": "import pytest\nfrom solution import light_travel_years\n\ndef test_happy():\n    assert light_travel_years(4.24) == pytest.approx(4.24)\n\ndef test_zero_edge():\n    assert light_travel_years(0) == 0\n\ndef test_negative_error():\n    with pytest.raises(ValueError):\n        light_travel_years(-1)\n",
  "solution": "def light_travel_years(distance_ly):\n    if distance_ly < 0:\n        raise ValueError('distance must be non-negative')\n    # A light-year is the distance light covers in a year, so years == distance.\n    return float(distance_ly)\n",
  "science_note": "Proxima Centauri is ~4.24 light-years away, so its light is ~4.24 years old when it reaches us. Distance in light-years is, by definition, the light travel time in years."
}
```

## Why this is a good result

The reference solution passes all three tests; the empty starter raises and fails
them; the science note is correct (Proxima ~4.24 ly). The problem is implementable
from the statement alone.
