---
id: acceptance-criterion
title: Acceptance criterion
type: primitive
domains: [reliability]
status: stable
brief: "An explicit, evaluatable definition of task completion that distinguishes a result merely produced from one that is correct."
order: 23
related_to: ["[[termination-condition]]", "[[review-and-critique-loop]]"]
---

# Acceptance criterion

An explicit, evaluatable definition of what it means for a task to be complete. It must distinguish a result that is merely produced — code that compiles, a file that was written — from one that is correct — code that passes its tests, a file whose contents satisfy the requirement. An acceptance criterion that checks only production is the primary source of premature-termination and incomplete-verification failures, because it lets a loop stop on the appearance of completion rather than its substance.

It is the success terminal that a termination condition tests and the standard a critic evaluates an output against.
