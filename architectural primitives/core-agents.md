---
id: core-agents
title: Core agents (trust-position axis)
type: primitive
domains: [security]
status: stable
brief: "Hold sensitive capabilities and produce plans, decisions, and actions; never exposed to `Untrusted` data. Generalization of the dual-LLM P-LLM."
order: 4
instantiates: ["[[role-typed-agent-separation-design-pattern]]"]
depends_on: ["[[bridge-agents]]"]
---

# Core agents (trust-position axis)

Agents that hold sensitive capabilities and produce decisions, plans, and actions, and are *never* exposed to `Untrusted` data. Core agents are the structural generalization of the Privileged LLM (P-LLM) in the dual-LLM pattern. The trust-position axis is the architectural expression of the [role-typed agent separation design pattern](/design%20patterns/role-typed-agent-separation-design-pattern.md).

Defining properties:

- **Holds sensitive capabilities.** Tool access, capability minting, audit-record signing, and any operation that affects state outside the agent are granted exclusively to Core agents. Edge and Bridge agents may invoke nothing of consequence directly.
- **`Trusted` inputs only.** The type system rejects `Untrusted` values as input to Core operations at compile time. A Core agent may *reference* `Untrusted` content only through opaque handles produced by Bridge declassification, and only at the schema the Bridge committed to.
- **Plans and decisions, not free text.** Stochastic Core agents emit structured plans in a closed DSL deserialized into a typed AST. The action space is fixed at compile time. Free-text emission from a Core agent is rejected by the framework before it can reach an effector.
- **Compromise of a Core agent is the highest-impact failure mode.** Defenses concentrate here: deterministic implementation where possible (a deterministic Core agent is not subject to the suborned model principle); strict provenance enforcement on inputs; output validation via the Byzantine pattern; quorum or independent verification for high-stakes decisions.
