---
id: admission-control
title: Admission control
type: pattern
domains: [security, reliability]
status: stable
brief: "Bound the work an agent accepts — rate-limit admitted requests, apply backpressure, and shed excess load — rather than only bounding what an accepted run consumes."
order: 30
requires: ["[[rate-limit]]"]
mitigates: ["[[unbounded-resource-consumption]]"]
composes_with: ["[[retry-with-backoff-and-budget]]"]
---

# Admission control

A pattern for protecting an agent or service from overload by bounding the work it accepts rather than the work it has already begun. Incoming requests pass a rate limit that admits them up to a ceiling; when demand exceeds capacity the system applies backpressure — signalling upstream callers to slow — and sheds load, rejecting or degrading excess requests rather than accepting work it cannot complete. It is the inbound counterpart to the per-run budgets: those bound what a single accepted run may consume, while admission control bounds how much work is admitted at all, which is the dimension an adversary attacks when inducing denial of service.

Admission control composes with retry with backoff and budget across the call boundary: the server sheds excess or signals backpressure, and a well-behaved caller's backoff and retry budget keep it from converting that signal into a retry storm that would defeat the limit.
