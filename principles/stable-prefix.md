---
id: stable-prefix
title: Stable prefix
type: principle
domains: [performance]
status: stable
brief: "Keep stable context at the start of the window so the prompt cache stays warm; reordering stable sections across turns destroys cache hits."
order: 19
requires: ["[[prompt-cache]]"]
---

# Stable prefix

Stable context — the system prompt, always-on rules, skill metadata — is kept at the beginning of the context window, and new dynamic content is appended after it rather than interleaved into it. Provider prompt caches are keyed on the prefix of the window, so reformatting or reordering a stable section across turns invalidates the cache from the point of change onward and forces the prefix to be re-encoded, inflating both latency and cost.

Context-loading order is therefore a performance variable, not a cosmetic one. New content extends the stable prefix; it does not rewrite it.
