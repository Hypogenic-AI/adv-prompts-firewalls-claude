# Cloned Repositories

## Repo 1: PSM (Prompt Sensitivity Minimization)
- **URL**: https://github.com/psm-defense/psm
- **Location**: `code/psm/`
- **Purpose**: Shield optimization framework for defending system prompts against extraction
- **Key files**:
  - `run.py` — Main entry point for running PSM optimization
  - `src/` — Core source code (optimizer, evaluator, fitness function)
  - `config/` — Configuration files for different models and datasets
  - `data/attack_prompts/` — Curated attack suites (Raccoon, Zhang, Liang)
  - `data/victim_prompts/` — System prompt corpora for evaluation
  - `data/defense_prompts/` — Pre-optimized shield results
- **Dependencies**: See `requirements.txt`
- **Notes**: Black-box approach, requires OpenAI API access. Contains pre-computed shields for GPT-4o-mini, GPT-4.1-mini, GPT-5-mini.

## Repo 2: PromptExtractionEval
- **URL**: https://github.com/liangzid/PromptExtractionEval
- **Location**: `code/PromptExtractionEval/`
- **Purpose**: Evaluation toolkit for prompt extraction attacks and defenses
- **Key files**:
  - `extractingPrompt/` — Prompt extraction attack implementations
  - `data/` — Dataset files
  - `GPTs/` — GPT-related evaluation tools
- **Notes**: From "Why Are My Prompts Leaked?" paper. Includes attack and defense evaluation scripts.

## Repo 3: RaccoonBench
- **URL**: https://github.com/M0gician/RaccoonBench
- **Location**: `code/RaccoonBench/`
- **Purpose**: Comprehensive prompt extraction attack benchmark
- **Key files**:
  - `Data/attacks/` — 14 categories of singular attacks + compound attacks
  - `Data/defenses/defense_template.json` — Defense prompt templates
  - `Raccoon/` — Benchmark evaluation code
  - `run_raccoon_gang.py` — Main benchmark runner
- **Dependencies**: See `requirements.txt`
- **Notes**: Provides the most comprehensive attack taxonomy for prompt extraction evaluation.

## Repo 4: Tensor Trust Data
- **URL**: https://github.com/HumanCompatibleAI/tensor-trust-data
- **Location**: `code/tensor-trust-data/`
- **Purpose**: Largest human-generated adversarial dataset (563K attacks, 118K defenses)
- **Key files**:
  - `raw-data/v2/raw_dump_attacks.jsonl.bz2` — All attack records
  - `raw-data/v2/raw_dump_defenses.jsonl.bz2` — All defense records
  - `Using the Tensor Trust dataset.ipynb` — Tutorial notebook
  - `benchmarks/` — Benchmark evaluation code
- **Notes**: Data is bz2-compressed. Read with Python `bz2` module. From ICLR 2024 paper.

## Repo 5: DAT (Defense by Attack Techniques)
- **URL**: https://github.com/LukeChen-go/pia-defense-by-attack
- **Location**: `code/pia-defense-by-attack/`
- **Purpose**: Training-free prompt injection defense using inverted attack patterns
- **Key files**: Shield prompt templates, evaluation scripts for direct/indirect injection
- **Notes**: Implements Ignore, Escape, Fake Completion, and Fakecom-t defenses. Most directly relevant to our "adversarial prompts as firewalls" hypothesis — uses attack vectors as defense.
