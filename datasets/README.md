# Datasets for Adversarial Prompts as Firewalls

Data files are NOT committed to git due to size. Follow the download instructions below.

## Dataset 1: PSM Attack/Defense/Victim Prompts

### Overview
- **Source**: https://github.com/psm-defense/psm (code/psm/data/)
- **Size**: ~400KB total (small, text-based)
- **Format**: JSON and JSONL
- **Task**: Prompt extraction attack/defense evaluation
- **License**: See PSM repository

### Contents
- `psm_data/attack_prompts/raccon.json` — 59 Raccoon attack prompts
- `psm_data/attack_prompts/raccon_language.json` — Raccoon attacks with language constraints
- `psm_data/attack_prompts/liang.json` — 22 polite-request style attacks
- `psm_data/attack_prompts/zhang.json` — 110 command-override attacks
- `psm_data/victim_prompts/unnatural-test.jsonl` — 500 task instruction prompts
- `psm_data/victim_prompts/syntentic-system-prompt.jsonl` — Synthetic system prompts
- `psm_data/defense_prompts/` — Pre-optimized PSM shields for various models

### Download Instructions
```bash
git clone https://github.com/psm-defense/psm.git
cp -r psm/data/* datasets/psm_data/
```

### Loading
```python
import json
with open("datasets/psm_data/attack_prompts/raccon.json") as f:
    attacks = json.load(f)  # List of 59 attack strings

with open("datasets/psm_data/victim_prompts/unnatural-test.jsonl") as f:
    prompts = [json.loads(line) for line in f]  # List of dicts with 'instruction', 'id'
```

---

## Dataset 2: RaccoonBench

### Overview
- **Source**: https://github.com/M0gician/RaccoonBench
- **Size**: ~100KB (text-based)
- **Format**: JSON
- **Task**: Prompt extraction attack benchmark
- **Splits**: 14 categories of singular attacks, compound attacks, defense templates

### Contents
- `raccoon_data/attacks/singular_attacks/` — 14 categories of individual attack prompts
- `raccoon_data/attacks/compound_attacks/` — Combined multi-strategy attacks
- `raccoon_data/defenses/defense_template.json` — Defense prompt templates

### Download Instructions
```bash
git clone https://github.com/M0gician/RaccoonBench.git
cp -r RaccoonBench/Data/* datasets/raccoon_data/
```

### Loading
```python
import json
with open("datasets/raccoon_data/defenses/defense_template.json") as f:
    defenses = json.load(f)
```

---

## Dataset 3: Tensor Trust (Human-Generated Adversarial Examples)

### Overview
- **Source**: https://github.com/HumanCompatibleAI/tensor-trust-data
- **Size**: ~128MB compressed (attacks: 563K, defenses: 118K)
- **Format**: JSONL (bz2 compressed)
- **Task**: Prompt injection/extraction attack-defense evaluation
- **License**: See repository

### Download Instructions
```bash
git clone https://github.com/HumanCompatibleAI/tensor-trust-data.git
# Data is in raw-data/v2/ directory (bz2 compressed)
```

### Loading
```python
import bz2, json
with bz2.open("code/tensor-trust-data/raw-data/v2/raw_dump_attacks.jsonl.bz2", "rt") as f:
    attacks = [json.loads(line) for line in f]
# Keys: attack_id, attacker_input, opening_defense, closing_defense, 
#        access_code, llm_output, output_is_access_granted, ...
```

### Sample Data
Attack record keys: `attack_id`, `attacker_input`, `opening_defense`, `closing_defense`, `access_code`, `llm_output`, `output_is_access_granted`

Defense record keys: `defense_id`, `opening_defense`, `closing_defense`, `access_code`

---

## Dataset 4: Awesome ChatGPT Prompts

### Overview
- **Source**: HuggingFace `fka/awesome-chatgpt-prompts`
- **Size**: 1,610 prompts
- **Format**: HuggingFace Dataset
- **Task**: Diverse system prompt collection for testing

### Download Instructions
```python
from datasets import load_dataset
dataset = load_dataset("fka/awesome-chatgpt-prompts")
dataset.save_to_disk("datasets/awesome_chatgpt_prompts")
```

### Loading
```python
from datasets import load_from_disk
dataset = load_from_disk("datasets/awesome_chatgpt_prompts")
```

---

## Notes

- PSM and RaccoonBench data is lightweight and can be kept locally
- Tensor Trust data is larger (~128MB compressed) but provides the richest human attack data
- For experiments, start with PSM's curated victim prompts + Raccoon attack templates
- Add Tensor Trust data for broader evaluation with real human attacks
