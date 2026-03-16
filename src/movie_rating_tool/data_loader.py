"""
Data loading and saving module.
Handles personal ratings stored in JSON file.
Demonstrates file I/O and dictionary usage.
"""

import json
from pathlib import Path

DATA_FILE = Path("data/personal_ratings.json")


def load_ratings() -> dict[str, float]:
    """Load personal ratings from JSON file. Returns empty dict if file doesn't exist."""
    if not DATA_FILE.exists():
        return {}  # first time user runs the app

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"✅ Loaded {len(data)} saved ratings from {DATA_FILE}")
        return data
    except Exception as e:
        print(f"⚠️  Could not load ratings: {e}")
        return {}


def save_ratings(ratings: dict[str, float]) -> None:
    """Save personal ratings to JSON file."""
    try:
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(ratings, f, indent=4, ensure_ascii=False)

        print(f"💾 Saved {len(ratings)} ratings to {DATA_FILE}")
    except Exception as e:
        print(f"⚠️  Could not save ratings: {e}")