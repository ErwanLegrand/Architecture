---
id: hash-chained-logs
title: Hash-chained logs
type: pattern
domains: [security]
status: stable
brief: "Append-only logs where each entry is cryptographically bound to its predecessor."
order: 7
protects: ["[[no-agency-without-auditability-principle]]"]
---

# Hash-chained logs

Append-only logs in which each entry is cryptographically bound to its predecessor, making after-the-fact tampering detectable. It makes the audit trail required by the [no agency without auditability principle](/security%20principles/no-agency-without-auditability-principle.md) tamper-evident: an adversary with write access cannot alter or excise a past record without breaking the chain and revealing the edit.
