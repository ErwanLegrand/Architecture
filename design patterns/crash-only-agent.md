---
id: crash-only-agent
title: Crash-only agent
type: pattern
domains: [reliability]
status: stable
brief: "An agent with no cleanup or rollback logic that, on failure, terminates and resumes from the last checkpoint."
order: 15
implements: ["[[fail-fast-crash-only]]", "[[idempotency-as-design-constraint]]"]
requires: ["[[checkpoint-resume]]", "[[idempotent-tool-design]]"]
---

# Crash-only agent

An agent built with no cleanup, rollback, or partial-state-recovery logic. On any failure it terminates immediately; recovery is always to restart and resume from the last checkpoint. The design removes the entire class of defects that live in cleanup and compensation code by ensuring there is no such code to be wrong. Its cost is a precondition: every mutating operation the agent performs must be idempotent, so that resuming from a checkpoint and re-executing the operations after it produces no additional effect.

It is the structural realization of the fail-fast principle, depending on checkpoint-resume for its recovery path and on idempotent tool design for its safety. Where idempotency cannot be guaranteed, a compensating-transaction design is the alternative, at the cost of the cleanup logic this pattern removes.
