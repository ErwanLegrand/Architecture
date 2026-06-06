---
id: step-reliability-compounding
title: Step reliability compounding
type: principle
domains: [reliability]
status: stable
brief: "In an unverified chain of stochastic steps end-to-end reliability is the product of per-step reliabilities; verification gates break this multiplicative decay."
order: 10
---

# Step reliability compounding

The end-to-end success rate of a chain of independent stochastic steps is the product of the per-step success rates. A workflow of n steps each succeeding with probability p succeeds end-to-end with probability pⁿ: ten steps at 0.95 each yield ≈0.60, twenty steps ≈0.36. Per-step reliability therefore dominates end-to-end reliability, and lengthening an unguarded pipeline degrades it geometrically. Reliability must be engineered at each node; it cannot be recovered by orchestration layered over sloppy steps.

This multiplicative model holds only for a chain of *independent generative steps that each fail without correction*. It does not describe a pipeline that contains verification gates. A verification gate is a step whose purpose is to detect or correct earlier output rather than to generate new state, and its presence changes the arithmetic:

- A *deterministic* gate — static analysis, type checking, schema validation, a passing test — decides a class of errors with certainty rather than probability, partitioning failures into detected and undetected and removing the assumption that every step contributes an independent sub-unity factor.
- A *corrective loop* — a critic that revises a generator's output, iterative self-refinement, adversarial falsification — raises the effective success probability of the step it guards before that step's errors propagate downstream.
- *Consensus over independent samples* — producing a step's output several times and selecting the agreed result — drives the residual error rate down far faster than a single pass, approaching the order of p^⌈n/2⌉ rather than degrading as pⁿ.

The principle therefore has two faces. An unguarded chain of stochastic steps degrades multiplicatively and must be kept short with each step made highly reliable. A chain interleaved with verification gates can sustain many more steps at a given end-to-end reliability, because the gates arrest error propagation instead of compounding it. Designing for reliability means placing verification after the steps whose failure is most costly, not merely minimizing the step count.
