# Agentic Architecture

This document defines the foundational principles, design patterns, architectural primitives, and threats of the framework for building agentic systems that are secure, reliable, and performant. It is intended as reference context for any agent or contributor working on the project. Definitions are normative: deviations require explicit justification. Each definition declares the domain(s) it speaks to — `security`, `reliability`, `performance` — in its frontmatter; a single concept may serve more than one.

---

## Principles

Principles are foundational assumptions and goals. They define what the framework is for and what it refuses to compromise on. A principle may belong to any domain — security, reliability, or performance — as declared in its frontmatter.

<!-- gen:principle:start (generated from frontmatter by tools/gen-index.py — do not edit by hand) -->
| Principle | Domain | Brief | Full Definition |
| --- | --- | --- | --- |
| **Kerckhoffs's principle** | security | Security must not depend on secrecy of design or implementation; only operational secrets (keys, credentials, tokens) may be confidential. | [→](/principles/kerckhoffs-principle.md) |
| **Least privilege principle** | security | Every component is granted the minimum authority required to perform its function. | [→](/principles/least-privilege-principle.md) |
| **Defense in depth** | security | Security properties are enforced by multiple independent layers such that the failure of any single layer does not compromise the system. | [→](/principles/defense-in-depth.md) |
| **Suborned model principle** | security | Any language model must be assumed to be induced into faithful cooperation with adversarial instructions in its input. | [→](/principles/suborned-model-principle.md) |
| **Least Model principle** | security | Minimize model-mediated decision-making in both extent and authority, across all classes of learned models. | [→](/principles/least-model-principle.md) |
| **No agency without auditability principle** | security | No agent invocation may cause a state change without first committing a forensically sufficient record of that invocation. | [→](/principles/no-agency-without-auditability-principle.md) |
<!-- gen:principle:end -->

---

## Design Patterns

Design patterns are the structural responses that implement the principles.

<!-- gen:pattern:start (generated from frontmatter by tools/gen-index.py — do not edit by hand) -->
| Pattern | Domain | Brief | Full Definition |
| --- | --- | --- | --- |
| **Byzantine model design pattern** | security | Treats every model invocation as a Byzantine component capable of arbitrary adversarial behavior; trust is established only through external mechanisms. | [→](/design%20patterns/byzantine-model-design-pattern.md) |
| **Local mediation design pattern** | security | All tool use by stochastic agents must pass through the local framework's deterministic mediation layer; provider-side connectors that act without local visibility are excluded. | [→](/design%20patterns/local-mediation-design-pattern.md) |
| **Provenance tracking design pattern** | security | Every value carries a compile-time `Trusted`/`Untrusted` provenance label; sensitive operations require `Trusted` operands, and audited declassification is the only promotion path. | [→](/design%20patterns/provenance-tracking-design-pattern.md) |
| **Role-typed agent separation design pattern** | security | Generalizes the dual-LLM pattern to N agents typed by trust position — Core, Edge, Bridge — with a declared topology in which Edge → Bridge → Core is the only path to Core. | [→](/design%20patterns/role-typed-agent-separation-design-pattern.md) |
| **Write-ahead audit** | security | Commit the invocation record before executing the authorized action, ensuring no unrecorded state changes. | [→](/design%20patterns/write-ahead-audit.md) |
| **Trusted-path logging** | security | Write log entries through a channel outside the model's authority, to storage the model cannot modify. | [→](/design%20patterns/trusted-path-logging.md) |
| **Hash-chained logs** | security | Append-only logs where each entry is cryptographically bound to its predecessor. | [→](/design%20patterns/hash-chained-logs.md) |
| **Replay-able invocation records** | security | Capture full invocation state enabling deterministic re-execution for forensic analysis. | [→](/design%20patterns/replay-able-invocation-records.md) |
<!-- gen:pattern:end -->

---

## Architectural Primitives

Architectural primitives are the building blocks the framework composes.

Agents are nodes in the orchestration graph or finite-state machine. They are classified along three orthogonal axes:

- **Scope axis.** How narrowly the agent's responsibility is defined. The framework admits only *specialist agents* on this axis; generalist agents are excluded by design.
- **Computational nature axis.** Whether the agent's computation is *stochastic* (model-mediated) or *deterministic* (pure code).
- **Trust-position axis.** Where the agent sits in the data-flow trust hierarchy: *Core* (holds sensitive capabilities, never exposed to untrusted data), *Edge* (exposed to untrusted data, holds no sensitive capabilities), or *Bridge* (performs validated declassification from Untrusted to Trusted). This axis is the architectural expression of the role-typed agent separation design pattern.

The axes are orthogonal: an agent's position on one does not determine its position on the others. A concrete agent is specified by a triple — for example, *a specialist deterministic Bridge agent* (a narrow code-only node that performs declassification) or *a specialist stochastic Edge agent* (a narrow model-mediated node that processes untrusted input without holding sensitive capabilities). Each combination carries different obligations under the principles and patterns defined above.

<!-- gen:primitive:start (generated from frontmatter by tools/gen-index.py — do not edit by hand) -->
| Primitive | Domain | Brief | Full Definition |
| --- | --- | --- | --- |
| **Specialist agents** | security, performance | Nodes with narrow, well-defined scopes of responsibility and restricted capability footprint. | [→](/architectural%20primitives/specialist-agents.md) |
| **Stochastic agents** | security | Agents whose computation involves probabilistic model inference of any model class; subject to the Byzantine model pattern, and to the suborned model principle where instruction-following. | [→](/architectural%20primitives/stochastic-agents.md) |
| **Deterministic agents** | security | Pure code agents with deterministic behavior; same interface as stochastic agents but without probabilistic or adversarial-input behavior. | [→](/architectural%20primitives/deterministic-agents.md) |
| **Core agents** | security | Hold sensitive capabilities and produce plans, decisions, and actions; never exposed to `Untrusted` data. Generalization of the dual-LLM P-LLM. | [→](/architectural%20primitives/core-agents.md) |
| **Edge agents** | security | Exposed to external `Untrusted` data, which they transform; hold no sensitive capabilities and emit only `Untrusted` outputs. Generalization of the dual-LLM Q-LLM. | [→](/architectural%20primitives/edge-agents.md) |
| **Bridge agents** | security | Perform validated, logged declassification from `Untrusted` to `Trusted` of restricted type; the only path by which Edge-produced content reaches Core agents. | [→](/architectural%20primitives/bridge-agents.md) |
<!-- gen:primitive:end -->

---

## Threats and Failure Modes

Threats are the failure modes the framework defends against. Unlike principles, patterns, and primitives — which describe what to build — a threat describes what can go wrong: an adversarial exploit or a reliability failure mode that the other concepts exist to mitigate. Each is linked to the principles, patterns, and primitives that mitigate it.

<!-- gen:threat:start (generated from frontmatter by tools/gen-index.py — do not edit by hand) -->
| Threat | Domain | Brief | Full Definition |
| --- | --- | --- | --- |
<!-- gen:threat:end -->

