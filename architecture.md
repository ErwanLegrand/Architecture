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
| **Least Model principle** | security, reliability | Minimize model-mediated decision-making in both extent and authority, across all classes of learned models. | [→](/principles/least-model-principle.md) |
| **No agency without auditability principle** | security | No agent invocation may cause a state change without first committing a forensically sufficient record of that invocation. | [→](/principles/no-agency-without-auditability-principle.md) |
| **Step reliability compounding** | reliability | In an unverified chain of stochastic steps end-to-end reliability is the product of per-step reliabilities; verification gates break this multiplicative decay. | [→](/principles/step-reliability-compounding.md) |
| **Fail fast / crash only** | reliability | A component that cannot guarantee clean recovery terminates immediately and restarts from the last checkpoint; no partial-state cleanup logic. | [→](/principles/fail-fast-crash-only.md) |
| **Observable failure** | reliability | Every failure must be detectable, attributable, and surfaced promptly; silent wrong output is worse than a loud error. | [→](/principles/observable-failure.md) |
| **Explicit termination** | reliability | Every agent loop must have a declared, mechanically verifiable termination condition enforced by the loop infrastructure, not the agent's judgement. | [→](/principles/explicit-termination.md) |
| **Intent-aligned retry** | reliability | Retry boundaries align to the intent unit, not the step unit; safe-to-retry is declared per operation, not inferred from transport. | [→](/principles/intent-aligned-retry.md) |
| **Idempotency as a design constraint** | reliability | Every mutating operation must be idempotent by design; under retries, restarts, and replays any non-idempotent operation eventually executes more than once. | [→](/principles/idempotency-as-design-constraint.md) |
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
| **Review-and-critique loop** | reliability | A generator produces output, a separate critic evaluates it against explicit criteria, and the generator revises until criteria pass or a limit is reached. | [→](/design%20patterns/review-and-critique-loop.md) |
| **Adversarial critique** | reliability | A critic that attempts to refute rather than approve the output — Socratic questioning and Popperian falsification — surfacing failures a confirmatory review would pass. | [→](/design%20patterns/adversarial-critique.md) |
| **Deterministic verification gate** | reliability | A deterministic check — static analysis, type check, schema validation, test — placed after a stochastic step to catch a class of errors with certainty. | [→](/design%20patterns/deterministic-verification-gate.md) |
| **N-version consensus** | reliability | Generate a step's output independently n times and select the agreed result, reducing residual error far faster than a single pass. | [→](/design%20patterns/n-version-consensus.md) |
| **Checkpoint-resume** | reliability | Persist state to a durable store before each phase and, on failure, restart from the last checkpoint rather than from scratch. | [→](/design%20patterns/checkpoint-resume.md) |
| **Crash-only agent** | reliability | An agent with no cleanup or rollback logic that, on failure, terminates and resumes from the last checkpoint. | [→](/design%20patterns/crash-only-agent.md) |
| **Idempotent tool design** | reliability | Every state-mutating tool takes a stable idempotency key and treats a repeated key as a no-op that returns the original result. | [→](/design%20patterns/idempotent-tool-design.md) |
| **Retry with backoff and budget** | reliability | A retry policy combining exponential backoff with jitter, a bounded attempt count, a circuit breaker, and a per-turn retry budget. | [→](/design%20patterns/retry-with-backoff-and-budget.md) |
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
| **Agent loop** | reliability | The core execution cycle — perceive, reason, act, observe, update state — repeated until a termination condition is met. | [→](/architectural%20primitives/agent-loop.md) |
| **Iteration limit** | reliability | A hard, externally enforced ceiling on loop iterations, set by the loop infrastructure rather than the agent. | [→](/architectural%20primitives/iteration-limit.md) |
| **Termination condition** | reliability | An explicit predicate the loop infrastructure evaluates each iteration, covering both the success and the failure terminals. | [→](/architectural%20primitives/termination-condition.md) |
| **Checkpoint store** | reliability | External, durable, agent-independent storage for task-critical state, written before each phase so any instance can resume. | [→](/architectural%20primitives/checkpoint-store.md) |
| **Idempotency key** | reliability | A stable identifier derived from an operation's intent that lets a receiver detect and de-duplicate re-submissions. | [→](/architectural%20primitives/idempotency-key.md) |
| **Retry budget** | reliability | A per-turn cap on total retry attempts across all tool calls, bounding aggregate retry cost independently of per-call limits. | [→](/architectural%20primitives/retry-budget.md) |
| **Exponential backoff** | reliability | A retry-delay strategy that grows the wait geometrically with jitter to avoid synchronized retries against a recovering service. | [→](/architectural%20primitives/exponential-backoff.md) |
| **Circuit breaker** | reliability | Stops requests to a failing downstream after repeated failures, making persistent failure visible instead of masking it with endless retries. | [→](/architectural%20primitives/circuit-breaker.md) |
<!-- gen:primitive:end -->

---

## Threats and Failure Modes

Threats are the failure modes the framework defends against. Unlike principles, patterns, and primitives — which describe what to build — a threat describes what can go wrong: an adversarial exploit or a reliability failure mode that the other concepts exist to mitigate. Each is linked to the principles, patterns, and primitives that mitigate it.

<!-- gen:threat:start (generated from frontmatter by tools/gen-index.py — do not edit by hand) -->
| Threat | Domain | Brief | Full Definition |
| --- | --- | --- | --- |
<!-- gen:threat:end -->

