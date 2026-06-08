---
id: n-version-consensus
title: N-version consensus
type: pattern
domains: [reliability]
status: stable
brief: "Generate a step's output independently n times and select the agreed result, reducing residual error far faster than a single pass."
order: 13
reduces: ["[[step-reliability-compounding]]"]
related_to: ["[[byzantine-model-design-pattern]]"]
mitigates: ["[[model-poisoning]]"]
---

# N-version consensus

A pattern in which a step is executed independently n times — by separate invocations, and where possible by diverse implementations — and the result is chosen by agreement among the outputs rather than taken from any single run. Independent errors that would each pass undetected in a single pass are exposed as disagreement, and the residual error rate of the agreed result falls far faster than the single-pass rate as n grows, approaching the order of p^⌈n/2⌉. The pattern trades additional cost for reliability and is justified where a step's failure is expensive enough to warrant the redundancy.

Consensus across independent instances that share no context is the constructive form of the Byzantine model pattern's assumption that no single instance should determine an outcome; by arresting independent errors before they propagate, it reduces the compounding degradation of the chain. Run over independent model instances, it also exposes a poisoned model whose backdoor fires in only some of them; it gives no protection, however, against an identical compromise shared across every instance — the same backdoored weights, or a single poisoned upstream — which agrees with itself and so surfaces no disagreement to detect.
