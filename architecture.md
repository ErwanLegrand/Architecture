# Agentic Architecture

This is the map of the framework for building agentic systems that are secure, reliable, and performant. It is intended as reference context for any agent or contributor working on the project. Definitions are normative: deviations require explicit justification. Each definition declares the domain(s) it speaks to — `security`, `reliability`, `performance` — in its frontmatter; a single concept may serve more than one.

The catalogue is organized by concept type, one generated index per type:

- **[Principles](/principles.md)** — foundational assumptions and goals; what the framework is for and what it refuses to compromise on.
- **[Patterns](/patterns.md)** — the structural responses that implement the principles.
- **[Primitives](/primitives.md)** — the building blocks the framework composes (carrying the agent taxonomy: the scope, computational-nature, and trust-position axes).
- **[Threats](/threats.md)** — the failure modes the other concepts exist to mitigate.
- **[References](/references.md)** — pointers to concepts defined in a separate knowledge base (e.g. cryptographic primitives).

Each index table is generated from definition frontmatter by `tools/gen-index.py`; the full definitions live in the matching folder. See [AGENTS.md](/AGENTS.md) for conventions, the relation vocabulary, and editing guidance.
