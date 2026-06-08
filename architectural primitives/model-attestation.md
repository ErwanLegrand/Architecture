---
id: model-attestation
title: Model attestation
type: primitive
domains: [security]
status: stable
brief: "A verified binding of a model's identity, version, and weight integrity, checked by the harness before the model is admitted for use, detecting tampering or substitution of the weights."
order: 30
mitigates: ["[[model-poisoning]]"]
requires: ["[[cryptographic-hash]]", "[[digital-signature]]"]
composes_with: ["[[byzantine-model-design-pattern]]", "[[merkle-tree]]"]
related_to: ["[[kerckhoffs-principle]]"]
---

# Model attestation

A verified binding of a model's identity, version, and weight integrity — a cryptographic hash or signature over the weights together with a pinned version identifier — that the harness checks before the model is admitted for use and re-checks whenever the deployed model changes. It establishes that the model in use is the specific, audited artifact the system intends to run, so that tampering with or substitution of the weights is detected and refused rather than silently accepted. For a large or sharded artifact the commitment can be a Merkle root, so that a failed check also localizes which shard changed.

Attestation concerns *integrity*, not secrecy: consistent with [Kerckhoffs's principle](/principles/kerckhoffs-principle.md), the weights and version may be fully known to an adversary, yet the system must still verify that what it loaded is the artifact it attested. It does not vouch for how the model was trained — a correctly-signed but maliciously-trained model passes — so it composes with the [Byzantine model design pattern](/design%20patterns/byzantine-model-design-pattern.md): attestation closes the supply-chain substitution path before inference, while Byzantine validation contains whatever the admitted model then does.
