---
id: least-model-principle
title: Least Model principle
type: principle
domains: [security, reliability]
status: stable
brief: "Minimize model-mediated decision-making in both extent and authority, across all classes of learned models."
order: 5
composes_with: ["[[least-privilege-principle]]"]
mitigates: ["[[model-poisoning]]"]
---

# Least Model principle

The use of model-mediated decision-making is minimized in both extent and authority. Each component is implemented in deterministic code unless probabilistic inference is genuinely required, and each model invocation is given the narrowest scope sufficient to perform its task. The principle applies to all classes of learned models — language models, vision-language models, embedding models, classifiers, speech-to-text, generative image and audio models, and others — because every model invocation is an attack surface that deterministic code does not have.

The principle composes with least privilege along an orthogonal axis: where least privilege bounds authority per component, least model bounds the number of components that have probabilistic agency at all. Every place a model is used is a place where attacker-controlled input can influence behavior in ways deterministic code would not permit; the specific attack mechanism differs by model class (prompt injection for LLMs and VLMs, adversarial examples for classifiers and vision models, embedding manipulation for retrieval, adversarial audio for speech-to-text), but the structural argument is identical. The same reduction shrinks exposure to a poisoned model: a decision made in deterministic code cannot be subverted by a backdoor in weights that are never invoked.

The principle has a reliability face as well as a security one. Every stochastic node is also a source of non-determinism and failure — it is slower, costlier, and less predictable than the deterministic code it replaces, and it contributes a sub-unity factor to the system's compounding reliability. Minimizing model-mediated decision-making therefore lowers the system's aggregate failure rate for the same structural reason it lowers its attack surface: a deterministic implementation, where one suffices, is at once the safer and the more reliable choice.
