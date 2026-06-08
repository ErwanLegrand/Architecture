---
id: capability-based-security-design-pattern
title: Capability-based security design pattern
type: pattern
domains: [security]
status: stable
brief: "Access to a resource is governed by possession of an unforgeable capability naming the object and permitted operations; authority travels with the reference, not the identity."
order: 9
implements: ["[[least-privilege-principle]]"]
mitigates: ["[[confused-deputy-problem]]", "[[ambient-authority-abuse]]"]
related_to: ["[[local-mediation-design-pattern]]", "[[provenance-tracking-design-pattern]]", "[[role-typed-agent-separation-design-pattern]]"]
---

# Capability-based security design pattern

Access to a resource is governed by possession of a *capability*: an unforgeable token that names a specific object together with the operations permitted on it. Possessing the capability is both necessary and sufficient for the access it describes; authority travels with the reference handed to a component, not with the component's identity or ambient environment. A component can exercise only the authority it has been explicitly given, and can delegate only by passing on a capability it already holds.

Because authority is bound to each reference rather than attached to identity, the pattern removes the ambient authority that makes the confused-deputy problem possible: a deputy holds only the capabilities it was handed for the task at hand, so it cannot be induced into exercising authority it was never given. It is the classical structural realization of least privilege. In the agentic setting it underlies role-typed agent separation — Core agents hold capabilities that Edge agents do not — and composes with local mediation, which is the layer at which the framework enforces the capability each tool invocation requires.
