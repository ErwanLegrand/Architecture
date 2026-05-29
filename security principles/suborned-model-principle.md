# Suborned model principle

Any language model that processes input must be assumed to be induced into faithful cooperation with whatever adversarial instructions that input may carry — including instructions embedded in tool outputs, retrieved documents, prior conversation turns, or upstream model responses.

The term derives from the legal sense of *suborn* (to induce another party to commit a wrong) and reflects the mechanism by which prompt injection operates: the model is not malfunctioning when it follows injected instructions; it is functioning as designed, but its alignment has been redirected by an attacker through ordinary input channels.

The principle assumes the worst case: that on every invocation, the model is actively aligned with an adversary who has crafted some portion of its input. Consequently, no security property may be derived from the model's compliance, judgment, refusal behavior, or self-report. All trust must be externally enforced.
