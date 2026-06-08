---
id: worktree
title: Worktree
type: primitive
domains: [reliability]
status: stable
brief: "An isolated filesystem checkout that lets multiple agents make overlapping code changes in parallel without conflict."
order: 22
related_to: ["[[subagent]]"]
---

# Worktree

An isolated filesystem checkout — for example a git worktree — that lets multiple agents make overlapping changes to a shared codebase in parallel without colliding on the filesystem. Each agent sees its own copy of the repository, and changes are merged back through the normal review process. It supplies the filesystem isolation a subagent needs when its task is to modify code rather than only to read it.
