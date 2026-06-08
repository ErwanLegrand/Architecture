---
id: termination-condition
title: Termination condition
type: primitive
domains: [reliability]
status: stable
brief: "An explicit predicate the loop infrastructure evaluates each iteration, covering both the success and the failure terminals."
order: 12
---

# Termination condition

An explicit, evaluatable predicate that the loop infrastructure checks after each iteration to decide whether the loop continues. It may be satisfied by an acceptance criterion being met, an iteration limit being reached, a budget being exhausted, or an explicit stop signal being received. A complete termination condition covers both terminals: a predicate that matches only success is not a termination condition, because a loop that can recognise success but not failure does not reliably halt.
