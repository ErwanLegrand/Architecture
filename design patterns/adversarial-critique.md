---
id: adversarial-critique
title: Adversarial critique
type: pattern
domains: [reliability]
status: stable
brief: "A critic that attempts to refute rather than approve the output — Socratic questioning and Popperian falsification — surfacing failures a confirmatory review would pass."
order: 11
specializes: ["[[review-and-critique-loop]]"]
reduces: ["[[step-reliability-compounding]]"]
related_to: ["[[byzantine-model-design-pattern]]"]
---

# Adversarial critique

A specialization of the review-and-critique loop in which the critic's objective is to *refute* the output rather than to confirm it. Instead of checking that the output appears to satisfy its criteria, the critic builds the strongest case against it: it asks the questions whose answers would expose an unstated assumption (Socratic questioning) and seeks the observation or test that would falsify the claim (Popperian falsification). An output that survives a genuine attempt at refutation is more reliable than one that merely passes a confirmatory check, because confirmatory review is biased toward accepting plausible-but-wrong results.

The stance is deliberately adversarial to counter the failure mode of a critic that rubber-stamps a fluent answer. By raising the effective reliability of the step it guards, adversarial critique reduces the compounding degradation of the chain it sits in; its independence from the generator is the same property the Byzantine model pattern requires of any verifier.
