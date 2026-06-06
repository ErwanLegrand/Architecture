---
id: ambient-authority-abuse
title: Ambient authority abuse
type: threat
domains: [security]
status: stable
brief: "A component exercises authority attached to its identity or environment rather than carried by an explicit grant, enabling unintended use."
order: 1
related_to: ["[[least-privilege-principle]]"]
---

# Ambient authority abuse

A class of failure in which a component acts with authority it holds *ambiently* — by virtue of its identity, role, or execution environment — rather than authority carried explicitly with each request. Because the authority is not bound to a specific request, the component cannot tell whether a given action is one it should perform on a requester's behalf or merely one it happens to be able to perform. Ambient authority is the precondition for the confused-deputy problem and for a wide range of privilege-escalation failures.

Capability-based security is the structural remedy: replacing ambient authority with unforgeable per-request grants removes the gap between what a component *may* do and what it has been *asked* to do.
