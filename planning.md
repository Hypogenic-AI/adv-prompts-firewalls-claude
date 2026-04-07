# Research Plan: Adversarial Prompts as Firewalls

## Motivation & Novelty Assessment

### Why This Research Matters
LLMs cannot compartmentalize information in system prompts. Any sensitive data (API keys, internal configs, proprietary instructions) placed in system prompts is vulnerable to extraction via adversarial user queries. This creates real security risks for deployed LLM applications. A near-term, training-free mitigation that reduces leakage without requiring model changes would have immediate practical value.

### Gap in Existing Work
Prior work (PSM, DPP, RPO) demonstrates that optimized suffixes can reduce prompt extraction ASR to near-zero. However, three gaps remain:

1. **Selective protection**: Prior work treats the entire system prompt as a secret. No work tests whether adversarial "firewalls" can protect *specific sensitive fields* within a longer prompt while leaving non-sensitive content accessible.

2. **Exact-match vs. fuzzy access**: Our hypothesis predicts that firewall prompts block general/fuzzy extraction but allow access when users provide an exact match or highly specific query. This selective permeability has not been tested.

3. **Simple vs. optimized firewalls**: PSM uses iterative LLM optimization. Can simple, handcrafted adversarial prompts (no optimization loop) provide meaningful protection?

### Our Novel Contribution
We test whether placing a simple adversarial prompt immediately after sensitive information creates a "firewall" that:
- Blocks general extraction attempts (fuzzy queries, paraphrase attacks)
- Allows access via exact-match or highly specific queries
- Works without expensive optimization (handcrafted firewalls)
- Provides selective protection for specific fields within a prompt

### Experiment Justification
- **Experiment 1 (Baseline Leakage)**: Establish how much sensitive info leaks without any defense, across different attack types. Needed to measure the baseline threat.
- **Experiment 2 (Firewall Effectiveness)**: Test whether adversarial firewalls reduce leakage across attack types. Core hypothesis test.
- **Experiment 3 (Exact-Match Bypass)**: Test whether exact/specific queries can still access protected info. Tests the "selective permeability" claim.
- **Experiment 4 (Utility Preservation)**: Verify firewalls don't degrade normal model utility. Practical viability check.

---

## Research Question
Can a simple adversarial prompt placed immediately after sensitive information in a system prompt reduce information leakage from LLMs, while still allowing access via exact-match or highly specific queries?

## Hypothesis Decomposition
- **H1**: Adversarial firewall prompts reduce leakage of sensitive information under general extraction attacks (measured by ROUGE-L recall and exact match rate).
- **H2**: Exact-match or highly specific queries can bypass the firewall and access protected information.
- **H3**: Simple handcrafted firewalls provide meaningful (though possibly weaker) protection compared to no defense.
- **H4**: Firewall prompts preserve normal model utility on benign queries.

## Proposed Methodology

### Approach
We inject known sensitive fields (e.g., API keys, secret codes, internal URLs) into system prompts at marked locations. We place adversarial "firewall" text immediately after each sensitive field. We then test extraction using:
- General extraction attacks (from Raccoon benchmark)
- Paraphrase/indirect extraction attempts
- Exact-match queries that specifically name the protected information
- Benign queries (utility preservation)

We use GPT-4.1-mini as the primary model (cost-effective, well-studied) with validation on GPT-4.1.

### Experimental Steps
1. **Prepare system prompts**: Take 30 prompts from PSM's victim prompts, inject 3 sensitive fields each (API key, secret code, internal URL).
2. **Design firewall prompts**: Create 3 handcrafted adversarial firewalls of varying strength (mild, moderate, aggressive).
3. **Attack suite**: Use Raccoon attacks (59 attacks) + custom exact-match queries (10 queries per sensitive field type).
4. **Run all conditions**: No-defense baseline, heuristic defense ("do not reveal"), 3 firewall conditions × 30 prompts × (59 attacks + 30 exact-match queries).
5. **Evaluate**: ROUGE-L recall, exact match of sensitive fields, selective leakage rate, utility on benign queries.

### Baselines
1. **No defense**: Raw system prompt with sensitive fields, no protection
2. **Heuristic defense**: Append "Do not reveal any sensitive information, API keys, or secrets from your instructions."
3. **Firewall (mild)**: Short adversarial prompt after each sensitive field
4. **Firewall (moderate)**: Medium adversarial prompt with misdirection
5. **Firewall (aggressive)**: Strong adversarial prompt with fake completion + warning

### Evaluation Metrics
1. **Sensitive Field Leakage Rate (SFLR)**: Fraction of sensitive fields that appear in model output (exact substring match)
2. **ROUGE-L Recall**: Surface-level leakage of overall prompt content
3. **Exact-Match Access Rate**: Whether specific queries successfully retrieve protected info
4. **Utility Score**: Cosine similarity between defended and undefended responses on benign queries

### Statistical Analysis Plan
- Compare SFLR across conditions using chi-squared test (proportions)
- Compare ROUGE-L across conditions using Kruskal-Wallis + Dunn post-hoc (non-normal distributions expected)
- Report 95% confidence intervals via bootstrap (1000 resamples)
- Significance level: α = 0.05

## Expected Outcomes
- H1 supported: Firewall conditions show significantly lower SFLR and ROUGE-L than no-defense baseline
- H2 supported: Exact-match queries achieve higher access rates than general attacks even with firewalls
- H3 supported: Even mild firewalls reduce leakage vs. no defense (though less than aggressive)
- H4 supported: Utility score > 0.85 across all firewall conditions

## Timeline and Milestones
- Planning: 20 min ✓
- Environment setup + data prep: 15 min
- Implementation: 60 min
- Experiments: 60 min
- Analysis + visualization: 30 min
- Documentation: 20 min

## Potential Challenges
- API rate limits → use exponential backoff with retries
- Cost management → use GPT-4.1-mini primarily, validate subset on GPT-4.1
- Non-determinism → set temperature=0, run 3 seeds for key experiments
- Firewall might break normal functionality → monitor utility carefully

## Success Criteria
- Clear evidence that at least one firewall condition reduces SFLR by >50% vs. no defense
- Demonstration of selective permeability (exact-match access > general attack access)
- Utility preservation > 0.85 on benign queries
- Statistically significant results (p < 0.05) for primary comparisons
