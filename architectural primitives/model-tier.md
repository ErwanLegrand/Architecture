---
id: model-tier
title: Model tier
type: primitive
domains: [performance]
status: stable
brief: "A categorical classification of model capability and cost — fast, mid, high — assigned in agent profile metadata, not selected at runtime."
order: 27
related_to: ["[[least-model-principle]]"]
---

# Model tier

A categorical classification of model capability and cost — fast and cheap, mid, high-capability — that maps to concrete model identities at deployment time. The tier is recorded in an agent's profile metadata and fixed when the agent is created rather than chosen dynamically during a session, so that the cost profile of a workflow is declared in advance rather than emerging unpredictably from runtime choices.
