---
id: prompt-injection
title: Prompt injection
type: threat
domains: [security]
status: stable
brief: "Adversarial content in an agent's input induces it to misuse its tools or authority on the attacker's behalf — a confused deputy in instruction-following models."
order: 3
specializes: ["[[confused-deputy-problem]]"]
related_to: ["[[suborned-model-principle]]"]
---

# Prompt injection

Adversarial instructions placed in the data an instruction-following model processes induce the model to act on the attacker's behalf — exfiltrating data, invoking tools, or abandoning its assigned task — using whatever authority the agent holds. The injected content need not arrive through the user's prompt; it can be embedded in any untrusted data the model reads, including tool outputs, retrieved documents, and web pages.

It is the agentic instance of the confused-deputy problem: the model is the deputy, its granted tools are the authority, and the injected content is the requester that confuses it. It is the concrete mechanism the suborned model principle assumes on every invocation, and the reason an Edge agent that processes untrusted data is permitted no sensitive capability.
