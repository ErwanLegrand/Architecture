---
id: prompt-cache
title: Prompt cache
type: primitive
domains: [performance]
status: stable
brief: "A provider-side cache keyed on the stable prefix of the window; hits avoid re-encoding the prefix, cutting latency and cost."
order: 26
related_to: ["[[stable-prefix]]"]
---

# Prompt cache

A provider-side cache keyed on the stable prefix of the context window. A cache hit avoids re-encoding that prefix on a subsequent turn, reducing both the latency and the cost of the turn substantially. It requires the prefix to be stable across turns, with dynamic content appended after the cached section; a change anywhere in the prefix invalidates the cache from the point of change onward.
