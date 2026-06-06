---
id: confused-deputy-problem
title: Confused deputy problem
type: threat
domains: [security]
status: stable
brief: "A program with authority is tricked by a less-privileged requester into misusing that authority on the requester's behalf."
order: 2
specializes: ["[[ambient-authority-abuse]]"]
related_to: ["[[least-privilege-principle]]"]
---

# Confused deputy problem

A failure mode in which a program that holds authority — the *deputy* — is induced by a less-privileged requester into exercising that authority on the requester's behalf, performing an action the requester could not perform directly. The deputy is not malicious; it is confused about whose authority it is acting under, because it receives the request and its authority from different sources and has no means to distinguish "do this for the requester" from "do this with my own privileges."

First described by Hardy, it is the canonical argument for capabilities: authority that travels with each reference, rather than ambient authority attached to the deputy's identity, removes the confusion. In an agentic system the deputy is an agent that holds tools or credentials, and the requester is the input that induces it to use them — which is why an agent exposed to untrusted data must hold no sensitive capability of its own.
