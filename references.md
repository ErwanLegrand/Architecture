# References

Reference nodes are pointers to concepts defined in a *separate* knowledge base (for instance, cryptographic primitives, which belong to cryptography engineering). Their full definitions live in that knowledge base; the thin pointers here exist so cross-knowledge-base edges resolve and the graph does not dangle at the seam. Each carries an `external_ref` naming the owning KB and node id. See [AGENTS.md](/AGENTS.md) for the convention.

The table below is generated from each pointer's frontmatter by `tools/gen-index.py`; do not edit it by hand. Pointer nodes live under [`/references/`](/references/).

<!-- gen:reference:start (generated from frontmatter by tools/gen-index.py — do not edit by hand) -->
| Reference | Domain | Brief | Full Definition |
| --- | --- | --- | --- |
| **Cryptographic hash** | security | A collision- and preimage-resistant hash function; full definition lives in the cryptography-engineering knowledge base. | [→](/references/cryptographic-hash.md) |
| **Digital signature** | security | An asymmetric scheme for authenticity and integrity; full definition lives in the cryptography-engineering knowledge base. | [→](/references/digital-signature.md) |
| **Merkle tree** | security | A hash tree giving a single-root commitment to a large or sequenced dataset with logarithmic inclusion and consistency proofs; full definition lives in the cryptography-engineering knowledge base. | [→](/references/merkle-tree.md) |
<!-- gen:reference:end -->
