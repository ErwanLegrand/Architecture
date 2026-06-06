---
id: hierarchical-task-decomposition
title: Hierarchical task decomposition
type: pattern
domains: [reliability, performance]
status: stable
brief: "A root orchestrator decomposes a goal into independent sub-tasks, routes each to a specialist subagent, and synthesizes the outputs."
order: 21
implements: ["[[scope-limiting]]"]
requires: ["[[orchestrator]]", "[[subagent]]"]
related_to: ["[[role-typed-agent-separation-design-pattern]]"]
---

# Hierarchical task decomposition

A root orchestrator decomposes a complex goal into sub-tasks that are as independent as possible, routes each to a specialized subagent that sees only its own sub-task, and synthesizes the structured outputs into the final result. Keeping the sub-tasks independent lets them run in parallel and keeps each subagent's context small, while the orchestrator alone holds the whole goal.

It is the reliability and performance form of role-typed agent separation: the same single-function decomposition, without the Core/Edge/Bridge trust-position constraints the security pattern layers on top.
