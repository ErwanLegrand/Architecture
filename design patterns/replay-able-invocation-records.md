# Replay-able invocation records

Capture enough state — model identity and version, sampling parameters, full input as the model saw it, and any class-specific configuration (prompt template version for LLMs, decoding parameters, embedding dimension, classifier threshold) — that any invocation can be deterministically re-executed from its log entry for forensic analysis or debugging. For deterministic agents, the analog is capturing input, code version, and declared nondeterminism sources.
