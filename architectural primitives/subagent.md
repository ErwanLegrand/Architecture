---
id: subagent
title: Subagent
type: primitive
domains: [reliability, performance]
status: stable
brief: "An isolated execution unit with a bounded context, a declared tool scope, and no shared state; the unit of parallelism in multi-agent orchestration."
order: 18
related_to: ["[[specialist-agents]]", "[[orchestrator]]"]
---

# Subagent

An isolated execution unit with a bounded context window, a declared tool scope, and no state shared with other subagents. It receives a single focused input and returns a single structured output, and it is the unit of parallelism in multi-agent orchestration. A subagent is dispatched by an orchestrator, which alone holds the overall task model; the subagent sees only its assigned slice.

The subagent is the reliability and performance view of the same isolated node the specialist-agent primitive describes from the scope axis: a narrow unit whose containment is a property of the architecture, not of the agent's discretion.
