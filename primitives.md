# Primitives

Primitives are the building blocks the framework composes.

Agents are nodes in the orchestration graph or finite-state machine. They are classified along three orthogonal axes:

- **Scope axis.** How narrowly the agent's responsibility is defined. The framework admits only *specialist agents* on this axis; generalist agents are excluded by design.
- **Computational nature axis.** Whether the agent's computation is *stochastic* (model-mediated) or *deterministic* (pure code).
- **Trust-position axis.** Where the agent sits in the data-flow trust hierarchy: *Core* (holds sensitive capabilities, never exposed to untrusted data), *Edge* (exposed to untrusted data, holds no sensitive capabilities), or *Bridge* (performs validated declassification from Untrusted to Trusted). This axis is the architectural expression of the [role-typed agent separation design pattern](/patterns/role-typed-agent-separation-design-pattern.md).

The axes are orthogonal: an agent's position on one does not determine its position on the others. A concrete agent is specified by a triple — for example, *a specialist deterministic Bridge agent* (a narrow code-only node that performs declassification) or *a specialist stochastic Edge agent* (a narrow model-mediated node that processes untrusted input without holding sensitive capabilities). Each combination carries different obligations under the principles and patterns.

The table below is generated from each definition's frontmatter by `tools/gen-index.py`; do not edit it by hand. Full definitions live under [`/primitives/`](/primitives/).

<!-- gen:primitive:start (generated from frontmatter by tools/gen-index.py — do not edit by hand) -->
| Primitive | Domain | Brief | Full Definition |
| --- | --- | --- | --- |
| **Specialist agents** | security, performance | Nodes with narrow, well-defined scopes of responsibility and restricted capability footprint. | [→](/primitives/specialist-agents.md) |
| **Stochastic agents** | security | Agents whose computation involves probabilistic model inference of any model class; subject to the Byzantine model pattern, and to the suborned model principle where instruction-following. | [→](/primitives/stochastic-agents.md) |
| **Deterministic agents** | security | Pure code agents with deterministic behavior; same interface as stochastic agents but without probabilistic or adversarial-input behavior. | [→](/primitives/deterministic-agents.md) |
| **Core agents** | security | Hold sensitive capabilities and produce plans, decisions, and actions; never exposed to `Untrusted` data. Generalization of the dual-LLM P-LLM. | [→](/primitives/core-agents.md) |
| **Edge agents** | security | Exposed to external `Untrusted` data, which they transform; hold no sensitive capabilities and emit only `Untrusted` outputs. Generalization of the dual-LLM Q-LLM. | [→](/primitives/edge-agents.md) |
| **Bridge agents** | security | Perform validated, logged declassification from `Untrusted` to `Trusted` of restricted type; the only path by which Edge-produced content reaches Core agents. | [→](/primitives/bridge-agents.md) |
| **Agent loop** | reliability | The core execution cycle — perceive, reason, act, observe, update state — repeated until a termination condition is met. | [→](/primitives/agent-loop.md) |
| **Iteration limit** | reliability | A hard, externally enforced ceiling on loop iterations, set by the loop infrastructure rather than the agent. | [→](/primitives/iteration-limit.md) |
| **Termination condition** | reliability | An explicit predicate the loop infrastructure evaluates each iteration, covering both the success and the failure terminals. | [→](/primitives/termination-condition.md) |
| **Checkpoint store** | reliability | External, durable, agent-independent storage for task-critical state, written before each phase so any instance can resume. | [→](/primitives/checkpoint-store.md) |
| **Idempotency key** | reliability | A stable identifier derived from an operation's intent that lets a receiver detect and de-duplicate re-submissions. | [→](/primitives/idempotency-key.md) |
| **Retry budget** | reliability | A per-turn cap on total retry attempts across all tool calls, bounding aggregate retry cost independently of per-call limits. | [→](/primitives/retry-budget.md) |
| **Exponential backoff** | reliability | A retry-delay strategy that grows the wait geometrically with jitter to avoid synchronized retries against a recovering service. | [→](/primitives/exponential-backoff.md) |
| **Circuit breaker** | reliability | Stops requests to a failing downstream after repeated failures, making persistent failure visible instead of masking it with endless retries. | [→](/primitives/circuit-breaker.md) |
| **Subagent** | reliability, performance | An isolated execution unit with a bounded context, a declared tool scope, and no shared state; the unit of parallelism in multi-agent orchestration. | [→](/primitives/subagent.md) |
| **Orchestrator** | reliability, performance | The coordinating agent that decomposes goals, dispatches subagents, manages shared state, synthesizes outputs, and evaluates termination. | [→](/primitives/orchestrator.md) |
| **Phase handoff** | reliability | A schema-validated artifact that carries one phase's output to the next phase's input, persisted before the next phase begins. | [→](/primitives/phase-handoff.md) |
| **Shared state store** | reliability, performance | External medium through which agents coordinate by reading their input slice and writing their output slice, without using each other's context windows. | [→](/primitives/shared-state-store.md) |
| **Worktree** | reliability | An isolated filesystem checkout that lets multiple agents make overlapping code changes in parallel without conflict. | [→](/primitives/worktree.md) |
| **Acceptance criterion** | reliability | An explicit, evaluatable definition of task completion that distinguishes a result merely produced from one that is correct. | [→](/primitives/acceptance-criterion.md) |
| **Context window** | performance | The total token capacity of a single model invocation, covering system prompt, history, tool outputs, and response. | [→](/primitives/context-window.md) |
| **Compaction boundary** | performance | A token threshold, set below the context ceiling, that triggers compaction; also fires at logical workflow boundaries. | [→](/primitives/compaction-boundary.md) |
| **Prompt cache** | performance | A provider-side cache keyed on the stable prefix of the window; hits avoid re-encoding the prefix, cutting latency and cost. | [→](/primitives/prompt-cache.md) |
| **Model tier** | performance | A categorical classification of model capability and cost — fast, mid, high — assigned in agent profile metadata, not selected at runtime. | [→](/primitives/model-tier.md) |
| **Compacted summary** | performance | A structured replacement for conversation history produced by compaction — current state, key decisions, artifacts in flight, open questions. | [→](/primitives/compacted-summary.md) |
| **Token budget** | performance | A declared ceiling on token expenditure for a session, operation, or invocation, enforced by the harness rather than the agent. | [→](/primitives/token-budget.md) |
| **Model attestation** | security | A verified binding of a model's identity, version, and weight integrity, checked by the harness before the model is admitted for use, detecting tampering or substitution of the weights. | [→](/primitives/model-attestation.md) |
| **Wall-clock budget** | reliability, performance | A declared ceiling on elapsed wall-clock time for a session, operation, or invocation, enforced by the harness — the time-domain sibling of the token and retry budgets. | [→](/primitives/wall-clock-budget.md) |
| **Rate limit** | security, reliability | A ceiling on the rate at which requests are admitted over a time window, enforced ahead of saturation rather than after failure like the circuit breaker. | [→](/primitives/rate-limit.md) |
<!-- gen:primitive:end -->
