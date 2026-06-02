---
id: edge-agents
title: Edge agents (trust-position axis)
type: primitive
domains: [security]
status: stable
instantiates: ["[[role-typed-agent-separation-design-pattern]]"]
depends_on: ["[[bridge-agents]]"]
---

# Edge agents (trust-position axis)

Agents exposed to external `Untrusted` data, which they transform — extract, summarize, translate, classify, parse — without holding any sensitive capability. Edge agents are the structural generalization of the Quarantined LLM (Q-LLM). The trust-position axis is the architectural expression of the [role-typed agent separation design pattern](/design%20patterns/role-typed-agent-separation-design-pattern.md).

Defining properties:

- **No sensitive capabilities.** Edge agents cannot invoke tools that affect state, cannot mint capabilities, and cannot issue privileged requests. Their authority is restricted to producing typed `Untrusted` values from `Untrusted` inputs.
- **All outputs are `Untrusted`.** The type system labels every output of an Edge agent as `Untrusted` regardless of how structured, confident, or well-formatted the output appears. Confidence is not provenance.
- **Bounded action surface even under suborning.** Because Edge agents hold no sensitive capabilities, a successfully suborned Edge agent can do nothing beyond producing crafted `Untrusted` output. The damage path runs through downstream Bridge declassification, which is where defenses against suborned Edge agents are concentrated.
- **The natural locus for stochastic agents that process external content.** Web reading, document parsing, RAG context assembly, email and message ingestion, and any other task that handles attacker-controllable input are Edge concerns by default.

An Edge agent's outputs reach [Core agents](/architectural%20primitives/core-agents.md) only after [Bridge](/architectural%20primitives/bridge-agents.md) declassification; the declared topology admits no direct Edge → Core edge.
