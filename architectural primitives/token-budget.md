---
id: token-budget
title: Token budget
type: primitive
domains: [performance]
status: stable
brief: "A declared ceiling on token expenditure for a session, operation, or invocation, enforced by the harness rather than the agent."
order: 29
related_to: ["[[context-window]]", "[[retry-budget]]"]
---

# Token budget

A declared ceiling on token expenditure for a session, operation, or single invocation, enforced by the orchestrator or harness rather than by the agent itself. It prevents runaway cost from a misconfigured loop or an unexpectedly large tool output. The token budget is the policy constraint layered over the context window's physical constraint; the retry budget is its specialization to the cost incurred by retries.
