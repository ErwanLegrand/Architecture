---
id: provenance-tracking-design-pattern
title: Provenance tracking design pattern
type: pattern
domains: [security]
status: stable
brief: "Every value carries a compile-time `Trusted`/`Untrusted` provenance label; sensitive operations require `Trusted` operands, and audited declassification is the only promotion path."
order: 3
enables: ["[[role-typed-agent-separation-design-pattern]]"]
mitigates: ["[[prompt-injection]]", "[[data-poisoning]]"]
---

# Provenance tracking design pattern

Every value in the system carries a compile-time provenance label — `Trusted` if it originates from the authenticated user, the framework's own code, or a fully validated source, `Untrusted` if it originates from external content read by the system (web pages, emails, documents, RAG corpora, tool outputs, model outputs that processed any of the above). The type system enforces provenance within a process; a wire protocol enforces it across process boundaries. Provenance is the technical substrate on which the [role-typed agent separation pattern](/design%20patterns/role-typed-agent-separation-design-pattern.md) is built — without it, the role typology has nothing to enforce. By keeping model-produced and externally-read values `Untrusted` and gating every sensitive operation on `Trusted` operands, the pattern defeats prompt injection by construction: an injected instruction remains `Untrusted` data and cannot reach a sensitive operation without first passing through audited declassification. The same labelling contains data poisoning: corrupted content in a retrieval corpus, a memory store, or a tool output enters as `Untrusted` and likewise cannot reach a sensitive operation without passing audited declassification.

In practice:

- **Compile-time labels.** Provenance is encoded in the type of every value (in Rust, typically via phantom type parameters or wrapper newtypes). Operations on values are typed by provenance requirements; the compiler rejects use of `Untrusted` values where `Trusted` is required.
- **Provenance-preserving wire protocol.** Every inter-process message carries its provenance label, along with a pipeline identifier and a capability witness. The wire format is canonical and authenticated. Deserialization never silently promotes `Untrusted` to `Trusted`; a received `Trusted` value is accepted only if the sender's authenticated identity is authorized to produce `Trusted` values for that schema on that edge.
- **Sensitive operations require Trusted operands.** Tool invocations, capability invocations, and any operation that affects state outside the agent are gated on the provenance of their arguments. The type system makes "passing an Untrusted argument to a sensitive operation" a compile error, not a runtime check.
- **Audited declassification is the only promotion path.** Promotion from `Untrusted` to `Trusted` happens exclusively through named, logged declassification functions, performed in dedicated code paths (Bridge agents, see the [role-typed agent separation pattern](/design%20patterns/role-typed-agent-separation-design-pattern.md)). Declassification is rare by design; a system with many declassification points is a system with many places where Untrusted content can be silently promoted, and is treated as a design smell.

The pattern descends from information-flow control research (Denning's lattice model, the IFC literature on labels and declassification). Its application to LLM-based agents originates in Simon Willison's dual-LLM pattern (April 2023) and was formalized for agentic systems by Google DeepMind's CaMeL (Debenedetti et al., *Defeating Prompt Injections by Design*, arXiv:2503.18813, March 2025), which introduced explicit `Trusted` / `Untrusted` provenance with declassification as the only promotion path.
