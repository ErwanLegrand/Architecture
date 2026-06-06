---
id: role-typed-agent-separation-design-pattern
title: Role-typed agent separation design pattern
type: pattern
domains: [security]
status: stable
brief: "Generalizes the dual-LLM pattern to N agents typed by trust position — Core, Edge, Bridge — with a declared topology in which Edge → Bridge → Core is the only path to Core."
order: 4
composes_with: ["[[provenance-tracking-design-pattern]]"]
decomposes_into: ["[[core-agents]]", "[[edge-agents]]", "[[bridge-agents]]"]
mitigates: ["[[prompt-injection]]"]
---

# Role-typed agent separation design pattern

The structural generalization of Simon Willison's dual-LLM pattern (April 2023). Dual-LLM separates a *Privileged LLM* (P-LLM), which produces plans but never sees untrusted data, from a *Quarantined LLM* (Q-LLM), which reads untrusted data but holds no capabilities. The pattern generalizes that two-node arrangement to N agents organized by their role in the trust hierarchy.

Three agent roles:

- **Core agents.** Hold sensitive capabilities; produce plans, decisions, and actions; never exposed to `Untrusted` data. The generalization of the P-LLM. Sensitive capabilities (tool access, capability minting, audit-record signing) are granted only to Core agents.
- **Edge agents.** Exposed to external `Untrusted` data; perform extraction, summarization, translation, classification, or any other transformation of untrusted content; hold no sensitive capabilities. The generalization of the Q-LLM. An Edge agent's outputs carry `Untrusted` provenance regardless of how confident or well-structured they appear.
- **Bridge agents.** Perform validated declassification from `Untrusted` to `Trusted` for Core consumption. The mechanism that dual-LLM left implicit. A Bridge agent applies a named, schema-validated declassification function to an `Untrusted` value and produces a `Trusted` value of restricted type, with the declassification logged and bounded.

In practice:

- **Role is part of the agent specification.** An agent's role is declared statically, enforced by the framework through capability assignment, allowed inputs, and topology. Role is not negotiable at runtime and not derivable from the agent's prompt or code.
- **Non-cloneable capabilities, sub-capabilities only narrow.** Tool access is mediated by handles that cannot be duplicated or widened. A Core agent may pass a narrowed sub-capability to another Core agent, but no operation can produce a capability broader than the holder's.
- **Declared topology.** Allowed communication edges between agents are statically specified, with schemas and provenance constraints per edge. Implicit Edge → Core communication is rejected at compile time and at runtime. Edge → Bridge → Core is the only path by which Edge-produced content reaches Core agents.
- **Bridge agents are deterministic by default.** Declassification logic — schema validation, structural checks, parsing into closed types — is a natural fit for deterministic agents. A stochastic Bridge agent is permitted but is itself subject to the [suborned model principle](/principles/suborned-model-principle.md), and any declassification it performs must be checked by deterministic code before the `Trusted` value is released.
- **Dual-LLM is the degenerate case.** A system with one Core agent (the P-LLM), one Edge agent (the Q-LLM), and an implicit Bridge (the orchestrator's deserialization layer) is the two-node specialization of this pattern.

The pattern composes with the [provenance tracking pattern](/design%20patterns/provenance-tracking-design-pattern.md): provenance labels are what role assignment enforces. A Core agent is one the type system permits to hold `Trusted` capabilities; an Edge agent is one the type system constrains to `Untrusted` outputs; a Bridge agent is one the type system permits to call declassification functions.

Because an Edge agent that reads untrusted data holds no sensitive capability and emits only `Untrusted` outputs, a prompt injection in that data cannot escalate into a sensitive action: the separation bounds the blast radius of prompt injection by construction, confining the suborned agent to the authority of its role.

The pattern descends from Simon Willison's dual-LLM (April 2023) and CaMeL (Debenedetti et al., March 2025), extended to multi-agent systems through the explicit Bridge role and the declared topology. The N-agent generalization makes the pattern usable for orchestration frameworks beyond the two-LLM case CaMeL originally addressed.
