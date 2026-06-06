---
id: no-agency-without-auditability-principle
title: No agency without auditability principle
type: principle
domains: [security]
status: stable
brief: "No agent invocation may cause a state change without first committing a forensically sufficient record of that invocation."
order: 6
composes_with: ["[[byzantine-model-design-pattern]]"]
---

# No agency without auditability principle

No agent invocation may cause a state change in the system or its environment unless the framework has first committed a forensically sufficient record of that invocation. The principle applies to every agent in the orchestration graph — stochastic agents of any model class and deterministic agents alike.

For stochastic agents, the record must capture:

- The model's input as the model saw it (byte-for-byte, including system prompt and prompt template for LLMs, raw image bytes for vision models, raw audio for speech-to-text, and so on for other classes; including any tool outputs, retrieved content, or prior-turn context that was assembled into the input).
- The model's output verbatim, pre-parsing and pre-validation.
- The action the framework took, distinguished from what the model produced.
- The policy decision that authorized the action.
- The causal lineage linking this invocation to its triggers and downstream effects.
- The model identity and version, including sampling parameters and any class-specific configuration (prompt template version for LLMs, decoding strategy, temperature, embedding model dimension, classifier threshold, etc.).

For deterministic agents, the record must capture the input, output, side effects, code version (commit hash or equivalent), and any sources of declared nondeterminism (clock readings, RNG seed). The schema differs from the stochastic case but the reconstructability standard is the same.

The record must be written through a path outside the agent's authority, to storage the agent cannot modify. Audit is treated as part of the trust kernel of the framework, not as observability tooling: it is the detection layer of defense in depth, complementing the preventive controls implied by the Byzantine model design pattern.
