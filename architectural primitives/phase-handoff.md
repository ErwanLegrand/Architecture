---
id: phase-handoff
title: Phase handoff
type: primitive
domains: [reliability]
status: stable
brief: "A schema-validated artifact that carries one phase's output to the next phase's input, persisted before the next phase begins."
order: 20
requires: ["[[checkpoint-store]]"]
related_to: ["[[bridge-agents]]"]
---

# Phase handoff

A structured, schema-validated artifact — typically a file — that carries a phase's output to the next phase's input. It is persisted to the checkpoint store before the next phase begins, so the handoff survives a crash between phases. Validating the artifact against a schema at the boundary prevents a malformed output from one phase from corrupting the phases downstream of it.

The phase handoff is the reliability view of the same boundary the Bridge-agent primitive guards for trust: where a Bridge validates and declassifies before passing content from Untrusted to Trusted, a phase handoff validates structure before passing work from one phase to the next.
