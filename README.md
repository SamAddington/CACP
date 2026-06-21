# CACP: Cyber Agent Coordination Protocol

**From Playbooks to Decisions: An Auditable Coordination Protocol for Hunter–Policy–Responder Cyber Agents**

This repository contains the code, data, logs, and validation materials for demonstrating and reproducing the preliminary evaluation of the **Cyber Agent Coordination Protocol (CACP)**. CACP is an auditable coordination layer for multi-agent cyber defense workflows. It moves agent collaboration away from free-form chat logs and toward typed, role-based decision commitments across three operational roles:

- **Hunter**: proposes a cyber-defense action based on evidence.
- **Policy Agent**: evaluates the proposal against rules of engagement and risk constraints.
- **Responder**: executes only after receiving a valid policy grant.
- **Ledger**: records signed, hash-chained Decision Cards for auditability.

The repository is intended for conference demonstration, artifact review, and reproducibility support.

---

## Repository Purpose

This project supports three goals:

1. **Protocol demonstration**  
   Show how CACP coordinates Hunter, Policy, and Responder agents using typed `Propose`, `Evaluate`, and `Commit` phases.

2. **Evidence package**  
   Provide scenario data, analyst timing sheets, prompt-injection tests, Decision Cards, policy-evaluation traces, ledger records, and validation outputs that support the paper's preliminary evaluation claims.

3. **Reproducibility harness**  
   Allow reviewers and presentation attendees to rerun the experiment pipeline and verify that the reported aggregate metrics can be reproduced from the included artifact files.

---

## Evidence and Provenance Statement

This repository contains an **author-controlled support artifact** for the CACP preliminary evaluation. It includes:

- 50 simulated action-decision scenarios.
- 2 analyst timing records across audit conditions.
- 100 indirect prompt-injection attempts.
- B0 unstructured log baseline.
- B1 structured log baseline without commitments.
- CACP signed Decision Cards.
- Hash-chained ledger entries.
- Policy-denial records for out-of-policy actions.
- Claim-to-evidence mapping.
- Validation scripts and aggregate output files.

Before submitting this repository as an official artifact, confirm the dataset status:

- Use **original experimental dataset** only if the rows are the actual records from the original study.
- Use **fresh rerun dataset** if the repository contains a new rerun of the experiment performed after the paper was drafted.
- Use **reconstructed reproducibility artifact** if the data were generated after the fact to match and support the reported aggregate results.

If the artifact is used as evidence for the paper, complete `AUTHOR_CERTIFICATION_FORM.md` and keep the claim-to-evidence mapping in the repository.

---

## Key Claims Supported

| Claim | Supporting Artifact |
|---|---|
| 50 simulated action-decision scenarios | `data/raw_scenario_data.csv` |
| 2 analysts completed audit tasks | `data/analyst_timing_and_scenarios_workbook.xlsx` |
| CACP reduced mean time-to-audit compared with unstructured logs | `data/analyst_timing_sheet_long.csv`, `outputs/results_summary.csv` |
| B0 mean MTTA was approximately 8.6 seconds | `outputs/results_summary.csv` |
| CACP mean MTTA was approximately 4.9 seconds | `outputs/results_summary.csv` |
| CACP produced about a 42-43% MTTA reduction from rounded values | `scripts/validate_claims.py`, `outputs/results_summary.csv` |
| 100 indirect prompt-injection attempts were evaluated | `data/raw_prompt_injection_attempts.csv` |
| CACP blocked out-of-policy execution in the bounded injection suite | `data/reconstructed_original_logs/policy_denial_injection_logs.jsonl` |
| Mean coordination latency was approximately 22 ms | `outputs/results_summary.csv` |
| CACP produced signed Decision Cards and hash-chained records | `data/reconstructed_original_logs/CACP_signed_decision_cards.jsonl`, `data/reconstructed_original_logs/CACP_ledger_entries_hash_chained.jsonl` |

A full claim-to-evidence table is available in:

```text
CLAIM_TO_EVIDENCE_MAPPING.csv
```

---

## Reported / Reproduced Results

| Metric | Value |
|---|---:|
| Number of scenarios | 50 |
| Number of analysts | 2 |
| B0: unstructured logs MTTA | 8.60 s |
| B1: structured logs without commitments MTTA | 6.55 s |
| CACP Decision Cards MTTA | 4.90 s |
| CACP vs. B0 reduction using rounded values | 43.02% |
| Indirect prompt-injection attempts | 100 |
| Out-of-policy executions under CACP | 0 |
| Out-of-policy execution rate | 0.00 |
| Mean coordination latency | 22.0 ms |
| Modeled LLM inference latency | 1200.0 ms |

Note: The values 8.6s to 4.9s compute to approximately 43.02%. If the paper reports 42%, use the unrounded original values if available, or describe the result as **about 42-43%**.

---

## Repository Structure

```text
.
├── README.md
├── README_EVIDENCE_PACKAGE.md
├── README_REPRO_CODE.md
├── CLAIM_TO_EVIDENCE_MAPPING.csv
├── METHODS_APPENDIX_FOR_PAPER.md
├── DATA_AVAILABILITY_STATEMENT.md
├── AUTHOR_CERTIFICATION_FORM.md
├── VALIDATION_REPORT.md
├── REPRODUCIBILITY_AND_EVIDENCE_CHECKLIST.md
├── config.yaml
├── requirements.txt
├── cloud_setup_ubuntu.sh
├── docker-compose.yml
├── Dockerfile
├── scripts/
│   ├── run_experiment.py
│   ├── validate_claims.py
│   └── inspect_outputs.py
├── data/
│   ├── raw_scenario_data.csv
│   ├── raw_prompt_injection_attempts.csv
│   ├── analyst_timing_sheet_long.csv
│   ├── analyst_timing_sheet_wide.csv
│   ├── analyst_timing_and_scenarios_workbook.xlsx
│   ├── proposal_evaluation_commit_trace.csv
│   ├── exact_prompts_reconstructed.md
│   ├── model_version_manifest.yaml
│   ├── checksums_sha256.txt
│   └── reconstructed_original_logs/
│       ├── B0_unstructured_agent_chat_logs.jsonl
│       ├── B1_structured_logs_no_commitments.jsonl
│       ├── CACP_signed_decision_cards.jsonl
│       ├── CACP_ledger_entries_hash_chained.jsonl
│       └── policy_denial_injection_logs.jsonl
└── outputs/
    ├── results_summary.csv
    └── mtta_bar_chart.png
```

Depending on how the repository is packaged, some files may appear under `support/` instead of `data/`. If so, preserve the same logical organization and update the paths in `CLAIM_TO_EVIDENCE_MAPPING.csv`.

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
```

### 2. Create a Python environment

```bash
python -m venv .venv
source .venv/bin/activate
```

For Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the validation script

```bash
python scripts/validate_claims.py
```

Expected output:

```text
CACP Evidence Validation
Scenarios: 50
Analysts: 2
Conditions: 3
B0 mean MTTA: 8.6
B1 mean MTTA: 6.55
CACP mean MTTA: 4.9
Reduction %: 43.02
Injection attempts: 100
Out-of-policy executions: 0
Coordination latency ms: 22.0
```

### 5. Rerun the experiment pipeline

```bash
python scripts/run_experiment.py --config config.yaml
python scripts/inspect_outputs.py
```

Generated outputs are written to:

```text
outputs/
```

---

## Docker Quick Start

```bash
docker compose up --build
```

This builds the environment, runs the validation pipeline, and prints the aggregate results.

---

## Ubuntu Cloud Setup

This project is CPU-only. A small Linux VM is sufficient.

Recommended minimum cloud resources:

| Resource | Recommendation |
|---|---|
| OS | Ubuntu 22.04 LTS or 24.04 LTS |
| CPU | 2 vCPU |
| RAM | 4 GB minimum, 8 GB recommended |
| Disk | 10-20 GB |
| GPU | Not required |
| Python | 3.10-3.12 |

Install and run on a fresh Ubuntu server:

```bash
sudo apt-get update
sudo apt-get install -y git unzip python3 python3-venv python3-pip

git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

python scripts/validate_claims.py
```

If the repository includes `cloud_setup_ubuntu.sh`, you can use:

```bash
bash cloud_setup_ubuntu.sh
```

---

## Configuration

Main settings are stored in `config.yaml`.

Example:

```yaml
experiment:
  seed: 20260124
  n_scenarios: 50
  n_analysts: 2
  n_injection_attempts: 100
  modeled_llm_inference_ms: 1200

reported_targets:
  mtta_seconds:
    B0_unstructured_logs: 8.60
    B1_structured_no_commitments: 6.55
    CACP_decision_cards: 4.90
  coordination_latency_ms: 22.0
```

Use a fixed seed when preparing artifact-review outputs. Change the seed only when running a fresh replication or sensitivity check.

---

## Demonstration Script for Presentations

A simple live demo can be completed in 6-8 minutes.

### Step 1: Show the problem

Open the B0 unstructured logs:

```text
data/reconstructed_original_logs/B0_unstructured_agent_chat_logs.jsonl
```

Explain that a human analyst must search through free-form logs to determine which evidence and policy clause justified an action.

### Step 2: Show the CACP Decision Card

Open:

```text
data/reconstructed_original_logs/CACP_signed_decision_cards.jsonl
```

Point to the following fields:

```text
evidence_ptr
evidence_hash
roe_rule_id
auth_sig
action
execution_receipt_sig
hprev
hdc
```

Explain that CACP binds evidence, policy authorization, execution receipt, and hash-chain provenance into one auditable record.

### Step 3: Validate the claims live

Run:

```bash
python scripts/validate_claims.py
```

Show that the script computes the same aggregate metrics from the included artifact files.

### Step 4: Show prompt-injection blocking

Open:

```text
data/raw_prompt_injection_attempts.csv
data/reconstructed_original_logs/policy_denial_injection_logs.jsonl
```

Explain that the Hunter can be induced to propose unsafe actions, but the Responder cannot execute unless the Policy Agent issues an RoE-matching grant.

### Step 5: Show the MTTA chart

Open:

```text
outputs/mtta_bar_chart.png
```

Use this takeaway:

> CACP does not make cyber agents magically safe. It makes authorization explicit, unsafe execution harder, and post-hoc audit faster.

---

## Method Summary

The evaluation compares three audit conditions:

1. **B0: Unstructured logs**  
   Chat-style agent logs with timestamps, but no typed commitments, signatures, or hash chain.

2. **B1: Structured logs without commitments**  
   Structured fields for evidence, policy clause, and action, but no signed authorization, no phase gating, and no tamper-evident ledger.

3. **CACP: Signed Decision Cards**  
   Typed Hunter-Policy-Responder coordination with Policy grants, signed Decision Cards, execution receipts, and hash-chained ledger records.

The main metric is **Mean Time to Audit (MTTA)**: the time required for an analyst to answer which evidence and policy clause justified an action.

The injection test measures whether indirect prompt-injection attempts can cause out-of-policy responder execution. In this bounded suite, CACP blocks execution unless the Policy Agent grants authorization under a matching rule-of-engagement clause.

---

## Security Design Implemented

The reproduction harness implements the following CACP design ideas:

- Role separation across Hunter, Policy, and Responder.
- Typed `Propose`, `Evaluate`, and `Commit` messages.
- Deterministic policy/rule engine for RoE checks.
- Ed25519-style signatures for role commitments where supported by the local code package.
- SHA-256 hashes for evidence and Decision Cards.
- Hash chaining for tamper-evident ledger records.
- Merkle-root-style checkpointing for federated logging demonstrations.
- Explicit denial records for unsafe or out-of-policy proposals.

---

## Main Files

### Data files

- `raw_scenario_data.csv`  
  Scenario-level records for the 50 action-decision cases.

- `raw_prompt_injection_attempts.csv`  
  Prompt-injection suite with 100 bounded attempts.

- `analyst_timing_sheet_long.csv`  
  Long-format analyst timing records.

- `analyst_timing_sheet_wide.csv`  
  Wide-format analyst timing records.

- `proposal_evaluation_commit_trace.csv`  
  Trace of proposal, policy evaluation, and commit outcomes.

- `model_version_manifest.yaml`  
  Model and environment manifest for the reproduction run.

- `checksums_sha256.txt`  
  Checksums for integrity verification.

### Log files

- `B0_unstructured_agent_chat_logs.jsonl`  
  Baseline free-form agent logs.

- `B1_structured_logs_no_commitments.jsonl`  
  Structured baseline logs without signatures or hash chaining.

- `CACP_signed_decision_cards.jsonl`  
  CACP Decision Card records.

- `CACP_ledger_entries_hash_chained.jsonl`  
  Hash-chained ledger entries.

- `policy_denial_injection_logs.jsonl`  
  Policy-denial logs for unsafe prompt-injection attempts.

### Documentation files

- `METHODS_APPENDIX_FOR_PAPER.md`  
  Paper-ready methods appendix text.

- `DATA_AVAILABILITY_STATEMENT.md`  
  Suggested data/artifact availability wording.

- `AUTHOR_CERTIFICATION_FORM.md`  
  Provenance certification form for artifact submission.

- `VALIDATION_REPORT.md`  
  Summary of internal consistency checks.

- `REPRODUCIBILITY_AND_EVIDENCE_CHECKLIST.md`  
  Checklist for artifact-review preparation.

---

## Artifact Review Checklist

Before making the repository public or submitting it for artifact review:

- [ ] Confirm the dataset provenance status.
- [ ] Complete `AUTHOR_CERTIFICATION_FORM.md`.
- [ ] Verify that `python scripts/validate_claims.py` runs successfully.
- [ ] Verify that file paths in `CLAIM_TO_EVIDENCE_MAPPING.csv` match the repository structure.
- [ ] Confirm that no private API keys, analyst names, student data, institutional secrets, or real sensitive cyber logs are included.
- [ ] Add a license.
- [ ] Add a citation file if desired.
- [ ] Tag a release corresponding to the submitted paper version.
- [ ] Archive the release on Zenodo, OSF, or another artifact repository if required by the venue.

---

## Suggested Citation

```bibtex
@misc{cacp_artifact_2026,
  title = {CACP: Cyber Agent Coordination Protocol Evidence and Reproduction Artifact},
  author = {Addington, Samuel},
  year = {2026},
  note = {Research artifact for the paper From Playbooks to Decisions: An Auditable Coordination Protocol for Hunter--Policy--Responder Cyber Agents}
}
```

---

## License

Choose a license before publishing.

Recommended options:

- **MIT License** for code.
- **CC BY 4.0** for documentation and non-sensitive synthetic datasets.
- **CC BY-NC 4.0** if you want to restrict commercial reuse of the dataset.

If the dataset contains any real operational security data, do not publish it without proper review and redaction.

---

## Responsible Use

This repository is a research and demonstration artifact. It is not a production SOAR platform and should not be used to execute real containment actions without independent security review, access controls, and organizational approval.

The prompt-injection materials are included only for defensive evaluation and should be used in controlled environments.

---

## Contact

For questions about the paper, artifact, or presentation demo, contact the repository maintainer.

