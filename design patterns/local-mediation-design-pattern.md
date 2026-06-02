---
id: local-mediation-design-pattern
title: Local mediation design pattern
type: pattern
domains: [security]
status: stable
enables: ["[[byzantine-model-design-pattern]]"]
constrains: ["[[stochastic-agents]]"]
---

# Local mediation design pattern

The structural constraint that all tool use by stochastic agents must pass through the local framework's deterministic mediation layer. *Provider-side connectors* — model-vendor features that allow the model to invoke external services directly from the vendor's infrastructure, without the local framework seeing the request — are incompatible with the framework's security guarantees and excluded by this pattern.

The pattern is the precondition that makes the [Byzantine model design pattern](/design%20patterns/byzantine-model-design-pattern.md) operational. Byzantine treatment assumes the framework can see and validate every model output before any action is taken; provider-side connectors break this assumption by letting the model take actions inside the vendor's deployment, before any output the framework can examine. Without local mediation, the framework's external enforcement, capability bounds, audit path, and validation surface are all silently bypassed for those tool calls. The [suborned model principle](/security%20principles/suborned-model-principle.md)'s blast radius is no longer bounded by what the framework permits after the fact, because some actions are no longer "after the fact" from the framework's perspective.

In practice:

- **Mediation boundary on local infrastructure.** Every tool invocation originates from deterministic code running inside the framework, in response to validated model output. The model produces a request; the framework parses it, applies policy, dispatches the tool with bounded arguments, and records the invocation. The model never invokes a tool directly.
- **Text-in / text-out provider interface.** The interface to model providers is restricted to inference: input goes in, generated tokens come out. Any provider feature that performs actions during inference — web access, code execution, file retrieval, third-party API calls, agent-like autonomous loops, bundled connectors — is disabled, refused, or excluded at model selection time.
- **No trust in provider-side audit.** Even where providers offer logs or traces of internal connector use, those logs are not part of the framework's trust kernel; they live on infrastructure the framework does not control and cannot verify. Auditability must be satisfied locally, by the framework's own records of every mediated invocation. Relying on provider-side audit would contradict [Kerckhoffs's principle](/security%20principles/kerckhoffs-principle.md) by making a security property depend on the provider's internal infrastructure.
- **Model selection as a security decision.** The choice of model provider is constrained not only by model capability but by whether the provider's deployment mode supports text-in / text-out operation without bundled action capabilities. Self-hosted models, open-weight deployments, and API offerings that expose only inference are compatible; offerings that bundle connectors as a non-disableable feature are not.

**Scope.** The pattern is specific to stochastic agents and their tool use. Deterministic agents are not affected — they have no provider relationship and no probabilistic inference layer to bypass. The pattern applies regardless of model class: an LLM with bundled web search, a VLM with bundled image-source access, an embedding service that performs retrieval as a bundled feature, or a speech-to-text service with bundled transcription post-processing are all subject to it. The criterion is structural — does the model take actions the local framework does not see? — not class-specific.
