---
id: pass-at-k-evaluation
title: pass@k / pass^k evaluation
type: pattern
domains: [reliability]
status: stable
brief: "Choose pass@k or pass^k to match the task's failure tolerance: at least one of k attempts succeeds, versus all k must succeed."
order: 26
related_to: ["[[step-reliability-compounding]]", "[[byzantine-model-design-pattern]]", "[[n-version-consensus]]"]
---

# pass@k / pass^k evaluation

An evaluation chooses the success metric that matches the task's tolerance for failure. Under **pass@k**, at least one of k attempts must succeed — appropriate where retries are acceptable and an occasional failure is cheap. Under **pass^k**, all k attempts must succeed — appropriate for safety-critical or consistency-required behaviour, where any single failure is unacceptable. Pass^k is a demanding bar: a per-attempt success probability of 0.70 yields only 0.34 across three independent attempts.

Pass^k is the evaluation analogue of the Byzantine assumption that no single instance may be trusted on its own: it requires every independent instance to succeed rather than accepting a majority. The two metrics quantify the two faces of step reliability compounding — pass@k rewards a chain that can retry, pass^k measures one that cannot afford a single bad step.
