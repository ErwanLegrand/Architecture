---
id: idempotency-key
title: Idempotency key
type: primitive
domains: [reliability]
status: stable
brief: "A stable identifier derived from an operation's intent that lets a receiver detect and de-duplicate re-submissions."
order: 14
---

# Idempotency key

A stable, unique identifier derived from the intent of an operation rather than generated fresh on each attempt. The receiving service records the key on first execution and, on any later submission carrying the same key, returns the original result instead of repeating the effect. The key shape must be consistent across every tool that mutates state; a system in which some mutating tools carry keys and others do not cannot guarantee safe retry, because the keyless tools remain duplication hazards. It is the mechanism through which idempotency — and therefore safe retry and safe restart — is realised.
