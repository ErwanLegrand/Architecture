---
id: shared-state-coordination
title: Shared state coordination
type: pattern
domains: [reliability, performance]
status: stable
brief: "Agents coordinate via an external shared state store rather than by serialization into the orchestrator's context window."
order: 25
implements: ["[[scope-limiting]]"]
requires: ["[[shared-state-store]]"]
related_to: ["[[local-mediation-design-pattern]]"]
---

# Shared state coordination

Agents coordinate through an external shared state store rather than by serializing their exchanges into the orchestrator's context window. The orchestrator reads from and writes to the store; each subagent reads its input slice and writes its output slice. Keeping coordination out of the context window holds each agent to its scope and keeps the orchestrator's own history from growing with every subagent's output.

Routing coordination through orchestrator-owned infrastructure the subagents cannot bypass is the structural analogue of local mediation, applied to inter-agent coordination rather than to tool use.
