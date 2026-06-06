---
id: iteration-limit
title: Iteration limit
type: primitive
domains: [reliability]
status: stable
brief: "A hard, externally enforced ceiling on loop iterations, set by the loop infrastructure rather than the agent."
order: 11
related_to: ["[[termination-condition]]"]
---

# Iteration limit

A hard maximum on the number of times an agent loop may iterate, enforced by the loop infrastructure rather than by the agent. It is the fallback terminal that fires when the loop's success condition is never satisfied: when the limit is reached the loop halts and escalates rather than continuing. Because it is external to the agent, it bounds even an agent that has lost the ability to recognise its own lack of progress.

The iteration limit is one mechanism by which explicit termination is realised; it is meaningful only alongside a termination condition that defines the success terminal.
