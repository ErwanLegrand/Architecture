---
id: react-loop
title: ReAct loop
type: pattern
domains: [reliability]
status: stable
brief: "At each step the agent produces a Thought, an Action, and receives an Observation, grounding reasoning in environment feedback."
order: 19
instantiates: ["[[agent-loop]]"]
implements: ["[[observable-failure]]"]
requires: ["[[termination-condition]]"]
---

# ReAct loop

At each step of the loop the agent produces a structured thought, then an action, then receives an observation from the environment, then reasons again. Neither pure chain-of-thought (reasoning without grounding) nor pure tool use (acting without reasoning) achieves reliable task completion; interleaving them grounds each inference in real feedback and forces implicit assumptions to be made explicit before the next action is taken.

The pattern is an instantiation of the agent loop with an explicit thought–action–observation structure. The observation step is where errors from the environment enter the agent's reasoning, so the pattern depends on those failures being observable in the first place.
