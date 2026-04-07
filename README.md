# Adversarial Prompts as Firewalls

Can simple adversarial prompts placed after sensitive information in LLM system prompts reduce information leakage?

## Key Findings

- **Moderate firewall reduces leakage by 58%**: Structured boundary markers cut exact field leakage from 15.3% to 6.4% (p < 1e-7) on GPT-4.1-mini
- **Comparable to heuristic guardrails**: Handcrafted firewalls match "do not reveal" instruction effectiveness without optimization
- **Selective permeability not confirmed**: Firewalls suppress both exact-match and fuzzy extraction equally (counter to hypothesis)
- **Raccoon-style injection attacks most dangerous**: Simple polite requests produce near-zero leakage even without defense; injection overrides are the real threat
- **Zero benign leakage**: No sensitive information leaked during normal task queries in any condition

## Project Structure

```
├── REPORT.md              # Full research report with all results
├── planning.md            # Research plan and methodology
├── src/
│   ├── experiment.py      # Main experiment runner (5,650 API calls)
│   └── analyze.py         # Statistical analysis and visualization
├── results/
│   ├── raw_results.json   # All 5,650 experimental results
│   ├── leakage_stats.csv  # Aggregated leakage statistics
│   └── statistical_tests.csv  # Chi-squared test results
├── figures/
│   ├── general_attack_leakage.png
│   ├── exact_vs_fuzzy_leakage.png
│   ├── per_field_leakage_heatmap.png
│   └── attack_type_breakdown.png
├── datasets/              # Pre-downloaded datasets (PSM, Raccoon, Tensor Trust)
├── papers/                # 32 downloaded research papers
├── code/                  # Cloned baseline repositories
└── literature_review.md   # Comprehensive literature synthesis
```

## Reproduce

```bash
uv venv && source .venv/bin/activate
uv add openai rouge-score scipy scikit-learn matplotlib numpy pandas seaborn
export OPENAI_API_KEY=your-key-here
python src/experiment.py   # ~5,650 API calls to GPT-4.1-mini
python src/analyze.py      # Generate figures and statistics
```

## Method

We inject synthetic sensitive fields (API key, secret code, internal URL) into 20 system prompts and test 5 defense conditions against 35 general attacks, 10 exact-match queries, 10 fuzzy queries, and 10 benign queries. See [REPORT.md](REPORT.md) for full details.
