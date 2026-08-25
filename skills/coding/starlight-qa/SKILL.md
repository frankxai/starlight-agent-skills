---
name: starlight-qa
description: "Autonomous Web QA, user-flow testing, responsive layout audit, and visual dogfooding via the Centralized CDP Multiplexer Hub."
version: 1.0.0
domain: coding
tags: [qa, testing, dogfooding, cdp-hub, visual-audit, responsive]
---

# Starlight QA — Autonomous Web Dogfooding & Layout Audit

> Test web applications end-to-end, verify responsive viewports, capture console errors, and dogfood real user flows without spawning rogue browser instances.

## Architecture: Centralized CDP Multiplexer Hub (Rule 6 Compliance)

In strict accordance with the Starlight Swarm Rules, agents never launch separate local browser binaries (`playwright.launch()`). All browser interactions connect to the central CDP Multiplexer Hub:

- **WebSocket Endpoint:** `http://localhost:9223/wsEndpoint`
- **Dashboard:** `http://localhost:9223`
- **Usage:**
  ```javascript
  const wsEndpoint = await fetch('http://localhost:9223/wsEndpoint').then(r => r.text());
  const browser = await chromium.connect({ wsEndpoint });
  ```

## QA Testing Protocol

1. **Page Load & Health:** Navigate to the target URL; assert title, HTTP 200, zero console errors, zero failed network requests.
2. **Interactive User Flows:** Test signup, checkout, filters, modal dialogs, and form validation states.
3. **Responsive Layouts:** Capture visual snapshots across viewports:
   - Mobile: 375x812 (iPhone)
   - Tablet: 768x1024 (iPad)
   - Desktop: 1440x900
4. **Visual Diffing & Proof:** Generate before/after diffs and capture annotated screenshots of defects.

---

Built on SIP — Starlight Intelligence Protocol  
Vertical: starlight-agent-skills · autonomous capability layer
