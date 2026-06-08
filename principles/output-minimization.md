---
id: output-minimization
title: Output minimization
type: principle
domains: [performance]
status: stable
brief: "Output token volume is a cost driver — of price, latency, and downstream context pressure — and so a design variable, not a style preference."
order: 20
mitigates: ["[[unbounded-resource-consumption]]"]
related_to: ["[[right-model-for-task]]", "[[stable-prefix]]"]
---

# Output minimization

Both input and output tokens are costs, and output volume is a design variable rather than a matter of style. The number of tokens a component emits affects price (output tokens are billed), latency (generation time scales with length), and the pressure on the next turn's context window (this turn's output becomes next turn's input). All three are reduced by explicit output-volume constraints imposed at the infrastructure or behavioural level, without loss of technical substance.

Minimizing output is the output-side complement of right model for task, which addresses cost on the input side; together they bound the two halves of an invocation's token cost.
