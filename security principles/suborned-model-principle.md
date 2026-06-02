---
id: suborned-model-principle
title: Suborned model principle
type: principle
domains: [security]
status: stable
---

# Suborned model principle

Any language model that processes input must be assumed to be induced into faithful cooperation with whatever adversarial instructions that input may carry — including instructions embedded in tool outputs, retrieved documents, prior conversation turns, or upstream model responses.

The term derives from the legal sense of *suborn* (to induce another party to commit a wrong) and reflects the mechanism by which prompt injection operates: the model is not malfunctioning when it follows injected instructions; it is functioning as designed, but its alignment has been redirected by an attacker through ordinary input channels.

The principle assumes the worst case: that on every invocation, the model is actively aligned with an adversary who has crafted some portion of its input. Consequently, no security property may be derived from the model's compliance, judgment, refusal behavior, or self-report. All trust must be externally enforced.

**Scope.** The principle applies to instruction-following models — language models and vision-language models — because the attack mechanism is the model treating attacker-controlled input as instructions to execute. Other model classes (embedding models, classifiers, speech-to-text, generative image models) have attack surfaces of their own but do not follow instructions in the same sense; they are covered by the least model principle and the Byzantine model design pattern but not by the suborned model principle specifically.
