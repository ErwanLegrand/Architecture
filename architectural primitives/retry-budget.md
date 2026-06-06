---
id: retry-budget
title: Retry budget
type: primitive
domains: [reliability]
status: stable
brief: "A per-turn cap on total retry attempts across all tool calls, bounding aggregate retry cost independently of per-call limits."
order: 15
---

# Retry budget

A ceiling on the total number of retry attempts permitted across all tool calls within a single agent turn. It is distinct from a per-call maximum: a per-call limit bounds how often one operation is retried, while the retry budget bounds the aggregate, so that many independently-retrying calls cannot together drive a turn into a large multiple of its intended cost. Without it, a single misconfigured tool can consume a turn in retries. The budget caps the resource expenditure that retries specifically can incur, separately from the per-call timing governed by backoff.
