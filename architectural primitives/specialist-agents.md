# Specialist agents (scope axis)

Nodes bound to narrow, well-defined scopes of responsibility, with capability and authority restricted to those required for that scope. The term emphasizes *scope*, not *competence*; the security argument rests on what a specialist agent is structurally incapable of doing, not on what it is skilled at doing. The property applies to both stochastic and deterministic agents.

Defining properties:

- **Narrow scope.** The agent's responsibility covers a single, declarable function or domain. Scope is part of the agent's specification, not an emergent property of its prompt or code.
- **Minimum capability footprint.** Tool access, file system access, network access, and any other authority are restricted to what the agent's declared scope requires, applying least privilege at the agent level.
- **External enforcement.** Scope and capability bounds are enforced by the host framework through sandboxing, capability tokens, and deterministic mediation of effects — not by the agent's instructions, its code, or its own judgment.
- **Validated interfaces.** Agents communicate through typed, schema-checked interfaces. Composition is the responsibility of deterministic orchestration code, not of the agents themselves.
- **Independent failure.** The compromise of one specialist agent does not propagate to others; agents treat one another's outputs as untrusted input.

The architectural intent is that broad capability emerges from the composition of narrow agents under deterministic orchestration, rather than residing in any single agent. This is the agent-level analog of the UNIX philosophy of small, single-purpose tools composed through clear interfaces.

Narrow scope is not stylistic; it is what makes several framework goals achievable:

- **Required for least privilege.** Least privilege at the agent level is achievable only through narrow-scoped specialists: an agent can be held to no more authority than its function requires only if that function is itself narrow and declared. Specialist scoping is therefore a precondition for least privilege, not merely an application of it. This holds for every specialist, stochastic or deterministic.
- **Blast-radius containment under the suborned model principle.** For instruction-following stochastic specialists, the bounded capability footprint that least privilege produces also limits the blast radius of a suborned model — an adversary who captures the agent gains only what its narrow scope can reach — while the independent-failure property keeps the compromise from propagating to peers. This is containment, not prevention; it complements the Byzantine model design pattern.
- **Focused context for stochastic specialists.** A stochastic specialist performs more reliably on a small, focused context than on a broad one. This is a quality and performance benefit rather than a security property, but it is a further reason the framework prefers narrow scopes.

Generality of capability is neither required nor rejected. Because security is externally enforced and may not be derived from the model (suborned model principle, Kerckhoffs), model generality is not a security variable: choosing a general or specialist *model* behind a specialist agent is an engineering tradeoff — capability, latency, and cost (training, serving utilization, and operational surface) — with no single right answer. What the framework rejects is the generalist *agent*: broad scope and authority in one node, not the capable model behind it.
