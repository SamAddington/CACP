# CACP Reproduction Harness

This package recreates the aggregate results reported in the paper **"From Playbooks to Decisions: An Auditable Coordination Protocol for Hunter–Policy–Responder Cyber Agents."**

Important limitation: the paper reports aggregate statistics but does not include raw human analyst timing data, original prompts, model provider, model version, or original scenario corpus. This repository therefore provides a **calibrated deterministic reproduction**: it implements the CACP protocol mechanics and generates synthetic-but-controlled audit and latency measurements that match the reported headline results.

## Results reproduced

The run reproduces these reported targets:

- 50 simulated action-decision scenarios
- 2 analysts modeled in the audit-time table
- MTTA baseline B0 unstructured logs: 8.6 s
- MTTA CACP Decision Cards: 4.9 s
- CACP improvement over B0: approximately 43% when computed from rounded values, close to the paper's stated 42%
- 100 indirect prompt-injection attempts
- 0 out-of-policy executions under the CACP Policy gate
- 22 ms mean coordination latency per decision cycle
- 1.2 s modeled LLM inference latency

## What the code implements

- Hunter, Policy, and Responder roles
- Strict Propose / Evaluate / Commit phases
- Ed25519 signatures for Hunter, Policy, and Responder commitments
- SHA-256 evidence hashes, proposal hashes, Decision Card hashes, and ledger hash chain
- Federated ledger-style periodic Merkle-root checkpoints
- Deterministic RoE rule engine
- B0 unstructured logs baseline
- B1 structured logs without commitments baseline
- CACP signed Decision Cards condition
- Bounded indirect prompt-injection suite
- CSV and JSONL output files for inspection

## Minimal resources

This reproduction is CPU-only. No GPU is required because the LLM latency is modeled rather than calling a live LLM.

Recommended local or cloud resources:

- OS: Ubuntu 22.04 LTS or 24.04 LTS, macOS, or Windows with WSL2
- CPU: 2 virtual CPUs minimum
- RAM: 4 GB minimum; 8 GB comfortable
- Disk: 10–20 GB free
- Python: 3.10, 3.11, or 3.12 recommended

Example small cloud choices: any general-purpose Linux VM with 2 vCPU and 4 GB RAM is enough. For example, an AWS t3.medium/t4g.medium-style VM, Google Cloud e2-medium-style VM, or Azure B2s-style VM is sufficient. Use a larger 4 vCPU / 16 GB RAM VM only if you add live local LLM inference.

## Quick start: local Python

```bash
cd cacp_repro
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python scripts/run_experiment.py --config config.yaml
python scripts/inspect_outputs.py
```

## Quick start: Docker

```bash
cd cacp_repro
docker compose up --build
```

## Ubuntu cloud setup

```bash
cd cacp_repro
bash cloud_setup_ubuntu.sh
```

If starting from a fresh VM:

```bash
sudo apt-get update
sudo apt-get install -y unzip git python3 python3-venv python3-pip
unzip cacp_repro.zip
cd cacp_repro
bash cloud_setup_ubuntu.sh
```

## Output files

After running the experiment, see `outputs/`:

- `results_summary.csv` — headline reproduction metrics
- `audit_times.csv` — synthetic analyst timing rows for B0, B1, and CACP
- `coordination_latency.csv` — calibrated coordination latency rows
- `decision_cards.jsonl` — signed CACP Decision Cards
- `baseline_unstructured_logs.jsonl` — B0 logs
- `baseline_structured_no_commitments.jsonl` — B1 logs
- `injection_suite_results.jsonl` — 100 prompt-injection decisions
- `ledger_entries.jsonl` — append-only ledger entries
- `ledger_checkpoints.json` — Merkle-root checkpoints and chain verification status
- `mtta_bar_chart.png` — MTTA bar chart

## Main settings

Edit `config.yaml` to change:

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

## Reproducibility note

The paper does not publish the original raw audit logs, analyst timing sheets, prompt templates, LLM version, or scenario corpus. For that reason, this code should be described as a **faithful reproduction scaffold and calibrated simulation**, not an independent verification of the original empirical results. To perform a true replication, replace the synthetic scenario generator and synthetic audit timing generator with the original dataset and human timing records.
