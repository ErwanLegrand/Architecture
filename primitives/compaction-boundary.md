---
id: compaction-boundary
title: Compaction boundary
type: primitive
domains: [performance]
status: stable
brief: "A token threshold, set below the context ceiling, that triggers compaction; also fires at logical workflow boundaries."
order: 25
requires: ["[[context-window]]"]
---

# Compaction boundary

A configurable token threshold — set below the context-window ceiling to leave headroom for tool outputs — at which context compaction is triggered. It also fires at logical workflow boundaries regardless of current occupancy, so that compaction happens at coherent points rather than mid-task. It is the trigger the context-compaction pattern acts on.
