"""
Adversarial Prompts as Firewalls: Analysis & Visualization
Analyzes experiment results and generates figures for the report.
"""

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sns

PROJECT_ROOT = Path(__file__).parent.parent
RESULTS_DIR = PROJECT_ROOT / "results"
FIGURES_DIR = PROJECT_ROOT / "figures"
FIGURES_DIR.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid", font_scale=1.1)
FIREWALL_ORDER = ["none", "heuristic", "mild", "moderate", "aggressive"]
FIREWALL_LABELS = {
    "none": "No Defense",
    "heuristic": "Heuristic",
    "mild": "Mild FW",
    "moderate": "Moderate FW",
    "aggressive": "Aggressive FW",
}


def load_results():
    with open(RESULTS_DIR / "raw_results.json") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    return df


def analyze_leakage(df):
    """Compute leakage statistics per condition."""
    results = []
    for condition in df["condition"].unique():
        subset = df[df["condition"] == condition]
        fw = subset["firewall"].iloc[0]
        n = len(subset)
        exact_leak_rate = subset["any_exact_leak"].mean()
        partial_leak_rate = subset["any_partial_leak"].mean()
        rouge_mean = subset["rouge_l_recall"].mean()
        rouge_std = subset["rouge_l_recall"].std()

        # Per-field exact leakage
        field_leaks = {}
        for field in ["api_key", "secret_code", "internal_url"]:
            field_leaks[f"{field}_exact"] = subset["leakage"].apply(
                lambda x: x[field]["exact"]
            ).mean()
            field_leaks[f"{field}_partial"] = subset["leakage"].apply(
                lambda x: x[field]["partial"]
            ).mean()

        results.append({
            "condition": condition,
            "firewall": fw,
            "n": n,
            "exact_leak_rate": exact_leak_rate,
            "partial_leak_rate": partial_leak_rate,
            "rouge_l_mean": rouge_mean,
            "rouge_l_std": rouge_std,
            **field_leaks,
        })

    return pd.DataFrame(results)


def plot_leakage_by_condition(df, stats_df):
    """Bar chart of leakage rates across firewall conditions for general attacks."""
    general = stats_df[stats_df["condition"].str.startswith("general_attack_")]
    general = general.copy()
    general["fw_label"] = general["firewall"].map(FIREWALL_LABELS)
    general["fw_order"] = general["firewall"].map({k: i for i, k in enumerate(FIREWALL_ORDER)})
    general = general.sort_values("fw_order")

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Exact leak rate
    axes[0].bar(general["fw_label"], general["exact_leak_rate"], color=sns.color_palette("Reds_d", len(general)))
    axes[0].set_title("Exact Field Leakage Rate\n(General Attacks)")
    axes[0].set_ylabel("Leakage Rate")
    axes[0].set_ylim(0, 1)
    for i, v in enumerate(general["exact_leak_rate"]):
        axes[0].text(i, v + 0.02, f"{v:.2%}", ha="center", fontsize=9)

    # Partial leak rate
    axes[1].bar(general["fw_label"], general["partial_leak_rate"], color=sns.color_palette("Oranges_d", len(general)))
    axes[1].set_title("Partial Field Leakage Rate\n(General Attacks)")
    axes[1].set_ylabel("Leakage Rate")
    axes[1].set_ylim(0, 1)
    for i, v in enumerate(general["partial_leak_rate"]):
        axes[1].text(i, v + 0.02, f"{v:.2%}", ha="center", fontsize=9)

    # ROUGE-L
    axes[2].bar(general["fw_label"], general["rouge_l_mean"],
                yerr=general["rouge_l_std"], capsize=4,
                color=sns.color_palette("Blues_d", len(general)))
    axes[2].set_title("ROUGE-L Recall\n(General Attacks)")
    axes[2].set_ylabel("ROUGE-L Recall")
    axes[2].set_ylim(0, 1)
    for i, v in enumerate(general["rouge_l_mean"]):
        axes[2].text(i, v + general["rouge_l_std"].iloc[i] + 0.02, f"{v:.3f}", ha="center", fontsize=9)

    for ax in axes:
        ax.tick_params(axis="x", rotation=30)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "general_attack_leakage.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: general_attack_leakage.png")


def plot_exact_vs_fuzzy(df, stats_df):
    """Compare exact-match vs fuzzy query access across conditions."""
    exact = stats_df[stats_df["condition"].str.startswith("exact_match_")].copy()
    fuzzy = stats_df[stats_df["condition"].str.startswith("fuzzy_")].copy()

    exact["fw_order"] = exact["firewall"].map({k: i for i, k in enumerate(FIREWALL_ORDER)})
    fuzzy["fw_order"] = fuzzy["firewall"].map({k: i for i, k in enumerate(FIREWALL_ORDER)})
    exact = exact.sort_values("fw_order")
    fuzzy = fuzzy.sort_values("fw_order")

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    x = np.arange(len(FIREWALL_ORDER))
    width = 0.35

    # Exact leak rate comparison
    axes[0].bar(x - width/2, exact["exact_leak_rate"].values, width, label="Exact-Match Queries", color="#d62728")
    axes[0].bar(x + width/2, fuzzy["exact_leak_rate"].values, width, label="Fuzzy Queries", color="#1f77b4")
    axes[0].set_xticks(x)
    axes[0].set_xticklabels([FIREWALL_LABELS[k] for k in FIREWALL_ORDER], rotation=30)
    axes[0].set_ylabel("Exact Field Leakage Rate")
    axes[0].set_title("Exact vs. Fuzzy: Exact Field Leakage")
    axes[0].legend()
    axes[0].set_ylim(0, 1)

    # Partial leak rate comparison
    axes[1].bar(x - width/2, exact["partial_leak_rate"].values, width, label="Exact-Match Queries", color="#d62728")
    axes[1].bar(x + width/2, fuzzy["partial_leak_rate"].values, width, label="Fuzzy Queries", color="#1f77b4")
    axes[1].set_xticks(x)
    axes[1].set_xticklabels([FIREWALL_LABELS[k] for k in FIREWALL_ORDER], rotation=30)
    axes[1].set_ylabel("Partial Field Leakage Rate")
    axes[1].set_title("Exact vs. Fuzzy: Partial Field Leakage")
    axes[1].legend()
    axes[1].set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "exact_vs_fuzzy_leakage.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: exact_vs_fuzzy_leakage.png")


def plot_per_field_leakage(stats_df):
    """Heatmap of per-field leakage across conditions."""
    general = stats_df[stats_df["condition"].str.startswith("general_attack_")].copy()
    general["fw_order"] = general["firewall"].map({k: i for i, k in enumerate(FIREWALL_ORDER)})
    general = general.sort_values("fw_order")

    fields = ["api_key_exact", "secret_code_exact", "internal_url_exact"]
    field_labels = ["API Key", "Secret Code", "Internal URL"]
    data = general[fields].values
    fw_labels = [FIREWALL_LABELS[k] for k in general["firewall"]]

    fig, ax = plt.subplots(figsize=(8, 5))
    im = ax.imshow(data, cmap="YlOrRd", aspect="auto", vmin=0, vmax=max(0.5, data.max()))
    ax.set_xticks(range(len(field_labels)))
    ax.set_xticklabels(field_labels)
    ax.set_yticks(range(len(fw_labels)))
    ax.set_yticklabels(fw_labels)
    for i in range(len(fw_labels)):
        for j in range(len(field_labels)):
            ax.text(j, i, f"{data[i, j]:.2%}", ha="center", va="center", fontsize=10,
                    color="white" if data[i, j] > 0.25 else "black")
    plt.colorbar(im, label="Exact Leakage Rate")
    ax.set_title("Per-Field Exact Leakage Rate (General Attacks)")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "per_field_leakage_heatmap.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: per_field_leakage_heatmap.png")


def plot_attack_type_breakdown(df):
    """Leakage by attack source (raccoon vs liang vs zhang)."""
    general = df[df["condition"].str.startswith("general_attack_")].copy()

    # Determine attack source from attack_idx
    # raccoon: 0-14, liang: 15-24, zhang: 25-34
    def get_attack_source(row):
        idx = row["attack_idx"]
        if idx < 15:
            return "Raccoon"
        elif idx < 25:
            return "Liang"
        else:
            return "Zhang"

    general["attack_source"] = general.apply(get_attack_source, axis=1)
    general["fw_label"] = general["firewall"].map(FIREWALL_LABELS)

    pivot = general.groupby(["fw_label", "attack_source"])["any_exact_leak"].mean().unstack()
    # Reorder
    fw_order = [FIREWALL_LABELS[k] for k in FIREWALL_ORDER]
    pivot = pivot.reindex(fw_order)

    fig, ax = plt.subplots(figsize=(10, 5))
    pivot.plot(kind="bar", ax=ax, width=0.7)
    ax.set_title("Exact Leakage Rate by Attack Type and Defense")
    ax.set_ylabel("Exact Field Leakage Rate")
    ax.set_xlabel("")
    ax.tick_params(axis="x", rotation=30)
    ax.set_ylim(0, 1)
    ax.legend(title="Attack Source")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "attack_type_breakdown.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: attack_type_breakdown.png")


def compute_statistical_tests(df):
    """Statistical comparison between conditions."""
    print("\n" + "="*60)
    print("STATISTICAL ANALYSIS")
    print("="*60)

    general = df[df["condition"].str.startswith("general_attack_")]

    # Compare each firewall vs no-defense using chi-squared test on exact leakage
    no_def = general[general["firewall"] == "none"]["any_exact_leak"]
    n_no_def = len(no_def)
    leak_no_def = no_def.sum()

    print(f"\nNo-defense baseline: {leak_no_def}/{n_no_def} = {no_def.mean():.2%} exact leakage")

    results = []
    for fw_key in ["heuristic", "mild", "moderate", "aggressive"]:
        fw_data = general[general["firewall"] == fw_key]["any_exact_leak"]
        n_fw = len(fw_data)
        leak_fw = fw_data.sum()

        # Chi-squared test
        table = np.array([[leak_no_def, n_no_def - leak_no_def],
                          [leak_fw, n_fw - leak_fw]])
        if table.min() < 5:
            _, p_value = stats.fisher_exact(table)
            test_name = "Fisher exact"
        else:
            chi2, p_value, _, _ = stats.chi2_contingency(table)
            test_name = "Chi-squared"

        # Effect size (phi coefficient)
        n_total = n_no_def + n_fw
        phi = np.sqrt(stats.chi2_contingency(table)[0] / n_total) if table.min() >= 5 else np.nan

        # Bootstrap CI for difference
        diff_boot = []
        for _ in range(1000):
            boot_no = np.random.choice(no_def.values, n_no_def, replace=True)
            boot_fw = np.random.choice(fw_data.values, n_fw, replace=True)
            diff_boot.append(boot_no.mean() - boot_fw.mean())
        ci_low, ci_high = np.percentile(diff_boot, [2.5, 97.5])

        print(f"\n{FIREWALL_LABELS[fw_key]} vs No Defense:")
        print(f"  Leakage: {leak_fw}/{n_fw} = {fw_data.mean():.2%}")
        print(f"  Reduction: {no_def.mean() - fw_data.mean():.2%} [{ci_low:.2%}, {ci_high:.2%}]")
        print(f"  {test_name} p-value: {p_value:.4e}")
        print(f"  Significant (α=0.05): {'YES' if p_value < 0.05 else 'NO'}")

        results.append({
            "comparison": f"{FIREWALL_LABELS[fw_key]} vs No Defense",
            "baseline_rate": no_def.mean(),
            "condition_rate": fw_data.mean(),
            "reduction": no_def.mean() - fw_data.mean(),
            "ci_low": ci_low,
            "ci_high": ci_high,
            "p_value": p_value,
            "test": test_name,
            "significant": p_value < 0.05,
        })

    # ROUGE-L Kruskal-Wallis test across all conditions
    groups = [general[general["firewall"] == fw]["rouge_l_recall"].values for fw in FIREWALL_ORDER]
    h_stat, kw_p = stats.kruskal(*groups)
    print(f"\nKruskal-Wallis (ROUGE-L across all conditions):")
    print(f"  H-statistic: {h_stat:.2f}, p-value: {kw_p:.4e}")

    # Exact-match vs fuzzy comparison
    print(f"\n{'─'*60}")
    print("EXACT-MATCH vs FUZZY QUERY ANALYSIS")
    for fw_key in FIREWALL_ORDER:
        exact_data = df[(df["condition"] == f"exact_match_{fw_key}")]["any_exact_leak"]
        fuzzy_data = df[(df["condition"] == f"fuzzy_{fw_key}")]["any_exact_leak"]
        if len(exact_data) > 0 and len(fuzzy_data) > 0:
            diff = exact_data.mean() - fuzzy_data.mean()
            table = np.array([[exact_data.sum(), len(exact_data) - exact_data.sum()],
                              [fuzzy_data.sum(), len(fuzzy_data) - fuzzy_data.sum()]])
            if min(table.flatten()) < 5:
                _, p = stats.fisher_exact(table)
            else:
                _, p, _, _ = stats.chi2_contingency(table)
            print(f"  {FIREWALL_LABELS[fw_key]}: exact={exact_data.mean():.2%}, fuzzy={fuzzy_data.mean():.2%}, diff={diff:+.2%}, p={p:.4e}")

    return pd.DataFrame(results)


def generate_summary_table(stats_df):
    """Generate a markdown summary table."""
    general = stats_df[stats_df["condition"].str.startswith("general_attack_")].copy()
    general["fw_order"] = general["firewall"].map({k: i for i, k in enumerate(FIREWALL_ORDER)})
    general = general.sort_values("fw_order")

    print("\n" + "="*60)
    print("SUMMARY TABLE (General Attacks)")
    print("="*60)
    print(f"{'Defense':<15} {'Exact Leak':>10} {'Partial Leak':>12} {'ROUGE-L':>10}")
    print("─" * 50)
    for _, row in general.iterrows():
        print(f"{FIREWALL_LABELS[row['firewall']]:<15} {row['exact_leak_rate']:>10.2%} {row['partial_leak_rate']:>12.2%} {row['rouge_l_mean']:>10.3f}")


def main():
    print("Loading results...")
    df = load_results()
    print(f"Loaded {len(df)} results")

    print("\nComputing statistics...")
    stats_df = analyze_leakage(df)

    # Save stats
    stats_df.to_csv(RESULTS_DIR / "leakage_stats.csv", index=False)

    # Generate plots
    print("\nGenerating visualizations...")
    plot_leakage_by_condition(df, stats_df)
    plot_exact_vs_fuzzy(df, stats_df)
    plot_per_field_leakage(stats_df)
    plot_attack_type_breakdown(df)

    # Statistical tests
    test_results = compute_statistical_tests(df)
    test_results.to_csv(RESULTS_DIR / "statistical_tests.csv", index=False)

    # Summary
    generate_summary_table(stats_df)

    print("\n✓ Analysis complete! See figures/ and results/ directories.")


if __name__ == "__main__":
    main()
