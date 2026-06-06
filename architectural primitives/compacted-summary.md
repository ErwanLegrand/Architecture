---
id: compacted-summary
title: Compacted summary
type: primitive
domains: [performance]
status: stable
brief: "A structured replacement for conversation history produced by compaction — current state, key decisions, artifacts in flight, open questions."
order: 28
related_to: ["[[checkpoint-store]]"]
---

# Compacted summary

A structured replacement for conversation history produced by the compaction process. It retains the current task state, the key decisions made, the artifacts in flight, and the open questions, in a structured rather than free-form shape so that later reasoning can reference it reliably. It is what compaction leaves in place of the history it discards; because it necessarily omits detail, state is checkpointed before compaction so nothing the summary drops is lost.
