---
id: least-privilege-principle
title: Least privilege principle
type: principle
domains: [security]
status: stable
brief: "Every component is granted the minimum authority required to perform its function."
order: 2
mitigates: ["[[confused-deputy-problem]]"]
---

# Least privilege principle

Every component is granted the minimum authority required to perform its function, and no more. Authority is denied by default and explicitly granted; expansion of authority requires explicit justification, not implicit accumulation.

The confused-deputy problem is the failure this principle forecloses: a component granted only the authority its function requires cannot be induced into exercising authority it was never given.
