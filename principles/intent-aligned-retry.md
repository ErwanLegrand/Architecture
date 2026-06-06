---
id: intent-aligned-retry
title: Intent-aligned retry
type: principle
domains: [reliability]
status: stable
brief: "Retry boundaries align to the intent unit, not the step unit; safe-to-retry is declared per operation, not inferred from transport."
order: 14
requires: ["[[idempotency-key]]", "[[retry-budget]]", "[[exponential-backoff]]"]
related_to: ["[[observable-failure]]"]
---

# Intent-aligned retry

Retry boundaries must align to the unit of intent, not the unit of mechanism. A read with no side effect is safe to retry unconditionally; a state-changing operation is not safe to retry unless it carries an idempotency key that lets the receiver recognise the repeat. Retrying the wrong unit produces duplicate side effects — a second order, a second payment — which are harder to detect and reverse than the original failure they were meant to mask.

Whether an operation is safe to retry is therefore a property the operation must declare explicitly, per operation. It cannot be inferred from the transport — an HTTP method, a status code — or assumed globally for all tools, because the same transport carries both safe and unsafe operations. Retrying correctly also requires knowing that the operation failed, which depends on the failure being observable in the first place.
