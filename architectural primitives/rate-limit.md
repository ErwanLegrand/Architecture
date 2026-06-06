---
id: rate-limit
title: Rate limit
type: primitive
domains: [security, reliability]
status: stable
brief: "A ceiling on the rate at which requests are admitted over a time window, enforced ahead of saturation rather than after failure like the circuit breaker."
order: 31
mitigates: ["[[unbounded-resource-consumption]]"]
related_to: ["[[circuit-breaker]]"]
---

# Rate limit

A ceiling on the rate at which requests or operations are admitted over a time window, enforced by the harness or a gateway in front of an agent or tool rather than by the caller. Where the circuit breaker reacts to a downstream that is already failing, the rate limit acts before saturation: it bounds the volume of work admitted per unit time, so that neither a runaway caller nor an adversary issuing a flood can drive consumption past the capacity the system was provisioned for. Work in excess of the ceiling is rejected or queued rather than served.
