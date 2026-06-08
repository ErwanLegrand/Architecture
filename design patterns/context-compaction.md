---
id: context-compaction
title: Context compaction
type: pattern
domains: [performance]
status: stable
brief: "At a threshold or logical boundary, replace full history with a structured summary, freeing context while retaining active state."
order: 28
requires: ["[[compaction-boundary]]", "[[compacted-summary]]"]
mitigates: ["[[unbounded-resource-consumption]]"]
related_to: ["[[checkpoint-resume]]"]
---

# Context compaction

At a configured threshold or a logical workflow boundary, the full conversation history is replaced with a structured summary that retains only the active task state and the essential decisions. This frees a large fraction of the context window and lets a long-running agent continue without exhausting it. Compaction is performed at logical boundaries — after a plan is approved, after a phase commits, before a large fan-out of subagents — so that the discarded history is genuinely stale rather than merely large.

Because the summary necessarily omits detail, state is checkpointed before compacting, so that resuming from the checkpoint can recover anything the summary dropped.
