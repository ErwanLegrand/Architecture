---
id: retry-with-backoff-and-budget
title: Retry with backoff and budget
type: pattern
domains: [reliability]
status: stable
brief: "A retry policy combining exponential backoff with jitter, a bounded attempt count, a circuit breaker, and a per-turn retry budget."
order: 17
implements: ["[[intent-aligned-retry]]"]
requires: ["[[exponential-backoff]]", "[[retry-budget]]", "[[circuit-breaker]]", "[[idempotent-tool-design]]"]
---

# Retry with backoff and budget

A policy for retrying failed tool calls that combines four mechanisms: exponential backoff with jitter between attempts, a bounded per-call attempt count, a circuit breaker that opens after persistent failure, and a per-turn retry budget that caps aggregate retry cost. Only failures a retry can plausibly resolve are retried — transient transport errors, timeouts, and downstream unavailability — while semantic failures such as a rejected or unauthorized request are not, because repeating them cannot succeed.

The policy realises intent-aligned retry and is safe only when the retried operations are idempotent; its circuit breaker surfaces persistent failure as an observable signal rather than masking it. It composes the backoff, retry-budget, and circuit-breaker primitives over the idempotent-tool-design pattern beneath it.
