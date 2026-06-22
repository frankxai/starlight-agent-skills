# Reference Orchestrators

Skills are the moves; **orchestrators** are short plays that chain them into an
end-to-end result. These are *reference* compositions — they show how a consuming
system (an agent, ACOS, or `starlight-cosmos-engine`) wires the skills together.
They are not a runtime or a framework; each is a documented pipeline you can hand
to any agent.

| Orchestrator | Chains | Outcome |
|--------------|--------|---------|
| [`cosmos-content-producer`](cosmos-content-producer/AGENT.md) | `apod-to-short` → `rights-check-nasa-esa` → `space-social-repurposer` → `thumbnail-concept` | One NASA image → a rights-cleared short + a multi-platform launch pack |
| [`research-digest`](research-digest/AGENT.md) | `arxiv-paper-to-brief` → `claim-verification` → `frankx-authority-post` | One paper → a verified brief + an authority post |

Each orchestrator carries the `Built on SIP` attestation and only composes skills
that already exist in [`../skills/`](../skills/).
