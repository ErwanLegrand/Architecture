---
id: fail-fast-crash-only
title: Fail fast / crash only
type: principle
domains: [reliability]
status: stable
brief: "A component that cannot guarantee clean recovery terminates immediately and restarts from the last checkpoint; no partial-state cleanup logic."
order: 11
requires: ["[[checkpoint-store]]"]
depends_on: ["[[idempotency-as-design-constraint]]"]
---

# Fail fast / crash only

A component that cannot guarantee a clean recovery terminates immediately rather than attempting partial cleanup. Task-critical state lives in an external checkpoint store, never solely in process memory, so the only recovery path is to stop and restart from the last checkpoint. This eliminates the class of defects that arise from partial-state cleanup and compensation logic: there is no cleanup logic to be wrong, because there is no in-process state worth salvaging.

State externalization is the precondition for the design, not an optimization layered on top of it. A crash-only component is correct only if every mutating operation it performed before the crash is safe to repeat on restart; the principle is therefore inseparable from idempotency as a design constraint. Where state cannot be cleanly externalized and re-execution cannot be made safe, a compensating-transaction (saga) design is the alternative — valid, but reintroducing the cleanup logic this principle exists to remove.
