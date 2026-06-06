---
id: orchestrator
title: Orchestrator
type: primitive
domains: [reliability, performance]
status: stable
brief: "The coordinating agent that decomposes goals, dispatches subagents, manages shared state, synthesizes outputs, and evaluates termination."
order: 19
requires: ["[[shared-state-store]]"]
related_to: ["[[core-agents]]"]
---

# Orchestrator

The coordinating agent that decomposes a goal into sub-tasks, dispatches them to subagents, manages the shared state, synthesizes the subagents' structured outputs, and evaluates the termination condition. The orchestrator holds the task model; each subagent holds only its slice, and the orchestrator never exposes one subagent's internal trace to another.

It occupies the same coordinating position that the Core-agent primitive holds in the trust hierarchy, with the reliability and performance concerns of output synthesis and resource management added to the security concern of never being exposed to untrusted data.
