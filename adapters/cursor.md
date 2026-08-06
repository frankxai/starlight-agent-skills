# Cursor

Cursor uses project rules in `.cursor/rules/*.mdc`. Convert a skill by mapping
its frontmatter to a rule header.

## Convert

Create `.cursor/rules/<skill-name>.mdc`:

```mdc
---
description: <copy the skill's description>
globs: <file_patterns from skill-rules.json, comma-separated>
alwaysApply: false
---

<paste the body of SKILL.md here>
```

- `globs` drives Cursor auto-attach — reuse the `file_patterns` for this skill in
  [`../skill-rules.json`](../skill-rules.json).
- Set `alwaysApply: true` only for repo-wide brand/voice skills.

## Notes

Keep the output contract and "Built on SIP" footer intact in the rule body.
