# Deterministic agents (computational nature axis)

Agents implemented as pure code with deterministic behavior: given the same input, they produce the same output and the same side effects, modulo declared sources of nondeterminism (clock, RNG with recorded seed, etc.). They are not language-model-mediated.

Deterministic agents participate in the orchestration graph as peers of stochastic agents — same node interface, same lifecycle, same place in the FSM — but without the probabilistic and adversarial-input properties that make stochastic agents subject to the suborned model principle. In a graph or FSM, any step that does not require probabilistic inference should be a deterministic agent; this is the practical expression of the least LLM principle at the node level.

Deterministic agents remain subject to:

- **Least privilege**: scope and capability footprint are minimized at the node level.
- **Validated interfaces**: input and output are schema-checked at the boundaries.
- **Auditability**: their invocations are recorded as part of the orchestration trace, with input, output, side effects, and code version captured. The audit content differs from a stochastic agent's (no model input or output to record) but the principle that every state-changing invocation is reconstructible from logs applies equally.

They are *not* subject to the suborned model principle (there is no model to suborn) nor to the Byzantine model design pattern in the form applied to stochastic agents (no adversarial inference). However, their *inputs* may originate from stochastic agents, in which case those inputs must be treated as adversarial per the Byzantine pattern. The boundary between a stochastic agent and a downstream deterministic agent is exactly where the Byzantine treatment of model output is enforced: validation, parsing, and policy checks happen at that interface, performed by the deterministic agent on behalf of the framework.
