---
id: iterative-retrieval
title: Iterative retrieval
type: pattern
domains: [reliability]
status: stable
brief: "The orchestrator evaluates a subagent's results against the objective and issues targeted follow-ups before accepting, passing why the information is needed."
order: 20
implements: ["[[observable-failure]]"]
requires: ["[[orchestrator]]", "[[acceptance-criterion]]"]
related_to: ["[[local-mediation-design-pattern]]"]
---

# Iterative retrieval

After a subagent returns results, the orchestrator evaluates their completeness against the objective — not merely against the literal query that was issued — and sends targeted follow-up queries before accepting the result, within a bounded number of refinement cycles. The orchestrator always passes the objective context down to the subagent: why the information is needed, not only what is being asked, so the subagent can judge relevance rather than match keywords.

Interposing the orchestrator's evaluation between a stochastic subagent's output and its downstream use is the reliability analogue of local mediation's deterministic checkpoint between a model's output and any consequence.
