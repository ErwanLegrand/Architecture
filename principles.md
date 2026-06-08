# Principles

Principles are foundational assumptions and goals. They define what the framework is for and what it refuses to compromise on. A principle may belong to any domain — security, reliability, or performance — as declared in its frontmatter.

The table below is generated from each definition's frontmatter by `tools/gen-index.py`; do not edit it by hand. Full definitions live under [`/principles/`](/principles/).

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
| **Stateless subagent** | reliability | Subagents hold no persistent state across invocations; all task state is externalized, making them restartable, parallelizable, and replaceable. | [→](/principles/stateless-subagent.md) |
| **Scope limiting** | performance, reliability | Each agent receives only the context slice its task requires; no subagent's reasoning trace is visible to another. | [→](/principles/scope-limiting.md) |
| **Right model for task** | performance | Every invocation uses the cheapest model sufficient for its task; capability the task does not need adds cost and latency without improving the result. | [→](/principles/right-model-for-task.md) |
| **Stable prefix** | performance | Keep stable context at the start of the window so the prompt cache stays warm; reordering stable sections across turns destroys cache hits. | [→](/principles/stable-prefix.md) |
| **Output minimization** | performance | Output token volume is a cost driver — of price, latency, and downstream context pressure — and so a design variable, not a style preference. | [→](/principles/output-minimization.md) |
<!-- gen:principle:end -->
