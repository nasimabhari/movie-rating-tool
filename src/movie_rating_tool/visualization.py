"""
Visualization module using Matplotlib and Seaborn.
Generates charts for comparison and rating distribution.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_comparison_bar(comparison_df: pd.DataFrame) -> None:
    """Bar chart: Your Rating vs IMDb Rating"""
    if comparison_df.empty:
        print("No comparison data to plot.")
        return

    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))

    # Melt the DataFrame for easy seaborn barplot
    plot_data = comparison_df.melt(
        id_vars=["Title"],
        value_vars=["Your Rating", "IMDb Rating"],
        var_name="Rating Type",
        value_name="Rating"
    )

    ax = sns.barplot(
        data=plot_data,
        x="Title",
        y="Rating",
        hue="Rating Type",
        palette=["#4CAF50", "#2196F3"]
    )

    plt.title("Your Ratings vs IMDb Ratings", fontsize=16, pad=20)
    plt.xlabel("Movie Title")
    plt.ylabel("Rating (0-10)")
    plt.xticks(rotation=45, ha="right")
    plt.legend(title="Rating Type")
    plt.tight_layout()
    plt.show()


def plot_rating_distribution(comparison_df: pd.DataFrame) -> None:
    """Histogram: Distribution of rating differences."""
    if comparison_df.empty:
        print("No data for distribution plot.")
        return

    sns.set_style("whitegrid")
    plt.figure(figsize=(9, 6))

    sns.histplot(
        data=comparison_df,
        x="Difference",
        bins=10,
        kde=True,
        color="#FF5722"
    )

    plt.title("Distribution of Rating Differences (You - IMDb)", fontsize=16)
    plt.xlabel("Difference (positive = you rated higher)")
    plt.ylabel("Number of Movies")
    plt.axvline(0, color="red", linestyle="--", label="No difference")
    plt.legend()
    plt.tight_layout()
    plt.show()