---
id: circuit-breaker
title: Circuit breaker
type: primitive
domains: [reliability]
status: stable
brief: "Stops requests to a failing downstream after repeated failures, making persistent failure visible instead of masking it with endless retries."
order: 17
implements: ["[[observable-failure]]"]
mitigates: ["[[unbounded-resource-consumption]]"]
---

# Circuit breaker

A component that stops issuing requests to a downstream service after a threshold of consecutive failures. It remains open for a cooldown period, then admits a single probe request: the probe's success closes the breaker and resumes normal traffic, its failure restarts the cooldown. By refusing to keep calling a service that is persistently failing, the breaker converts an unbounded sequence of masked retries into an explicit, observable failure signal that recovery logic can act on. It opens when a backoff-governed retry sequence has been exhausted without success.
