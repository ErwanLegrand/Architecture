---
id: byzantine-model-design-pattern
title: Byzantine model design pattern
type: pattern
domains: [security]
status: stable
brief: "Treats every model invocation as a Byzantine component capable of arbitrary adversarial behavior; trust is established only through external mechanisms."
order: 1
implements: ["[[suborned-model-principle]]"]
mitigates: ["[[model-poisoning]]"]
---

# Byzantine model design pattern

The design response that follows from the suborned model principle. Every model invocation is treated as a Byzantine component in the sense of distributed systems: capable of arbitrary, adversarial behavior, including coordinated misbehavior with other components. Trust in any model output is established only through mechanisms external to the model itself.

In practice:

- **Output validation.** Model outputs are parsed, type-checked, and policy-checked by deterministic code before any action is taken.
- **Independent verification.** Where stakes warrant, a model's output is checked by a separate model instance or a deterministic verifier with no shared context, applying the BFT principle that no single Byzantine node should determine an outcome.
- **Externally bounded authority.** Each model invocation operates within a sandbox whose boundary is unaffected by what the model produces; the model cannot widen its own authority by emitting tokens.
- **Mutual suspicion between agents.** In multi-agent systems, agent B treats agent A's output as adversarial input, not as a trusted upstream signal.

The pattern is modeled on classical Byzantine fault tolerance, with the substantive difference that the assumed adversarial fraction is one: every model invocation is treated as Byzantine by default, not merely some bounded subset. Because the assumption is unconditional, the pattern contains a poisoned or backdoored model exactly as it contains a suborned one: the boundary validates every output regardless of why the model might misbehave.

**Scope.** The pattern's *structure* — treat output as adversarial, validate externally, derive trust through mechanisms outside the model — applies to every model class, not only language models. The *specifics* of validation differ by class: JSON schema and policy checks for LLM output; confidence thresholds and consistency checks across independent models for classifiers; bounded use (never as control-flow input, only as retrieval ranking) for embeddings; transcript sanitization and bounded interpretation for speech-to-text. In every case, the deterministic boundary downstream of the model is where the pattern is implemented.
