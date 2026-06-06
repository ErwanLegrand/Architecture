---
id: review-and-critique-loop
title: Review-and-critique loop
type: pattern
domains: [reliability]
status: stable
brief: "A generator produces output, a separate critic evaluates it against explicit criteria, and the generator revises until criteria pass or a limit is reached."
order: 10
implements: ["[[step-reliability-compounding]]", "[[observable-failure]]"]
requires: ["[[iteration-limit]]", "[[termination-condition]]"]
related_to: ["[[byzantine-model-design-pattern]]"]
---

# Review-and-critique loop

A generator component produces an output; a separate critic component evaluates that output against explicit acceptance criteria; if the criteria are not met the critic returns specific feedback and the generator revises. The loop terminates when the criteria pass, when the iteration limit is reached, or by escalation. Separating generation from evaluation raises the reliability of the produced output above what a single generative pass achieves, because the critic can reject a class of errors the generator is prone to repeat — a direct application of engineering reliability at the node rather than hoping a single pass succeeds.

The critic must be able to see what it is evaluating: the loop depends on observable failure, and it is bounded by the same iteration-limit and termination-condition machinery as any other loop. Establishing trust in an output through an independent evaluator that shares no generation context is structurally the same move as the Byzantine model pattern's independent verification, applied here for output quality rather than for adversarial containment.
