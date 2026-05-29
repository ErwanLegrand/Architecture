# Stochastic agents (computational nature axis)

Agents whose computation involves probabilistic model inference. A stochastic agent's output is sampled from a probability distribution conditioned on its input; the same input may produce different outputs across invocations. The model class may be a language model, vision-language model, embedding model, classifier, speech-to-text, or any other learned model; the stochastic-agent designation applies uniformly.

Stochastic agents are the locus of the framework's model-mediated capability. They are subject to:

- The **suborned model principle**, where applicable: instruction-following stochastic agents (LLM-based, VLM-based) are assumed actively aligned with an adversary on every invocation. Non-instruction-following stochastic agents are subject to the Byzantine pattern but not to the suborned model principle in its specific form.
- The **Byzantine model design pattern**: outputs are validated, authority is externally bounded, mutual suspicion is the default in multi-agent composition. The validation specifics depend on the model class.
- The **local mediation design pattern**: all tool use passes through the framework's deterministic mediation layer. Provider-side connectors that let the model act inside the vendor's deployment, before any output the framework can examine, are excluded — they would bypass the Byzantine pattern's precondition that every output is seen and validated before any action.
- The **no agency without auditability principle**: every invocation is recorded forensically before its output is permitted to cause a state change.
- The **least model principle**: a stochastic agent is introduced only when no deterministic implementation would suffice. The default node type is deterministic; choosing stochastic is a deliberate decision requiring justification.
