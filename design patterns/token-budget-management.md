---
id: token-budget-management
title: Token budget management
type: pattern
domains: [performance]
status: stable
brief: "Impose hard internal token limits below the API ceiling, track per-turn spend, pre-check expensive operations, and expose remaining budget to orchestrators."
order: 29
requires: ["[[token-budget]]"]
related_to: ["[[context-compaction]]", "[[right-model-for-task]]"]
---

# Token budget management

A hard internal token limit is set below the provider's ceiling, expenditure is tracked per turn, a pre-flight check guards expensive operations against the remaining balance, and the remaining budget is exposed to orchestrators so they can scale work dynamically. Where context compaction and model selection *reduce* spend, the budget *bounds* it: when an operation would exceed the ceiling, the pattern fails loudly rather than silently overrunning, turning cost overrun into an observable, enforced limit.
