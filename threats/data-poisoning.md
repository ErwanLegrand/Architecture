---
id: data-poisoning
title: Data poisoning
type: threat
domains: [security]
status: stable
brief: "Corruption of a persistent data source a model relies on — training or fine-tuning data, a RAG corpus, agent memory, or persisted tool output — so the model later produces attacker-chosen behavior across many invocations."
order: 5
related_to: ["[[prompt-injection]]"]
---

# Data poisoning

A failure mode in which an adversary corrupts data the system relies on to shape a model's behavior or decisions — training and fine-tuning datasets, retrieval (RAG) corpora, an agent's long-term memory or knowledge store, or persisted tool outputs — so that the model later produces attacker-chosen behavior. The corruption is introduced once, into a source the system trusts to be stable, and takes effect whenever that source is read.

It is distinct from prompt injection, though the two meet: injection manipulates a single live invocation through adversarial instructions in the current input, whereas data poisoning corrupts a *persistent* source so that the manipulation recurs across many future invocations and may carry no adversarial-looking content at the moment of inference. Poisoning the data used to train or fine-tune a model is, further, the mechanism by which data poisoning becomes model poisoning — the corruption is baked into the weights. The structural remedy is to treat ingested and retrieved data as `Untrusted` provenance, validate it at declassification against closed schemas, isolate the agents that handle untrusted data from any sensitive capability, and verify the integrity and source of a corpus before relying on it.
