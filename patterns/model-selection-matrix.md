---
id: model-selection-matrix
title: Model selection matrix
type: pattern
domains: [performance]
status: stable
brief: "Encode the task-type-to-tier mapping as a declared policy applied at agent-creation time; default to the cheapest sufficient tier, upgrade only with justification."
order: 27
implements: ["[[right-model-for-task]]"]
requires: ["[[model-tier]]"]
related_to: ["[[least-model-principle]]"]
---

# Model selection matrix

The mapping from task type to model tier is encoded as a declared policy and applied when an agent is created, not chosen ad hoc during a session. The default is the cheapest sufficient tier; an upgrade to a more capable tier requires explicit justification recorded with the agent. The task-to-tier mapping itself is supplied by the right-model-for-task principle; this pattern is the mechanism that applies that mapping consistently and auditably across a system of agents rather than leaving it to per-invocation discretion.
