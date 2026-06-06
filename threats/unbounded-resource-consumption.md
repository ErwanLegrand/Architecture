---
id: unbounded-resource-consumption
title: Unbounded resource consumption
type: threat
domains: [security, reliability, performance]
status: stable
brief: "An agent loop without enforced caps on iterations, tokens, retries, or wall-clock consumes compute, context, and cost without bound — through misconfiguration or adversarial input that drives consumption to deny service."
order: 4
related_to: ["[[explicit-termination]]"]
---

# Unbounded resource consumption

A failure mode in which a loop or call path governs its resource use by the agent's own judgement rather than by an externally enforced ceiling, and so can consume iterations, tokens, context, retries, and wall-clock without bound. A single misconfiguration — a success predicate that never fires, a tool returning unexpectedly large output, or many independently-retrying calls compounding — drives a run into an unbounded multiple of its intended cost, exhausting the context window or the budget and, in the limit, never halting. The agent cannot recover by itself: an instance that has lost the ability to recognise its own lack of progress cannot be the thing that stops it.

Untrusted input can *induce* this on purpose: content that expands the task, inflates tool output, or provokes retry storms turns resource consumption into a denial-of-service vector against the agent and the downstreams it calls. The structural remedy is bounds enforced outside the agent on every terminal — iteration count, token spend, retry attempts, and time — so that an agent which cannot recognise its own runaway state is still halted, and the exhaustion is surfaced as an observable failure rather than silently absorbed. Against the induced, adversarial form, these per-run terminals are complemented by bounding the rate and volume of work admitted in the first place, so that a flood is shed rather than served.
