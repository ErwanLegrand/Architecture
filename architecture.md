# Secure Agentic Architecture

This document defines the foundational security principles, design patterns, and architectural primitives of the framework for building secure agentic systems. It is intended as reference context for any agent or contributor working on the project. Definitions are normative: deviations require explicit justification.

---

## Security Principles

Principles are foundational assumptions and goals. They define what the framework is for and what it refuses to compromise on.

| Principle | Brief | Full Definition |
|-----------|-------|------------------|
| **Kerckhoffs's principle** | Security must not depend on secrecy of design or implementation; only operational secrets (keys, credentials, tokens) may be confidential. | [→](/security%20principles/kerckhoffs-principle.md) |
| **Least privilege principle** | Every component is granted the minimum authority required to perform its function. | [→](/security%20principles/least-privilege-principle.md) |
| **Defense in depth** | Security properties are enforced by multiple independent layers such that the failure of any single layer does not compromise the system. | [→](/security%20principles/defense-in-depth.md) |
| **Suborned model principle** | Any language model must be assumed to be induced into faithful cooperation with adversarial instructions in its input. | [→](/security%20principles/suborned-model-principle.md) |
| **Least LLM principle** | Minimize language-model-mediated decision-making in both extent and authority. | [→](/security%20principles/least-llm-principle.md) |
| **No agency without auditability principle** | No model output may cause a state change without first committing a forensically sufficient record of the invocation. | [→](/security%20principles/no-agency-without-auditability-principle.md) |

---

## Design Patterns

Design patterns are the structural responses that implement the principles.

| Pattern | Brief | Full Definition |
|---------|-------|------------------|
| **Byzantine model design pattern** | Treats every model invocation as a Byzantine component capable of arbitrary adversarial behavior; trust is established only through external mechanisms. | [→](/design%20patterns/byzantine-model-design-pattern.md) |
| **Write-ahead audit** | Commit the invocation record before executing the authorized action, ensuring no unrecorded state changes. | [→](/design%20patterns/write-ahead-audit.md) |
| **Trusted-path logging** | Write log entries through a channel outside the model's authority, to storage the model cannot modify. | [→](/design%20patterns/trusted-path-logging.md) |
| **Hash-chained logs** | Append-only logs where each entry is cryptographically bound to its predecessor. | [→](/design%20patterns/hash-chained-logs.md) |
| **Replay-able invocation records** | Capture full invocation state enabling deterministic re-execution for forensic analysis. | [→](/design%20patterns/replay-able-invocation-records.md) |

---

## Architectural Primitives

Architectural primitives are the building blocks the framework composes.

Agents are nodes in the orchestration graph or finite-state machine. They are classified along two orthogonal axes:

- **Scope axis.** How narrowly the agent's responsibility is defined.
- **Computational nature axis.** Whether the agent's computation is stochastic (model-mediated) or deterministic (pure code).

The framework admits only specialist agents by design — generalist agents are excluded — but specialists may be either stochastic or deterministic depending on which member of the computational-nature axis they occupy. A *specialist stochastic agent* is a narrow LLM-mediated node; a *specialist deterministic agent* is a narrow code-only node. Both participate as peers in the same orchestration graph, with the same node interface and the same lifecycle, but they carry different obligations under the principles defined above.

| Primitive | Brief | Full Definition |
|-----------|-------|------------------|
| **Specialist agents** | Nodes with narrow, well-defined scopes of responsibility and restricted capability footprint. | [→](/architectural%20primitives/specialist-agents.md) |
| **Stochastic agents** | Agents whose computation involves probabilistic language-model inference; subject to suborned model principle and Byzantine model pattern. | [→](/architectural%20primitives/stochastic-agents.md) |
| **Deterministic agents** | Pure code agents with deterministic behavior; same interface as stochastic agents but without probabilistic or adversarial-input behavior. | [→](/architectural%20primitives/deterministic-agents.md) |
