# Specialist agents (scope axis)

Nodes bound to narrow, well-defined scopes of responsibility, with capability and authority restricted to those required for that scope. The term emphasizes *scope*, not *competence*; the security argument rests on what a specialist agent is structurally incapable of doing, not on what it is skilled at doing. The property applies to both stochastic and deterministic agents.

Defining properties:

- **Narrow scope.** The agent's responsibility covers a single, declarable function or domain. Scope is part of the agent's specification, not an emergent property of its prompt or code.
- **Minimum capability footprint.** Tool access, file system access, network access, and any other authority are restricted to what the agent's declared scope requires, applying least privilege at the agent level.
- **External enforcement.** Scope and capability bounds are enforced by the host framework through sandboxing, capability tokens, and deterministic mediation of effects — not by the agent's instructions, its code, or its own judgment.
- **Validated interfaces.** Agents communicate through typed, schema-checked interfaces. Composition is the responsibility of deterministic orchestration code, not of the agents themselves.
- **Independent failure.** The compromise of one specialist agent does not propagate to others; agents treat one another's outputs as untrusted input.

The architectural intent is that broad capability emerges from the composition of narrow agents under deterministic orchestration, rather than residing in any single agent. This is the agent-level analog of the UNIX philosophy of small, single-purpose tools composed through clear interfaces.
