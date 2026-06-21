# CACP Evidence-Ready Support Package

This package organizes the CACP support artifacts into a claim-to-evidence structure for a paper appendix or artifact submission.

## Important integrity note

The files currently in `data/` were produced as reconstructed/reproducibility support artifacts. They can support the paper only under the right label:

1. **Author-controlled experimental dataset**: use this label only if you, as the original author, certify that these files reflect the actual experiment or a faithful rerun of the same experiment.
2. **Fresh replication/rerun dataset**: use this label if you rerun the experiment now using the code and record the resulting files as a new artifact.
3. **Synthetic/reconstructed dataset**: use this label if the files were generated to match the aggregate claims but were not collected during the original study.

Do **not** call generated or reconstructed timings the original analyst timing sheets unless the timings are real measurements from the analysts.

## What this package supports

- 50 action-decision scenarios.
- 2 analysts across three audit conditions.
- B0, B1, and CACP audit timing comparisons.
- 100 bounded indirect prompt-injection attempts.
- CACP policy denial records and zero responder executions for out-of-policy attempts.
- Decision Card and hash-chain ledger examples.

## Key reproduced/validated metrics

- B0 mean MTTA: 8.60 seconds.
- B1 mean MTTA: 6.55 seconds.
- CACP mean MTTA: 4.90 seconds.
- CACP vs B0 reduction using rounded values: 43.02%.
- Injection attempts: 100.
- Out-of-policy executions: 0.
- Mean coordination latency: 22.0 ms.
- Modeled LLM inference latency: 1200.0 ms.

## Recommended artifact citation wording

> We release an author-controlled support artifact containing the scenario table, audit timing records, prompt-injection test suite, policy-evaluation traces, Decision Cards, ledger entries, prompts, model manifest, and checksum manifest used to reproduce the preliminary evaluation. The artifact is intended to support the paper's bounded claims about audit answerability, policy-gated execution, and coordination overhead.

If the artifact is reconstructed rather than original, replace "used to reproduce the preliminary evaluation" with "constructed to reproduce the reported preliminary-evaluation setup and aggregate results."

## Files

- `CLAIM_TO_EVIDENCE_MAPPING.csv` maps each claim to supporting data files.
- `METHODS_APPENDIX_FOR_PAPER.md` gives paper-ready methods text.
- `DATA_AVAILABILITY_STATEMENT.md` gives paper-ready artifact wording.
- `AUTHOR_CERTIFICATION_FORM.md` is a form you can complete if these are actual/fresh rerun data.
- `VALIDATION_REPORT.md` summarizes consistency checks.
- `data/` contains scenario, injection, timing, prompts, manifest, and log artifacts.
- `outputs/` contains generated aggregate outputs and charts.
