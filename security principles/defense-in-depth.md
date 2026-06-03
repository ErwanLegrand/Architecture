---
id: defense-in-depth
title: Defense in depth
type: principle
domains: [security]
status: stable
brief: "Security properties are enforced by multiple independent layers such that the failure of any single layer does not compromise the system."
order: 3
decomposes_into: ["[[no-agency-without-auditability-principle]]"]
---

# Defense in depth

Security properties are enforced by multiple independent layers — preventive, detective, and responsive — such that the failure of any single layer does not compromise the system. No single control is treated as sufficient. The [no-agency-without-auditability principle](/security%20principles/no-agency-without-auditability-principle.md) supplies the detective layer: it commits a forensically sufficient record before any state change, so that a failure of the preventive layers remains observable and reconstructable.
