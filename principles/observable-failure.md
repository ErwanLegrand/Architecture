---
id: observable-failure
title: Observable failure
type: principle
domains: [reliability]
status: stable
brief: "Every failure must be detectable, attributable, and surfaced promptly; silent wrong output is worse than a loud error."
order: 12
related_to: ["[[no-agency-without-auditability-principle]]"]
---

# Observable failure

Every failure in the system must be detectable, attributable to a specific step, and surfaced promptly to the component responsible for recovery. A step that produces wrong output without signalling an error is worse than one that fails loudly: a silent failure is invisible to retries, circuit breakers, critics, and escalation policies, all of which can act only on failures they can observe. A failure the orchestrator cannot see is a failure it cannot recover from.

Observable failure is the reliability counterpart of auditability. Where the audit requirement exists to make every state change forensically reconstructable, observability exists to make every failure operationally actionable; the two share the demand that the system emit a faithful record of what happened, and differ in what that record is for. Verification depends on it directly — a critic cannot evaluate what it cannot observe.
