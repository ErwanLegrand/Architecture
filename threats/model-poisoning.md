---
id: model-poisoning
title: Model poisoning
type: threat
domains: [security]
status: stable
brief: "The model itself is compromised — a backdoor baked in by a poisoned training process, or weights tampered with or substituted in the supply chain — so it behaves adversarially independently of its input."
order: 6
related_to: ["[[data-poisoning]]", "[[suborned-model-principle]]"]
---

# Model poisoning

A failure mode in which the model itself is compromised, so that it behaves adversarially independently of its input — through a poisoned training or fine-tuning process that embeds a backdoor (the training-time form of data poisoning), or through tampering with or substitution of the deployed weights somewhere in the supply chain. Unlike a *suborned* model, which is an ordinary model induced to misbehave by adversarial input at inference time, a poisoned model is adversarial by construction: it may behave correctly on all ordinary inputs and betray its backdoor only on a trigger known to the attacker.

It is one concrete realization of the worst case the [suborned model principle](/principles/suborned-model-principle.md) already assumes — that on every invocation the model may be aligned with an adversary — so the framework's behavioral containment, treating every output as Byzantine, validating it with deterministic code, and minimizing where models are used at all, applies to a poisoned model unchanged. What poisoning adds is an attack stage *before* inference, which containment can detect but not prevent: a backdoor that fires only on a rare trigger may pass every output check it happens to face. Verifying a model's identity and weight integrity at load closes the tampering-and-substitution path; it cannot, however, vouch for how a correctly-delivered model was trained, so it complements rather than replaces behavioral containment.
