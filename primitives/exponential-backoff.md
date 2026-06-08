---
id: exponential-backoff
title: Exponential backoff
type: primitive
domains: [reliability]
status: stable
brief: "A retry-delay strategy that grows the wait geometrically with jitter to avoid synchronized retries against a recovering service."
order: 16
related_to: ["[[circuit-breaker]]"]
---

# Exponential backoff

A retry-delay strategy in which the wait before each attempt grows geometrically with the attempt number and a random jitter is added: the delay is approximately a base interval times two raised to the attempt index, plus jitter. The geometric growth gives a failing downstream service time to recover instead of being struck by immediate repeats; the jitter spreads many clients' retries across time so they do not synchronise into a thundering herd against the service as it comes back. It is the timing discipline a bounded retry policy applies between attempts.
