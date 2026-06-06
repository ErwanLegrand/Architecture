---
id: scope-limiting-stateless-subagent
title: Scope limiting / stateless subagent
type: pattern
domains: [reliability, performance]
status: stable
brief: "Distribute work across subagents that each receive only their relevant context; the orchestrator synthesizes outputs and no reasoning trace is shared."
order: 23
implements: ["[[scope-limiting]]", "[[stateless-subagent]]"]
requires: ["[[orchestrator]]"]
related_to: ["[[specialist-agents]]"]
---

# Scope limiting / stateless subagent

Work is distributed across subagents, each receiving only the context relevant to its subtask; no subagent's internal reasoning trace is passed to another, and the orchestrator synthesizes the final outputs. Isolating context per subagent reduces the total tokens consumed, limits the lost-in-the-middle attention problem, and prevents the cross-agent context drift that occurs when one agent inherits another's irrelevant history.

The pattern is the structural realization of both the scope-limiting and stateless-subagent principles, and it narrows what each agent can reach for the same containment reason the specialist-agent and least-privilege concepts narrow what each agent can do.
