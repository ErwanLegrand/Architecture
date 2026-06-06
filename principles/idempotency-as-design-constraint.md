---
id: idempotency-as-design-constraint
title: Idempotency as a design constraint
type: principle
domains: [reliability]
status: stable
brief: "Every mutating operation must be idempotent by design; under retries, restarts, and replays any non-idempotent operation eventually executes more than once."
order: 15
requires: ["[[idempotency-key]]"]
related_to: ["[[provenance-tracking-design-pattern]]"]
---

# Idempotency as a design constraint

Every mutating operation in the system must be idempotent by design. Agents are retried, restarted from checkpoints, and replayed; under these conditions any operation that is not idempotent will eventually execute more than once, and the duplicate execution is a defect that surfaces far from its cause. Idempotency is therefore an architectural invariant, not a per-operation optimization: a system in which some mutating tools are idempotent and others are not is a latent failure mode, because the unsafe tools are indistinguishable from the safe ones until a retry exposes them.

An idempotency key, derived from the identity of the operation rather than generated fresh per attempt, is the primary mechanism. The constraint is what makes safe restart possible: a crash-only component can resume from a checkpoint only if re-running the operations after that checkpoint is guaranteed to have no additional effect. It is the reliability complement of provenance — provenance establishes where an action originated, idempotency guarantees that re-executing that origin is safe.
