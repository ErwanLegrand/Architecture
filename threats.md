# Threats

Threats are the failure modes the framework defends against. Unlike principles, patterns, and primitives — which describe what to build — a threat describes what can go wrong: an adversarial exploit or a reliability failure mode that the other concepts exist to mitigate. Each threat is reached by the `mitigates` edges authored on the concepts that defend against it.

The table below is generated from each definition's frontmatter by `tools/gen-index.py`; do not edit it by hand. Full definitions live under [`/threats/`](/threats/).

<!-- gen:threat:start (generated from frontmatter by tools/gen-index.py — do not edit by hand) -->
| Threat | Domain | Brief | Full Definition |
| --- | --- | --- | --- |
| **Ambient authority abuse** | security | A component exercises authority attached to its identity or environment rather than carried by an explicit grant, enabling unintended use. | [→](/threats/ambient-authority-abuse.md) |
| **Confused deputy problem** | security | A program with authority is tricked by a less-privileged requester into misusing that authority on the requester's behalf. | [→](/threats/confused-deputy-problem.md) |
| **Prompt injection** | security | Adversarial content in an agent's input induces it to misuse its tools or authority on the attacker's behalf — a confused deputy in instruction-following models. | [→](/threats/prompt-injection.md) |
| **Unbounded resource consumption** | security, reliability, performance | An agent loop without enforced caps on iterations, tokens, retries, or wall-clock consumes compute, context, and cost without bound — through misconfiguration or adversarial input that drives consumption to deny service. | [→](/threats/unbounded-resource-consumption.md) |
| **Data poisoning** | security | Corruption of a persistent data source a model relies on — training or fine-tuning data, a RAG corpus, agent memory, or persisted tool output — so the model later produces attacker-chosen behavior across many invocations. | [→](/threats/data-poisoning.md) |
| **Model poisoning** | security | The model itself is compromised — a backdoor baked in by a poisoned training process, or weights tampered with or substituted in the supply chain — so it behaves adversarially independently of its input. | [→](/threats/model-poisoning.md) |
<!-- gen:threat:end -->
