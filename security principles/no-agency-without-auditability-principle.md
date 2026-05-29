# No agency without auditability principle

No language model output may cause a state change in the system or its environment unless the framework has first committed a forensically sufficient record of the invocation that produced it.

The record must capture:

- The model's input as the model saw it (byte-for-byte, including system prompt, tool outputs, retrieved content, prior turns).
- The model's output verbatim, pre-parsing and pre-validation.
- The action the framework took, distinguished from what the model requested.
- The policy decision that authorized the action.
- The causal lineage linking this invocation to its triggers and downstream effects.
- The model identity and version, including sampling parameters and prompt template version.

The record must be written through a path outside the model's authority, to storage the model cannot modify. Audit is treated as part of the trust kernel of the framework, not as observability tooling: it is the detection layer of defense in depth, complementing the preventive controls implied by the Byzantine model design pattern.
