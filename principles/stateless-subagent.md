---
id: stateless-subagent
title: Stateless subagent
type: principle
domains: [reliability]
status: stable
brief: "Subagents hold no persistent state across invocations; all task state is externalized, making them restartable, parallelizable, and replaceable."
order: 16
requires: ["[[shared-state-store]]"]
related_to: ["[[specialist-agents]]"]
---

# Stateless subagent

Subagents hold no persistent state across invocations. All task-relevant state is externalized before a subagent is invoked and retrieved at the start of each invocation, so a subagent's identity is irrelevant to correctness: any instance given the same input produces equivalent output for a given model. This is what makes subagents independently restartable, freely replaceable, and safe to run in parallel — there is no in-process history that one invocation accumulates and another would lack.

Statelessness requires somewhere for the state to live between invocations: a shared state store or a phase handoff carries what the subagent is not permitted to retain. The principle narrows what a subagent accumulates in the same spirit that the specialist-agent primitive narrows what it is responsible for.
