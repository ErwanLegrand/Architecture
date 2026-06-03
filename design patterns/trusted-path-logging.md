---
id: trusted-path-logging
title: Trusted-path logging
type: pattern
domains: [security]
status: stable
brief: "Write log entries through a channel outside the model's authority, to storage the model cannot modify."
order: 6
enforces: ["[[no-agency-without-auditability-principle]]"]
---

# Trusted-path logging

Write log entries through a channel outside the model's authority, to storage the model cannot reach or modify. The path from model output to committed log entry passes only through code in the trust kernel. This enforces the [no agency without auditability principle](/security%20principles/no-agency-without-auditability-principle.md)'s requirement that the record be written through a path outside the agent's authority — the integrity precondition without which an agent could forge or suppress the record of its own invocation.
