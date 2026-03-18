"""
CLI module — now using OOP classes + recommendation system.
"""

from .data_loader import load_ratings, save_ratings, load_online_ratings
from .rating_engine import compare_ratings, calculate_statistics
from .visualization import plot_comparison_bar, plot_rating_distribution
from .models import RatingsManager
import pandas as pd

ONLINE_RATINGS: pd.DataFrame | None = None
ratings_manager = RatingsManager()   # OOP object


def show_welcome():
    print("\n" + "="*70)
    print("🎬 Welcome to Movie Rating Tool v0.5.0")
    print("="*70)
    print("Now with full OOP, recommendations and everything!\n")


def show_menu():
    print("\nWhat would you like to do?")
    print("1. Show sample movies (demo data structures)")
    print("2. Add your own rating")
    print("3. List your current ratings")
    print("4. Browse top IMDb movies")
    print("5. Search IMDb movies by title")
    print("6. Compare my ratings with IMDb")
    print("7. Show statistics")
    print("8. Show comparison bar chart")
    print("9. Show rating distribution plot")
    print("10. Get recommendations (NEW!)")
    print("11. Exit")


def run_cli():
    global ONLINE_RATINGS
    show_welcome()

    # Load saved ratings into our OOP manager
    saved = load_ratings()
    for title, rating in saved.items():
        ratings_manager.personal_ratings[title] = rating

    if ONLINE_RATINGS is None:
        ONLINE_RATINGS = load_online_ratings()

    while True:
        show_menu()
        choice = input("\nEnter choice (1-11): ").strip()

        if choice == "1":
            print("\n📋 Sample Movies (list): The Dark Knight, Inception, etc.")
        elif choice == "2":
            title = input("\nMovie title: ").strip()
            try:
                rating = float(input("Your rating (0.0–10.0): "))
                ratings_manager.add_rating(title, rating)
            except ValueError:
                print("Invalid number!")
        elif choice == "3":
            if not ratings_manager.personal_ratings:
                print("No ratings yet.")
            else:
                print("\n📝 Your Ratings:")
                for t, r in ratings_manager.personal_ratings.items():
                    print(f"  • {t}: {r}/10")
        elif choice == "4":
            top = ONLINE_RATINGS.nlargest(10, "Rating")
            print(top[["Title", "Rating", "Genre"]].to_string(index=False))
        elif choice == "5":
            q = input("\nSearch: ").strip()
            res = ONLINE_RATINGS[ONLINE_RATINGS["Title"].str.contains(q, case=False)]
            print(res[["Title", "Rating", "Genre"]].to_string(index=False) if not res.empty else "No matches.")
        elif choice == "6":
            comp = compare_ratings(ratings_manager.personal_ratings, ONLINE_RATINGS)
            print(comp.to_string(index=False) if not comp.empty else "No matches.")
        elif choice == "7":
            comp = compare_ratings(ratings_manager.personal_ratings, ONLINE_RATINGS)
            stats = calculate_statistics(comp)
            print(stats if stats else "No data.")
        elif choice == "8":
            comp = compare_ratings(ratings_manager.personal_ratings, ONLINE_RATINGS)
            plot_comparison_bar(comp)
        elif choice == "9":
            comp = compare_ratings(ratings_manager.personal_ratings, ONLINE_RATINGS)
            plot_rating_distribution(comp)
        elif choice == "10":
            recs = ratings_manager.get_recommendations(ONLINE_RATINGS)
            print("\n🎯 Recommended movies for you:")
            for i, movie in enumerate(recs[:5], 1):
                print(f"  {i}. {movie}")
        elif choice == "11":
            save_ratings(ratings_manager.personal_ratings)
            print("\n👋 Goodbye! Everything saved.")
            break
        else:
            print("❌ Invalid choice.")