---
name: starlight-devex-review
description: "Review an API, CLI, SDK, plugin, package, or installation flow for discoverability, safe defaults, actionable errors, compatibility, documentation, and time to verified value. Use before publishing a developer-facing interface or when onboarding friction is suspected."
metadata: {"version":"0.1.0","domain":"coding","tags":"devex,api,cli,plugin,documentation,onboarding"}
---

# Starlight DevEx Review

## Purpose

Make the correct path easy to discover, safe to execute, and simple to verify without hiding prerequisites or host-specific limits.

## When it fires

- A public API, CLI, package, plugin, schema, or install guide changes.
- Users must cross authentication, marketplace, configuration, or runtime boundaries.
- Errors or setup steps are causing support load.

## Inputs

- Intended user and first successful outcome.
- Supported environments, prerequisites, permissions, and version policy.
- Interface definitions, examples, error messages, and telemetry/support evidence.

## Workflow

1. Trace discovery through install, configure, first action, verification, update, and removal.
2. Test commands and examples in a supported environment.
3. Check names, types, defaults, help text, and error remediation.
4. Make host-specific approval, authentication, and compatibility steps explicit.
5. Review versioning, deprecation, migration, rollback, and support ownership.
6. Measure time and steps to verified value; report the observed context rather than a universal target.

## Output contract

Return journey map, observed setup time, friction points, API/CLI findings, error-quality findings, compatibility/versioning findings, documentation gaps, prioritized fixes, and verification commands.

## Tools & MCP

Use the actual package, API schema, CLI help, and official runtime documentation. Do not claim one-click installation when review, OAuth, admin consent, or manual verification remains.

## Quality bar

- Every documented command is copyable and scoped to a supported runtime.
- Errors state what failed, where, and the safest next action.
- Removal and rollback are documented alongside installation.
- Current limitations are visible before a user invests time.

## Example

Input: “Review our cross-runtime plugin install.”

Good output: distinguish native marketplace install, local package install, staged adapter, and generic MCP connection; verify each path independently; and label unverified hosts honestly.

---

Built on SIP — Starlight Intelligence Protocol
Vertical: starlight-agent-skills · portable capability layer
