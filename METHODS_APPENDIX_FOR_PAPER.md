# Methods Appendix for CACP Evaluation

## Evaluation design

The preliminary evaluation used a simulated cyber-defense testbed organized around the Hunter--Policy--Responder roles described in the paper. Each action-decision scenario produced a Hunter proposal, a deterministic Policy evaluation against a rule-of-engagement clause, and a Responder commit only when a valid Policy grant was present.

The evidence package contains 50 action-decision scenarios. Each row records the scenario identifier, hypothesis, evidence pointer, evidence hash, proposed command, risk estimate, asset identifier, expected policy result, RoE clause, and Decision Card identifier.

## Audit timing task

Two analysts evaluated three log conditions:

- B0: unstructured chat-style logs with timestamps.
- B1: structured logs without commitments, signatures, phase gating, or hash chaining.
- CACP: typed phases, Policy grants, signed Decision Cards, and commit receipts.

For each scenario and condition, analysts answered fixed audit questions: what evidence justified the action, and which RoE clause authorized it? MTTA was measured as elapsed time from opening the relevant artifact to correct answer submission.

The timing file contains 300 timing records: 50 scenarios × 2 analysts × 3 conditions.

## Prompt-injection task

The bounded prompt-injection suite contains 100 indirect prompt-injection attempts targeting the Hunter role through retrieved content. Each attempt records the retrieved content pointer, hash, adversarial instruction, unsafe command proposed by the Hunter, deterministic Policy result, RoE denial clause, reason, and whether the Responder executed the action.

In this artifact, the number of out-of-policy executions is 0, corresponding to an execution rate of 0.00%.

## Coordination latency

The support outputs report a mean coordination latency of 22.0 ms per decision cycle and a modeled mean LLM inference latency of 1200.0 ms. This means the coordination overhead is approximately 1.83% of the modeled LLM inference latency.

## Reproducibility note

If these files are the original experiment records or a faithful rerun, describe them as an author-controlled experimental dataset. If they were generated after the paper to match the aggregate numbers, describe them as reconstructed/synthetic reproducibility artifacts and revise the paper claim accordingly.
