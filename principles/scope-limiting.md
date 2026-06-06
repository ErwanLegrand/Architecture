---
id: scope-limiting
title: Scope limiting
type: principle
domains: [performance, reliability]
status: stable
brief: "Each agent receives only the context slice its task requires; no subagent's reasoning trace is visible to another."
order: 17
requires: ["[[orchestrator]]"]
composes_with: ["[[least-privilege-principle]]"]
---

# Scope limiting

Each agent receives only the context its specific task requires. No subagent's internal reasoning trace is exposed to another subagent; the orchestrator synthesizes the outputs. Limiting scope reduces the tokens consumed per invocation, mitigates the degraded attention that models show toward content in the middle of a long context, and contains the drift that accumulates when an agent carries history irrelevant to its task.

Scope limiting is the context-bounding counterpart of least privilege's authority-bounding. Least privilege bounds what an agent may *do*; scope limiting bounds what an agent may *see*. The two compose along orthogonal axes: a compromised or drifting agent is contained both in the authority it can exercise and in the information it can reach.
