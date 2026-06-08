---
id: wall-clock-budget
title: Wall-clock budget
type: primitive
domains: [reliability, performance]
status: stable
brief: "A declared ceiling on elapsed wall-clock time for a session, operation, or invocation, enforced by the harness — the time-domain sibling of the token and retry budgets."
order: 30
mitigates: ["[[unbounded-resource-consumption]]"]
related_to: ["[[token-budget]]", "[[termination-condition]]"]
---

# Wall-clock budget

A declared ceiling on the elapsed wall-clock time a session, operation, or single invocation may run before the harness aborts it, enforced by the orchestrator or harness rather than by the agent. It is the time-domain sibling of the token budget and retry budget: where those bound spend and attempts, the wall-clock budget bounds duration, and so catches a run that consumes neither tokens nor iterations quickly yet still fails to halt — one blocked on a slow or hanging downstream, for instance.

It is one of the terminals a complete termination condition covers, alongside iteration-limit exhaustion and budget exhaustion: the fallback that fires on elapsed time when neither the success predicate nor the other budgets do.
