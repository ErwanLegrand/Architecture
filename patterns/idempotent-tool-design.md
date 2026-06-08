---
id: idempotent-tool-design
title: Idempotent tool design
type: pattern
domains: [reliability]
status: stable
brief: "Every state-mutating tool takes a stable idempotency key and treats a repeated key as a no-op that returns the original result."
order: 16
implements: ["[[idempotency-as-design-constraint]]", "[[intent-aligned-retry]]"]
requires: ["[[idempotency-key]]"]
related_to: ["[[provenance-tracking-design-pattern]]"]
---

# Idempotent tool design

Every tool that mutates external state takes an idempotency key as a required parameter and treats a repeated key as a no-op that returns the original result rather than performing the effect again. The key is stable across retries because it is derived from the identity of the task or operation, not generated fresh on each call, so a retry, a restart, or a replay carries the same key as the original attempt and the receiver recognises it. The pattern is how the idempotency invariant is realised at the tool boundary, and it is the precondition that makes retry and crash-only restart safe.

It is the operational complement of provenance tracking: provenance records where a value originated, while the idempotency key ensures that acting on that origin more than once is indistinguishable from acting on it once.
