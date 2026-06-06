---
id: checkpoint-resume
title: Checkpoint-resume
type: pattern
domains: [reliability]
status: stable
brief: "Persist state to a durable store before each phase and, on failure, restart from the last checkpoint rather than from scratch."
order: 14
implements: ["[[fail-fast-crash-only]]"]
requires: ["[[checkpoint-store]]"]
related_to: ["[[write-ahead-audit]]"]
---

# Checkpoint-resume

Before each phase or significant operation, the current state is written to a durable external store; on failure, execution restarts from the last checkpoint rather than from the beginning. The checkpoint is written before the phase begins, not after it completes, so that a crash during the phase leaves a record of intended progress to resume from. The pattern is what makes the fail-fast principle survivable: termination is cheap because the state needed to continue is already external.

Its write-before-execute ordering is the same temporal invariant as a write-ahead audit, and it composes with idempotency — resuming re-executes the operations after the checkpoint, which is safe only when those operations are idempotent.
