---
id: sequential-phase-orchestration
title: Sequential phase orchestration
type: pattern
domains: [reliability]
status: stable
brief: "Chain specialized agents so each has one input and one output persisted as a handoff before the next phase begins."
order: 18
implements: ["[[stateless-subagent]]"]
requires: ["[[phase-handoff]]"]
related_to: ["[[role-typed-agent-separation-design-pattern]]"]
---

# Sequential phase orchestration

Specialized agents are chained so that each has exactly one clear input and produces exactly one clear output, persisted as a phase handoff before the next phase begins; each output becomes the next phase's input. Phases are not skipped, and intermediate reasoning is compacted at phase boundaries so that stale context does not accumulate across the chain. Because each phase's state is externalized in its handoff, the agents themselves remain stateless and any phase can be restarted from its input.

Decomposing work into single-function phases is the reliability counterpart of role-typed agent separation, which adds Core/Edge/Bridge trust constraints on top of the same narrow-function decomposition.
