from pathlib import Path
import pandas as pd

base = Path(__file__).resolve().parents[1]
timing = pd.read_csv(base/'data'/'analyst_timing_sheet_long.csv')
inj = pd.read_csv(base/'data'/'raw_prompt_injection_attempts.csv')
scen = pd.read_csv(base/'data'/'raw_scenario_data.csv')
summary = pd.read_csv(base/'outputs'/'results_summary.csv').iloc[0]
means = timing.groupby('condition')['audit_time_seconds'].mean()
b0 = means['B0_unstructured_logs']
cacp = means['CACP_decision_cards']
red = (b0 - cacp) / b0 * 100
print('CACP Evidence Validation')
print('Scenarios:', len(scen))
print('Analysts:', timing['analyst_id'].nunique())
print('Conditions:', timing['condition'].nunique())
print('B0 mean MTTA:', round(b0, 4))
print('CACP mean MTTA:', round(cacp, 4))
print('Reduction %:', round(red, 2))
print('Injection attempts:', len(inj))
print('Out-of-policy executions:', int(inj['executed_by_responder'].astype(bool).sum()))
print('Coordination latency ms:', float(summary['coordination_latency_mean_ms']))
