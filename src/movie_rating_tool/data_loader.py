"""
Data loading and saving module.
Now also loads the real IMDb dataset (~1000 movies) using Pandas.
"""

import json
from pathlib import Path
import pandas as pd   # ← course requirement

DATA_FILE = Path("data/personal_ratings.json")
IMDB_URL = "https://raw.githubusercontent.com/LearnDataSci/articles/master/Python%20Pandas%20Tutorial%20A%20Complete%20Introduction%20for%20Beginners/IMDB-Movie-Data.csv"


def load_ratings() -> dict[str, float]:
    """Load personal ratings from JSON """
    if not DATA_FILE.exists():
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"✅ Loaded {len(data)} saved personal ratings")
        return data
    except Exception as e:
        print(f"⚠️ Could not load personal ratings: {e}")
        return {}


def save_ratings(ratings: dict[str, float]) -> None:
    """Save personal ratings to JSON (unchanged)."""
    try:
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(ratings, f, indent=4, ensure_ascii=False)
        print(f"💾 Saved {len(ratings)} personal ratings")
    except Exception as e:
        print(f"⚠️ Could not save: {e}")


def load_online_ratings() -> pd.DataFrame:
    """Fetch real IMDb dataset (~1000 movies) from the internet using Pandas."""
    try:
        print("📥 Fetching 1,000 IMDb movies from online dataset...")
        df = pd.read_csv(IMDB_URL)
        print(f"✅ Successfully loaded {len(df)} movies from IMDb!")
        df = df[["Title", "Genre", "Rating"]].copy()
        return df
    except Exception as e:
        print(f"⚠️ Failed to load online data: {e}")
        print("Using empty dataset for now.")
        return pd.DataFrame(columns=["Title", "Genre", "Rating"])