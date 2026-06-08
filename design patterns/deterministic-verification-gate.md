---
id: deterministic-verification-gate
title: Deterministic verification gate
type: pattern
domains: [reliability]
status: stable
brief: "A deterministic check — static analysis, type check, schema validation, test — placed after a stochastic step to catch a class of errors with certainty."
order: 12
implements: ["[[least-model-principle]]"]
reduces: ["[[step-reliability-compounding]]"]
related_to: ["[[deterministic-agents]]"]
mitigates: ["[[model-poisoning]]"]
---

# Deterministic verification gate

A verification step implemented in deterministic code — static analysis, type checking, schema validation, a test suite — placed immediately after a stochastic step to check its output before that output propagates. Unlike a stochastic critic, a deterministic gate decides a class of errors with certainty rather than probability: a type error or a schema violation is caught every time, not most of the time. This is what lets it break the multiplicative reliability model — it removes a whole category of failures from the chain rather than contributing another sub-unity factor to it. Because it judges the output rather than the model, it catches a violation in the class it decides whether that violation came from an ordinary error, a suborned model, or a poisoned one.

Because the check is deterministic, the gate is the preferred verifier wherever the property to be checked can be expressed in code; a stochastic verifier is reserved for properties deterministic code cannot decide. Placing the gate is thus an application of the least model principle to verification, and it reduces the compounding degradation of the chain it guards.
