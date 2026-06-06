---
id: write-ahead-audit
title: Write-ahead audit
type: pattern
domains: [security]
status: stable
brief: "Commit the invocation record before executing the authorized action, ensuring no unrecorded state changes."
order: 5
implements: ["[[no-agency-without-auditability-principle]]"]
---

# Write-ahead audit

Commit the invocation record before executing the action it authorizes, parallel to database write-ahead logging. A crash between record and action leaves no unrecorded state changes. It is the temporal mechanism of the [no agency without auditability principle](/principles/no-agency-without-auditability-principle.md): because the record is committed *before* the action, no authorized state change can precede its own audit entry.
