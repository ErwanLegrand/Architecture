---
id: explicit-termination
title: Explicit termination
type: principle
domains: [reliability]
status: stable
brief: "Every agent loop must have a declared, mechanically verifiable termination condition enforced by the loop infrastructure, not the agent's judgement."
order: 13
requires: ["[[iteration-limit]]", "[[termination-condition]]"]
mitigates: ["[[unbounded-resource-consumption]]"]
related_to: ["[[no-agency-without-auditability-principle]]"]
---

# Explicit termination

Every agent loop must declare a termination condition that the loop infrastructure can evaluate mechanically. A loop whose stopping condition is delegated to the agent's own judgement is a liability: a single misconfiguration can produce a run that consumes unbounded resources and never halts. The maximum iteration count is therefore not optional, and it is enforced outside the agent — by the harness that runs the loop — so that an agent which fails to recognise its own completion is still stopped.

A termination condition must cover both terminals. A predicate that recognises only success is incomplete: the loop must also halt on iteration-limit exhaustion, budget exhaustion, or an explicit stop signal, and report which terminal it reached. An agent that never terminates never produces a closed record of its work, so explicit termination is also a precondition for auditability.
