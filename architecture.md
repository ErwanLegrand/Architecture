# Security Principles, Design Patterns, and Architectural Primitives

This document defines the foundational principles, design patterns, and architectural primitives of the framework. It is intended as reference context for any agent or contributor working on the project. Definitions are normative: deviations require explicit justification.

---

## Principles

Principles are foundational assumptions and goals. They define what the framework is for and what it refuses to compromise on.

### Kerckhoffs's principle

The security of the system must not depend on the secrecy of its design or implementation, including its AI components. All security properties must hold when the framework's source code, configuration, architecture, model weights, model identity and version, system prompts, and prompt templates are fully known to an adversary. Only operational secrets — keys, credentials, tokens — may be confidential.

The principle applies regardless of whether the language models used are open-weight or closed-weight: model extraction attacks and the high transfer rate of adversarial inputs across models make black-box obscurity an unreliable defense. Defenses that rely on the adversary not knowing the model, the prompts, or the input-construction strategy are excluded by this principle.

### Least privilege principle

Every component is granted the minimum authority required to perform its function, and no more. Authority is denied by default and explicitly granted; expansion of authority requires explicit justification, not implicit accumulation.

### Defense in depth

Security properties are enforced by multiple independent layers — preventive, detective, and responsive — such that the failure of any single layer does not compromise the system. No single control is treated as sufficient.

### Suborned model principle

Any language model that processes input must be assumed to be induced into faithful cooperation with whatever adversarial instructions that input may carry — including instructions embedded in tool outputs, retrieved documents, prior conversation turns, or upstream model responses.

The term derives from the legal sense of *suborn* (to induce another party to commit a wrong) and reflects the mechanism by which prompt injection operates: the model is not malfunctioning when it follows injected instructions; it is functioning as designed, but its alignment has been redirected by an attacker through ordinary input channels.

The principle assumes the worst case: that on every invocation, the model is actively aligned with an adversary who has crafted some portion of its input. Consequently, no security property may be derived from the model's compliance, judgment, refusal behavior, or self-report. All trust must be externally enforced.

### Least LLM principle

The use of language-model-mediated decision-making is minimized in both extent and authority. Each component is implemented in deterministic code unless an LLM is genuinely required, and each LLM invocation is given the narrowest scope sufficient to perform its task.

The principle composes with least privilege along an orthogonal axis: where least privilege bounds authority per component, least LLM bounds the number of components that have LLM-mediated agency at all. Every place an LLM is used is a place prompt injection can manifest, so minimizing LLM use directly reduces attack surface.

### No agency without auditability principle

No language model output may cause a state change in the system or its environment unless the framework has first committed a forensically sufficient record of the invocation that produced it.

The record must capture:

- The model's input as the model saw it (byte-for-byte, including system prompt, tool outputs, retrieved content, prior turns).
- The model's output verbatim, pre-parsing and pre-validation.
- The action the framework took, distinguished from what the model requested.
- The policy decision that authorized the action.
- The causal lineage linking this invocation to its triggers and downstream effects.
- The model identity and version, including sampling parameters and prompt template version.

The record must be written through a path outside the model's authority, to storage the model cannot modify. Audit is treated as part of the trust kernel of the framework, not as observability tooling: it is the detection layer of defense in depth, complementing the preventive controls implied by the Byzantine model design pattern.

---

## Design patterns

Design patterns are the structural responses that implement the principles.

### Byzantine model design pattern

The design response that follows from the suborned model principle. Every language model invocation is treated as a Byzantine component in the sense of distributed systems: capable of arbitrary, adversarial behavior, including coordinated misbehavior with other components. Trust in any model output is established only through mechanisms external to the model itself.

In practice:

- **Output validation.** Model outputs are parsed, type-checked, and policy-checked by deterministic code before any action is taken.
- **Independent verification.** Where stakes warrant, a model's output is checked by a separate model instance or a deterministic verifier with no shared context, applying the BFT principle that no single Byzantine node should determine an outcome.
- **Externally bounded authority.** Each model invocation operates within a sandbox whose boundary is unaffected by what the model produces; the model cannot widen its own authority by emitting tokens.
- **Mutual suspicion between agents.** In multi-agent systems, agent B treats agent A's output as adversarial input, not as a trusted upstream signal.

The pattern is modeled on classical Byzantine fault tolerance, with the substantive difference that the assumed adversarial fraction is one: every model invocation is treated as Byzantine by default, not merely some bounded subset.

### Patterns implementing the no-agency-without-auditability principle

- **Write-ahead audit.** Commit the invocation record before executing the action it authorizes, parallel to database write-ahead logging. A crash between record and action leaves no unrecorded state changes.
- **Trusted-path logging.** Write log entries through a channel outside the model's authority, to storage the model cannot reach or modify. The path from model output to committed log entry passes only through code in the trust kernel.
- **Hash-chained logs.** Append-only logs in which each entry is cryptographically bound to its predecessor, making after-the-fact tampering detectable.
- **Replay-able invocation records.** Capture enough state — model identity and version, sampling parameters, full input as the model saw it, prompt template version — that any invocation can be deterministically re-executed from its log entry for forensic analysis or debugging.

---

## Architectural primitives

Architectural primitives are the building blocks the framework composes.

Agents are nodes in the orchestration graph or finite-state machine. They are classified along two orthogonal axes:

- **Scope axis.** How narrowly the agent's responsibility is defined.
- **Computational nature axis.** Whether the agent's computation is stochastic (model-mediated) or deterministic (pure code).

The framework admits only specialist agents by design — generalist agents are excluded — but specialists may be either stochastic or deterministic depending on which member of the computational-nature axis they occupy. A *specialist stochastic agent* is a narrow LLM-mediated node; a *specialist deterministic agent* is a narrow code-only node. Both participate as peers in the same orchestration graph, with the same node interface and the same lifecycle, but they carry different obligations under the principles defined above.

### Specialist agents (scope axis)

Nodes bound to narrow, well-defined scopes of responsibility, with capability and authority restricted to those required for that scope. The term emphasizes *scope*, not *competence*; the security argument rests on what a specialist agent is structurally incapable of doing, not on what it is skilled at doing. The property applies to both stochastic and deterministic agents.

Defining properties:

- **Narrow scope.** The agent's responsibility covers a single, declarable function or domain. Scope is part of the agent's specification, not an emergent property of its prompt or code.
- **Minimum capability footprint.** Tool access, file system access, network access, and any other authority are restricted to what the agent's declared scope requires, applying least privilege at the agent level.
- **External enforcement.** Scope and capability bounds are enforced by the host framework through sandboxing, capability tokens, and deterministic mediation of effects — not by the agent's instructions, its code, or its own judgment.
- **Validated interfaces.** Agents communicate through typed, schema-checked interfaces. Composition is the responsibility of deterministic orchestration code, not of the agents themselves.
- **Independent failure.** The compromise of one specialist agent does not propagate to others; agents treat one another's outputs as untrusted input.

The architectural intent is that broad capability emerges from the composition of narrow agents under deterministic orchestration, rather than residing in any single agent. This is the agent-level analog of the UNIX philosophy of small, single-purpose tools composed through clear interfaces.

### Stochastic agents (computational nature axis)

Agents whose computation involves probabilistic language-model inference. A stochastic agent's output is sampled from a probability distribution conditioned on its input; the same input may produce different outputs across invocations.

Stochastic agents are the locus of the framework's LLM-mediated capability. They are subject to:

- The **suborned model principle**: the model is assumed actively aligned with an adversary on every invocation.
- The **Byzantine model design pattern**: outputs are validated, authority is externally bounded, mutual suspicion is the default in multi-agent composition.
- The **no agency without auditability principle**: every invocation is recorded forensically before its output is permitted to cause a state change.
- The **least LLM principle**: a stochastic agent is introduced only when no deterministic implementation would suffice. The default node type is deterministic; choosing stochastic is a deliberate decision requiring justification.

### Deterministic agents (computational nature axis)

Agents implemented as pure code with deterministic behavior: given the same input, they produce the same output and the same side effects, modulo declared sources of nondeterminism (clock, RNG with recorded seed, etc.). They are not language-model-mediated.

Deterministic agents participate in the orchestration graph as peers of stochastic agents — same node interface, same lifecycle, same place in the FSM — but without the probabilistic and adversarial-input properties that make stochastic agents subject to the suborned model principle. In a graph or FSM, any step that does not require probabilistic inference should be a deterministic agent; this is the practical expression of the least LLM principle at the node level.

Deterministic agents remain subject to:

- **Least privilege**: scope and capability footprint are minimized at the node level.
- **Validated interfaces**: input and output are schema-checked at the boundaries.
- **Auditability**: their invocations are recorded as part of the orchestration trace, with input, output, side effects, and code version captured. The audit content differs from a stochastic agent's (no model input or output to record) but the principle that every state-changing invocation is reconstructible from logs applies equally.

They are *not* subject to the suborned model principle (there is no model to suborn) nor to the Byzantine model design pattern in the form applied to stochastic agents (no adversarial inference). However, their *inputs* may originate from stochastic agents, in which case those inputs must be treated as adversarial per the Byzantine pattern. The boundary between a stochastic agent and a downstream deterministic agent is exactly where the Byzantine treatment of model output is enforced: validation, parsing, and policy checks happen at that interface, performed by the deterministic agent on behalf of the framework.
