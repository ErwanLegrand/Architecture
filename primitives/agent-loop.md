---
id: agent-loop
title: Agent loop
type: primitive
domains: [reliability]
status: stable
brief: "The core execution cycle — perceive, reason, act, observe, update state — repeated until a termination condition is met."
order: 10
requires: ["[[termination-condition]]"]
---

# Agent loop

The core execution cycle of every agentic component: perceive the current state, reason about it, act, observe the result, update state, and repeat until a termination condition is satisfied. All agentic behaviour runs inside a loop of this shape, whether the loop is explicit in orchestration code or implicit in a model's turn-by-turn generation. It is the unit to which iteration limits, budgets, and termination conditions attach.

A loop without a termination condition is not a complete agent loop but a runaway; the termination condition is a required partner of the loop, not an optional addition to it.
