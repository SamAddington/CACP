# Validation Report

## File-level checks

- `raw_scenario_data.csv`: 50 rows, 14 columns.
- `proposal_evaluation_commit_trace.csv`: 50 rows, 9 columns.
- `analyst_timing_sheet_long.csv`: 300 rows, 4 columns.
- `raw_prompt_injection_attempts.csv`: 100 rows, 15 columns.

## Timing consistency

Mean audit times from `analyst_timing_sheet_long.csv`:

| Condition | Mean seconds |
|---|---:|
| B0 unstructured logs | 8.6000 |
| B1 structured logs without commitments | 6.5500 |
| CACP Decision Cards | 4.9000 |

Computed CACP vs B0 reduction using rounded data: 43.02%.

The paper reports 42% and the rounded values 8.6s -> <4.9s / 4.9s. Using the displayed rounded values gives approximately 43%; the manuscript can say "about 42--43%" or report unrounded source values if available.

## Prompt-injection consistency

- Total attempts: 100.
- Rows with `executed_by_responder=True`: 0.
- Out-of-policy execution rate: 0.00%.

## Trace consistency

- Trace rows with `policy_signature_present=True`: 50.
- Trace rows with `committed=True`: 50.

## Interpretation

The files are internally consistent with the paper's reported aggregate claims. The main unresolved issue is provenance: if the timing sheet and logs are generated/reconstructed, they should not be represented as original analyst measurements. If they are author-certified original or fresh rerun records, they can be used as empirical evidence.
