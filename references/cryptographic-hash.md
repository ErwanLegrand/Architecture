---
id: cryptographic-hash
title: Cryptographic hash
type: reference
domains: [security]
status: stable
brief: "A collision- and preimage-resistant hash function; full definition lives in the cryptography-engineering knowledge base."
external_ref: "cryptography-engineering:cryptographic-hash"
---

# Cryptographic hash

A function mapping arbitrary input to a fixed-length digest such that collisions and preimages are computationally infeasible to find. It is the substrate this framework relies on for tamper-evidence — binding each audit-log entry to its predecessor, and committing to model weights at load. Its construction and security analysis (collision and second-preimage resistance, length-extension, domain separation) belong to cryptography engineering and are defined in that knowledge base.

This is a reference node: a thin pointer that anchors cross-knowledge-base edges so the in-vault graph resolves at the seam. Its full definition is external — see `external_ref`.
