"""
Rating engine module — comparison and statistics.
Uses Pandas for merging + NumPy for mean/median.
FIXED: duplicate Title columns after merge.
"""

import pandas as pd
import numpy as np


def compare_ratings(personal_ratings: dict[str, float], online_df: pd.DataFrame) -> pd.DataFrame:
    """Compare personal ratings with IMDb ratings. """
    if not personal_ratings:
        print("You have no personal ratings yet.")
        return pd.DataFrame()

    # Convert personal dict to DataFrame
    personal_df = pd.DataFrame(
        list(personal_ratings.items()), 
        columns=["Title", "Your Rating"]
    )

    # Normalize for matching
    online_copy = online_df.copy()
    online_copy["Title_lower"] = online_copy["Title"].str.lower().str.strip()
    personal_df["Title_lower"] = personal_df["Title"].str.lower().str.strip()

    # Merge on normalized title
    merged = personal_df.merge(
        online_copy, 
        on="Title_lower", 
        how="inner"
    )

    if merged.empty:
        print("No matching movies found in IMDb dataset.")
        return pd.DataFrame()

    if "Title_y" in merged.columns:
        merged = merged.rename(columns={"Title_y": "Title"})
        merged = merged.drop(columns=["Title_x"], errors="ignore")

    # Calculate difference (positive = you rated higher)
    merged["Difference"] = merged["Your Rating"] - merged["Rating"]
    merged = merged.rename(columns={"Rating": "IMDb Rating"})

    # Final clean columns
    result = merged[["Title", "Your Rating", "IMDb Rating", "Difference", "Genre"]].copy()
    return result


def calculate_statistics(comparison_df: pd.DataFrame) -> dict:
    """Return basic statistics using NumPy."""
    if comparison_df.empty:
        return {}

    diffs = comparison_df["Difference"].to_numpy()

    return {
        "number_of_compared_movies": len(comparison_df),
        "mean_difference": round(float(np.mean(diffs)), 2),
        "median_difference": round(float(np.median(diffs)), 2),
        "average_your_rating": round(float(np.mean(comparison_df["Your Rating"])), 2),
        "average_imdb_rating": round(float(np.mean(comparison_df["IMDb Rating"])), 2),
    }