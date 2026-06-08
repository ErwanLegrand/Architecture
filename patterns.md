# Patterns

Patterns are the structural responses that implement the principles.

The table below is generated from each definition's frontmatter by `tools/gen-index.py`; do not edit it by hand. Full definitions live under [`/patterns/`](/patterns/).

<!-- gen:pattern:start (generated from frontmatter by tools/gen-index.py — do not edit by hand) -->
| Pattern | Domain | Brief | Full Definition |
| --- | --- | --- | --- |
| **Byzantine model design pattern** | security | Treats every model invocation as a Byzantine component capable of arbitrary adversarial behavior; trust is established only through external mechanisms. | [→](/patterns/byzantine-model-design-pattern.md) |
| **Local mediation design pattern** | security | All tool use by stochastic agents must pass through the local framework's deterministic mediation layer; provider-side connectors that act without local visibility are excluded. | [→](/patterns/local-mediation-design-pattern.md) |
| **Provenance tracking design pattern** | security | Every value carries a compile-time `Trusted`/`Untrusted` provenance label; sensitive operations require `Trusted` operands, and audited declassification is the only promotion path. | [→](/patterns/provenance-tracking-design-pattern.md) |
| **Role-typed agent separation design pattern** | security | Generalizes the dual-LLM pattern to N agents typed by trust position — Core, Edge, Bridge — with a declared topology in which Edge → Bridge → Core is the only path to Core. | [→](/patterns/role-typed-agent-separation-design-pattern.md) |
| **Write-ahead audit** | security | Commit the invocation record before executing the authorized action, ensuring no unrecorded state changes. | [→](/patterns/write-ahead-audit.md) |
| **Trusted-path logging** | security | Write log entries through a channel outside the model's authority, to storage the model cannot modify. | [→](/patterns/trusted-path-logging.md) |
| **Hash-chained logs** | security | Append-only logs where each entry is cryptographically bound to its predecessor. | [→](/patterns/hash-chained-logs.md) |
| **Replay-able invocation records** | security | Capture full invocation state enabling deterministic re-execution for forensic analysis. | [→](/patterns/replay-able-invocation-records.md) |
| **Capability-based security design pattern** | security | Access to a resource is governed by possession of an unforgeable capability naming the object and permitted operations; authority travels with the reference, not the identity. | [→](/patterns/capability-based-security-design-pattern.md) |
| **Review-and-critique loop** | reliability | A generator produces output, a separate critic evaluates it against explicit criteria, and the generator revises until criteria pass or a limit is reached. | [→](/patterns/review-and-critique-loop.md) |
| **Adversarial critique** | reliability | A critic that attempts to refute rather than approve the output — Socratic questioning and Popperian falsification — surfacing failures a confirmatory review would pass. | [→](/patterns/adversarial-critique.md) |
| **Deterministic verification gate** | reliability | A deterministic check — static analysis, type check, schema validation, test — placed after a stochastic step to catch a class of errors with certainty. | [→](/patterns/deterministic-verification-gate.md) |
| **N-version consensus** | reliability | Generate a step's output independently n times and select the agreed result, reducing residual error far faster than a single pass. | [→](/patterns/n-version-consensus.md) |
| **Checkpoint-resume** | reliability | Persist state to a durable store before each phase and, on failure, restart from the last checkpoint rather than from scratch. | [→](/patterns/checkpoint-resume.md) |
| **Crash-only agent** | reliability | An agent with no cleanup or rollback logic that, on failure, terminates and resumes from the last checkpoint. | [→](/patterns/crash-only-agent.md) |
| **Idempotent tool design** | reliability | Every state-mutating tool takes a stable idempotency key and treats a repeated key as a no-op that returns the original result. | [→](/patterns/idempotent-tool-design.md) |
| **Retry with backoff and budget** | reliability | A retry policy combining exponential backoff with jitter, a bounded attempt count, a circuit breaker, and a per-turn retry budget. | [→](/patterns/retry-with-backoff-and-budget.md) |
| **Sequential phase orchestration** | reliability | Chain specialized agents so each has one input and one output persisted as a handoff before the next phase begins. | [→](/patterns/sequential-phase-orchestration.md) |
| **ReAct loop** | reliability | At each step the agent produces a Thought, an Action, and receives an Observation, grounding reasoning in environment feedback. | [→](/patterns/react-loop.md) |
| **Iterative retrieval** | reliability | The orchestrator evaluates a subagent's results against the objective and issues targeted follow-ups before accepting, passing why the information is needed. | [→](/patterns/iterative-retrieval.md) |
| **Hierarchical task decomposition** | reliability, performance | A root orchestrator decomposes a goal into independent sub-tasks, routes each to a specialist subagent, and synthesizes the outputs. | [→](/patterns/hierarchical-task-decomposition.md) |
| **Human-in-the-loop** | reliability | Pause the workflow at high-stakes checkpoints for human review or approval before proceeding. | [→](/patterns/human-in-the-loop.md) |
| **Scope limiting / stateless subagent** | reliability, performance | Distribute work across subagents that each receive only their relevant context; the orchestrator synthesizes outputs and no reasoning trace is shared. | [→](/patterns/scope-limiting-stateless-subagent.md) |
| **Parallel worktree isolation** | reliability | Give each agent making overlapping code changes its own filesystem checkout; coordinate through a store, not a shared context window. | [→](/patterns/parallel-worktree-isolation.md) |
| **Shared state coordination** | reliability, performance | Agents coordinate via an external shared state store rather than by serialization into the orchestrator's context window. | [→](/patterns/shared-state-coordination.md) |
| **pass@k / pass^k evaluation** | reliability | Choose pass@k or pass^k to match the task's failure tolerance: at least one of k attempts succeeds, versus all k must succeed. | [→](/patterns/pass-at-k-evaluation.md) |
| **Model selection matrix** | performance | Encode the task-type-to-tier mapping as a declared policy applied at agent-creation time; default to the cheapest sufficient tier, upgrade only with justification. | [→](/patterns/model-selection-matrix.md) |
| **Context compaction** | performance | At a threshold or logical boundary, replace full history with a structured summary, freeing context while retaining active state. | [→](/patterns/context-compaction.md) |
| **Token budget management** | performance | Impose hard internal token limits below the API ceiling, track per-turn spend, pre-check expensive operations, and expose remaining budget to orchestrators. | [→](/patterns/token-budget-management.md) |
| **Admission control** | security, reliability | Bound the work an agent accepts — rate-limit admitted requests, apply backpressure, and shed excess load — rather than only bounding what an accepted run consumes. | [→](/patterns/admission-control.md) |
<!-- gen:pattern:end -->
