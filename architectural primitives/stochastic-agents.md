# Stochastic agents (computational nature axis)

Agents whose computation involves probabilistic language-model inference. A stochastic agent's output is sampled from a probability distribution conditioned on its input; the same input may produce different outputs across invocations.

Stochastic agents are the locus of the framework's LLM-mediated capability. They are subject to:

- The **suborned model principle**: the model is assumed actively aligned with an adversary on every invocation.
- The **Byzantine model design pattern**: outputs are validated, authority is externally bounded, mutual suspicion is the default in multi-agent composition.
- The **no agency without auditability principle**: every invocation is recorded forensically before its output is permitted to cause a state change.
- The **least LLM principle**: a stochastic agent is introduced only when no deterministic implementation would suffice. The default node type is deterministic; choosing stochastic is a deliberate decision requiring justification.
