---
id: shared-state-store
title: Shared state store
type: primitive
domains: [reliability, performance]
status: stable
brief: "External medium through which agents coordinate by reading their input slice and writing their output slice, without using each other's context windows."
order: 21
related_to: ["[[local-mediation-design-pattern]]"]
---

# Shared state store

An external medium — file system, database, or memory service — through which multiple agents coordinate without occupying each other's context windows. Each agent reads its input slice and writes its output slice; the orchestrator owns the structure of the store. Because coordination passes through a store the orchestrator controls rather than through serialization into a shared conversation, the agents stay scope-limited and their histories stay independent.

Routing coordination through orchestrator-owned infrastructure the agents cannot bypass is the reliability and performance analogue of local mediation, which routes tool use through framework-owned infrastructure the model cannot bypass.
