# Least LLM principle

The use of language-model-mediated decision-making is minimized in both extent and authority. Each component is implemented in deterministic code unless an LLM is genuinely required, and each LLM invocation is given the narrowest scope sufficient to perform its task.

The principle composes with least privilege along an orthogonal axis: where least privilege bounds authority per component, least LLM bounds the number of components that have LLM-mediated agency at all. Every place an LLM is used is a place prompt injection can manifest, so minimizing LLM use directly reduces attack surface.
