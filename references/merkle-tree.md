---
id: merkle-tree
title: Merkle tree
type: reference
domains: [security]
status: stable
brief: "A hash tree giving a single-root commitment to a large or sequenced dataset with logarithmic inclusion and consistency proofs; full definition lives in the cryptography-engineering knowledge base."
external_ref: "cryptography-engineering:merkle-tree"
---

# Merkle tree

A tree of hashes whose root is a compact commitment to a large or sequenced dataset, supporting O(log n) proofs that a given element is included and that one version of the set extends another without modification. It generalizes the linear hash chain used for tamper-evident logs, and it lets an attestation over a large artifact localize *which* shard changed rather than only that something did. Its construction and security analysis belong to cryptography engineering and are defined in that knowledge base.

This is a reference node: a thin pointer that anchors cross-knowledge-base edges so the in-vault graph resolves at the seam. Its full definition is external — see `external_ref`.
