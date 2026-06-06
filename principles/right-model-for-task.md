---
id: right-model-for-task
title: Right model for task
type: principle
domains: [performance]
status: stable
brief: "Every invocation uses the cheapest model sufficient for its task; capability the task does not need adds cost and latency without improving the result."
order: 18
requires: ["[[model-tier]]"]
related_to: ["[[least-model-principle]]"]
---

# Right model for task

Every agent invocation should use the cheapest model sufficient for its task. High-capability models — slower and costlier — are reserved for deep reasoning, tradeoff analysis, and tasks where a missed error is expensive; fast, inexpensive models cover search, mechanical edits, and structured extraction. Assigning every task to the most capable model is both wasteful and slower, because capability the task does not require does not improve the result.

| Task type | Tier | Rationale |
| --- | --- | --- |
| Search / exploration | Fast | Lookup needs no deep reasoning |
| Single-file mechanical edit | Fast | Instructions are explicit |
| Multi-file implementation | Mid | Requires context synthesis |
| Architecture / planning | High | Deep reasoning and tradeoff analysis |
| Security analysis | High | A missed vulnerability is costly |
| Complex debugging | High | Needs the full system model in context |

It is the cost-and-latency face of the least model principle: where least model minimizes how many stochastic nodes exist at all, right model right-sizes each node that is justified.
