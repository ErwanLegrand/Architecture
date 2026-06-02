---
id: replay-able-invocation-records
title: Replay-able invocation records
type: pattern
domains: [security]
status: stable
implements: ["[[no-agency-without-auditability-principle]]"]
---

# Replay-able invocation records

Capture enough state — model identity and version, sampling parameters, full input as the model saw it, and any class-specific configuration (prompt template version for LLMs, decoding parameters, embedding dimension, classifier threshold) — that any invocation can be deterministically re-executed from its log entry for forensic analysis or debugging. For deterministic agents, the analog is capturing input, code version, and declared nondeterminism sources. This is the [no agency without auditability principle](/security%20principles/no-agency-without-auditability-principle.md)'s reconstructability standard made concrete — a record is forensically sufficient only if the invocation it describes can be re-executed from it alone.
