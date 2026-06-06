---
id: checkpoint-store
title: Checkpoint store
type: primitive
domains: [reliability]
status: stable
brief: "External, durable, agent-independent storage for task-critical state, written before each phase so any instance can resume."
order: 13
related_to: ["[[write-ahead-audit]]"]
---

# Checkpoint store

External, durable, agent-independent storage for task-critical state. A checkpoint is written before the operation it protects begins, so the record of intended progress precedes the work itself; on failure, any instance of the agent can load the checkpoint and resume from it. The store is the substrate that makes crash-only design and stateless restart possible, because it holds the state that process memory deliberately does not.

Its write-before-execute discipline is structurally the same mechanism as a write-ahead audit log, applied for a different purpose: the audit log writes the record before the action to guarantee forensic completeness, while the checkpoint store writes state before the phase to guarantee recoverability.
