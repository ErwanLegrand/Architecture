---
id: parallel-worktree-isolation
title: Parallel worktree isolation
type: pattern
domains: [reliability]
status: stable
brief: "Give each agent making overlapping code changes its own filesystem checkout; coordinate through a store, not a shared context window."
order: 24
implements: ["[[stateless-subagent]]"]
requires: ["[[worktree]]", "[[shared-state-store]]"]
---

# Parallel worktree isolation

When several agents must make overlapping changes to a shared codebase in parallel, each is given an independent filesystem checkout — a worktree. Coordination happens through file I/O or a shared state store, never through a shared context window, and the orchestrator does not re-serialize the agents' outputs into its own growing history. Each agent works against its own copy and the results are merged back through the normal review process.

Isolating the filesystem per agent removes the write conflicts of parallel editing, and routing coordination through a store rather than a shared conversation removes the context-window race conditions that arise when parallel agents share state through one history.
