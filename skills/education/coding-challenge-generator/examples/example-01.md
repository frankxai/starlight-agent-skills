# Example 01 — recursion (Python, 3 of 5 shown)

## Input

```
topic: "recursion"
language: python
count: 5
range: "intro→advanced"
```

## Output (first three rungs)

```json
{
  "topic": "recursion",
  "challenges": [
    {
      "title": "Factorial",
      "difficulty": "intro",
      "statement": "Implement factorial(n) recursively for n >= 0. factorial(0) == 1. Raise ValueError for n < 0.",
      "starter_code": "def factorial(n):\n    # TODO: recursive implementation\n    raise NotImplementedError\n",
      "tests": "import pytest\nfrom solution import factorial\n\ndef test_base(): assert factorial(0) == 1\ndef test_happy(): assert factorial(5) == 120\ndef test_negative():\n    with pytest.raises(ValueError): factorial(-1)\n",
      "solution": "def factorial(n):\n    if n < 0: raise ValueError('n must be >= 0')\n    return 1 if n == 0 else n * factorial(n - 1)\n"
    },
    {
      "title": "Sum a Nested List",
      "difficulty": "easy",
      "statement": "Implement deep_sum(items) returning the sum of all integers in a possibly-nested list of ints.",
      "starter_code": "def deep_sum(items):\n    raise NotImplementedError\n",
      "tests": "from solution import deep_sum\n\ndef test_flat(): assert deep_sum([1,2,3]) == 6\ndef test_nested(): assert deep_sum([1,[2,[3,4]],5]) == 15\ndef test_empty(): assert deep_sum([]) == 0\n",
      "solution": "def deep_sum(items):\n    total = 0\n    for x in items:\n        total += deep_sum(x) if isinstance(x, list) else x\n    return total\n"
    },
    {
      "title": "Binary Tree Height",
      "difficulty": "medium",
      "statement": "Given a binary tree as nested tuples (value, left, right) or None, return its height (a single node has height 1; None has height 0).",
      "starter_code": "def height(node):\n    raise NotImplementedError\n",
      "tests": "from solution import height\n\ndef test_none(): assert height(None) == 0\ndef test_single(): assert height((1, None, None)) == 1\ndef test_unbalanced(): assert height((1, (2, (3, None, None), None), None)) == 3\n",
      "solution": "def height(node):\n    if node is None: return 0\n    _, left, right = node\n    return 1 + max(height(left), height(right))\n"
    }
  ]
}
```

## Why this is a good result

Difficulty rises (intro → easy → medium → …); each solution passes its tests and
each empty starter fails; statements are implementable from text alone.
