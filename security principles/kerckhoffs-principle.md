---
id: kerckhoffs-principle
title: Kerckhoffs's principle
type: principle
domains: [security]
status: stable
brief: "Security must not depend on secrecy of design or implementation; only operational secrets (keys, credentials, tokens) may be confidential."
order: 1
---

# Kerckhoffs's principle

The security of the system must not depend on the secrecy of its design or implementation, including its AI components. All security properties must hold when the framework's source code, configuration, architecture, model weights, model identity and version, system prompts, and prompt templates are fully known to an adversary. Only operational secrets — keys, credentials, tokens — may be confidential.

The principle applies regardless of whether the language models used are open-weight or closed-weight: model extraction attacks and the high transfer rate of adversarial inputs across models make black-box obscurity an unreliable defense. Defenses that rely on the adversary not knowing the model, the prompts, or the input-construction strategy are excluded by this principle.
