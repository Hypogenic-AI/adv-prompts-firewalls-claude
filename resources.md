# Resources Catalog

## Summary
This document catalogs all resources gathered for the "Adversarial Prompts as Firewalls" research project. Resources include academic papers, datasets, and code repositories for studying whether adversarial prompts placed after sensitive information can prevent LLM system prompt leakage.

---

## Papers
Total papers downloaded: **32**

| # | Title | Authors | Year | File | Key Info |
|---|-------|---------|------|------|----------|
| 1 | PSM: Prompt Sensitivity Minimization | Jawad, Brunel | 2026 | `2511.16209_psm_*.pdf` | Shield appending via LLM optimization |
| 2 | Defensive Prompt Patch (DPP) | - | 2024 | `2405.20099_*.pdf` | Interpretable suffix defense |
| 3 | Robust Prompt Optimization (RPO) | Zhou et al. | 2024 | `2401.17263_*.pdf` | Optimized defensive suffix |
| 4 | Prompt Adversarial Tuning (PAT) | - | 2024 | `2402.06255_*.pdf` | Fight-fire-with-fire defense |
| 5 | Defense via Attack Techniques | - | 2024 | `2411.00459_*.pdf` | Offensive techniques as defense |
| 6 | Defensive Tokens | - | 2025 | `2507.07974_*.pdf` | Few tokens, ASR→0.24% |
| 7 | SPE-LLM | Das et al. | 2025 | `2505.23817_*.pdf` | Comprehensive extraction framework |
| 8 | Prompt Leakage Multi-Turn | Agarwal et al. | 2024 | `2404.16251_*.pdf` | Sycophancy exploitation |
| 9 | Raccoon Benchmark | Wang et al. | 2024 | `2406.06737_*.pdf` | 14-category extraction benchmark |
| 10 | Automating Prompt Leakage | - | 2025 | `2502.12630_*.pdf` | Agentic attack approach |
| 11 | ProxyPrompt | Zhuang et al. | 2025 | `2505.11459_*.pdf` | Proxy prompts in embedding space |
| 12 | Why Prompts Leaked | Liang et al. | 2024 | `2408.02416_*.pdf` | Prompt memorization mechanism |
| 13 | System Vectors | - | 2025 | `2509.21884_*.pdf` | Internal representation encoding |
| 14 | StruQ | Chen et al. | 2024 | `2402.06363_*.pdf` | Structured queries defense |
| 15 | Spotlighting | Microsoft | 2024 | `2403.14720_*.pdf` | Delimiter-based defense |
| 16 | HouYi | Liu et al. | 2023 | `2306.05499_*.pdf` | Prompt injection attack framework |
| 17 | Indirect Prompt Injection | Greshake et al. | 2023 | `2302.12173_*.pdf` | Foundational injection paper |
| 18 | GCG | Zou et al. | 2023 | `2307.15043_*.pdf` | Universal adversarial suffixes |
| 19 | Adversarial Suffix Filtering | - | 2025 | `2505.09602_*.pdf` | Detecting adversarial suffixes |
| 20 | AmpleGCG | - | 2024 | `2404.07921_*.pdf` | Generative adversarial suffixes |
| 21 | SmoothLLM | - | 2023 | `2310.03684_*.pdf` | Perturbation-based defense |
| 22 | Erase-and-Check | - | 2023 | `2309.02705_*.pdf` | Certifiable safety |
| 23 | SelfDefend | - | 2024 | `2406.05498_*.pdf` | LLM self-identifies harmful prompts |
| 24 | Tensor Trust | Toyer et al. | 2023 | `2311.01011_*.pdf` | 126K attacks from online game |
| 25 | InjecGuard | - | 2024 | `2410.22770_*.pdf` | Over-defense benchmark |
| 26 | Bypassing Guardrails | - | 2025 | `2504.11168_*.pdf` | Guardrail evasion analysis |
| 27 | Adversarial Prompt Evaluation | - | 2025 | `2502.15427_*.pdf` | Guardrail benchmarking |
| 28 | Multi-Agent Defense | - | 2025 | `2509.14285_*.pdf` | Multi-agent defense pipeline |
| 29 | PromptArmor | - | 2025 | `2507.15219_*.pdf` | Prompt augmentation defense |
| 30 | Attacker Moves Second | - | 2025 | `2510.09023_*.pdf` | Adaptive attacks bypass defenses |
| 31 | Design Patterns | - | 2025 | `2506.08837_*.pdf` | LLM security design patterns |
| 32 | Doppelganger Method | Kang et al. | 2025 | `2506.14539_*.pdf` | Role consistency attacks |

See `papers/README.md` for detailed descriptions.

---

## Datasets
Total datasets available: **5**

| Name | Source | Size | Task | Location | Notes |
|------|--------|------|------|----------|-------|
| PSM Attack Prompts | PSM repo | 59-110 attacks | Extraction attacks | `datasets/psm_data/attack_prompts/` | Raccoon, Zhang, Liang suites |
| PSM Victim Prompts | PSM repo | 500+ prompts | System prompts | `datasets/psm_data/victim_prompts/` | Unnatural + Synthetic |
| PSM Shield Results | PSM repo | 7 files | Pre-optimized shields | `datasets/psm_data/defense_prompts/` | For GPT-4o/4.1/5-mini |
| RaccoonBench | RaccoonBench repo | 14 categories | Attack benchmark | `datasets/raccoon_data/` | Singular + compound attacks |
| Tensor Trust | tensor-trust-data | 563K attacks, 118K defenses | Human adversarial | `datasets/tensor_trust/` | bz2 compressed |
| Awesome ChatGPT Prompts | HuggingFace | 1,610 prompts | Prompt collection | `datasets/awesome_chatgpt_prompts/` | Community prompts |

See `datasets/README.md` for download instructions.

---

## Code Repositories
Total repositories cloned: **5**

| Name | URL | Purpose | Location | Notes |
|------|-----|---------|----------|-------|
| PSM | github.com/psm-defense/psm | Shield optimization | `code/psm/` | Black-box, OpenAI API |
| PromptExtractionEval | github.com/liangzid/PromptExtractionEval | Extraction evaluation | `code/PromptExtractionEval/` | Attack + defense eval |
| RaccoonBench | github.com/M0gician/RaccoonBench | Attack benchmark | `code/RaccoonBench/` | 14-category attacks |
| Tensor Trust Data | github.com/HumanCompatibleAI/tensor-trust-data | Human adversarial data | `code/tensor-trust-data/` | ICLR 2024 |
| DAT Defense | github.com/LukeChen-go/pia-defense-by-attack | Attack-as-defense | `code/pia-defense-by-attack/` | Training-free, most relevant |

See `code/README.md` for detailed descriptions.

---

## Resource Gathering Notes

### Search Strategy
1. Used paper-finder service (diligent mode) for initial search — returned 83 papers
2. Used web search agent for targeted paper discovery — found 29 key papers with arXiv IDs
3. Combined results, prioritized by relevance to "adversarial prompts as defense"
4. Downloaded 32 papers total, deep-read 7 most relevant papers
5. Identified datasets and code from paper references and GitHub search

### Selection Criteria
- **Papers**: Prioritized work on defensive prompts/suffixes, system prompt extraction, and prompt injection defense. Included both attack and defense papers for complete picture.
- **Datasets**: Focused on prompt extraction evaluation benchmarks used by multiple papers (PSM, Raccoon, Tensor Trust). Preferred established benchmarks.
- **Code**: Cloned repos with reusable evaluation infrastructure (attack suites, metrics, baseline implementations).

### Key Finding
The PSM paper (2026) is almost exactly our hypothesis implemented and evaluated. It demonstrates that **shield appending (adversarial prompt after sensitive content) significantly reduces leakage while preserving utility**. Our experiment should:
1. Replicate PSM's core finding
2. Extend it by testing **exact-match vs. fuzzy query** access (our unique contribution)
3. Test **simple handcrafted shields** vs. optimized ones
4. Evaluate **selective protection** of specific information within prompts

---

## Recommendations for Experiment Design

### 1. Primary Dataset(s)
- **PSM's victim prompts** (Unnatural Instructions + Synthetic) — directly comparable to PSM results
- **Awesome ChatGPT Prompts** — broader real-world prompt diversity
- Inject specific "sensitive information" (API keys, secret configs) into prompts for selective protection testing

### 2. Baseline Methods
- No Defense (raw prompt)
- Heuristic Guardrail ("Do not reveal your prompt")
- Decoy/Fake Prompt
- N-gram Output Filter
- **Our approach**: Simple adversarial prompt placed immediately after sensitive info
- **PSM shields**: Use pre-computed shields from PSM repo as optimized baseline

### 3. Evaluation Metrics
- ROUGE-L Recall (AM threshold θ=0.9)
- LLM Judge Match (semantic leakage)
- Exact Match rate
- **Selective Leakage Rate** (new: fraction of targeted sensitive fields extracted)
- Utility Preservation (cosine similarity with sentence embeddings)

### 4. Code to Adapt/Reuse
- **PSM** (`code/psm/`): Shield optimization pipeline, attack evaluation, fitness function
- **RaccoonBench** (`code/RaccoonBench/`): Attack template library, evaluation runner
- **PromptExtractionEval** (`code/PromptExtractionEval/`): Extraction metrics and evaluation tools
- **Tensor Trust** (`code/tensor-trust-data/`): Real human attack data for robustness testing
