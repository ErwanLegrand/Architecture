---
id: human-in-the-loop
title: Human-in-the-loop
type: pattern
domains: [reliability]
status: stable
brief: "Pause the workflow at high-stakes checkpoints for human review or approval before proceeding."
order: 22
implements: ["[[observable-failure]]"]
related_to: ["[[defense-in-depth]]", "[[no-agency-without-auditability-principle]]"]
---

# Human-in-the-loop

The workflow pauses at high-stakes checkpoints for a human to review, approve, or correct before it proceeds. It is required when the next action is irreversible, when its blast radius is large, when the agent's confidence falls below a threshold, or when policy mandates human authorization. The pause turns a failure that would otherwise be silent into one a human can catch and stop.

Human review before a state change is both the strongest detective layer in a defense-in-depth stack and the strongest expression of auditability, because human judgement is interposed before the consequence rather than recorded after it.
