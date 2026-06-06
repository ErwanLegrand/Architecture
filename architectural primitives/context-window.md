---
id: context-window
title: Context window
type: primitive
domains: [performance]
status: stable
brief: "The total token capacity of a single model invocation, covering system prompt, history, tool outputs, and response."
order: 24
related_to: ["[[scope-limiting]]"]
---

# Context window

The total token capacity available to a single model invocation, spanning the system prompt, the conversation history, tool outputs, and the space reserved for the response. It is a physical constraint with performance consequences: models attend less reliably to content in the middle of a long window, and headroom must be reserved for tool outputs that arrive partway through a turn. It is the constraint that scope limiting, context compaction, and token budgeting each exist to manage.
