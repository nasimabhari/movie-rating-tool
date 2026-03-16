"""
CLI module, now with comparison and statistics.
"""

from .data_loader import load_ratings, save_ratings, load_online_ratings
from .rating_engine import compare_ratings, calculate_statistics
import pandas as pd

# Global online dataset 
ONLINE_RATINGS: pd.DataFrame | None = None


def show_welcome():
    print("\n" + "="*60)
    print("🎬 Welcome to Movie Rating Tool v0.3.0")
    print("="*60)
    print("Compare your ratings with real IMDb data + statistics!\n")


def show_menu():
    print("\nWhat would you like to do?")
    print("1. Show sample movies (demo data structures)")
    print("2. Add your own rating")
    print("3. List your current ratings")
    print("4. Browse top IMDb movies")
    print("5. Search IMDb movies by title")
    print("6. Compare my ratings with IMDb (NEW!)")
    print("7. Show statistics (NEW!)")
    print("8. Exit")


def show_sample_movies():
    print("\n📋 Sample Movies (list): The Dark Knight, Inception, etc.")
    print("❤️  Favorite Genres (set): Action, Sci-Fi, Drama")


def add_rating(ratings_dict: dict):
    title = input("\nEnter movie title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    while True:
        try:
            rating = float(input("Your rating (0.0–10.0): "))
            if 0.0 <= rating <= 10.0:
                break
            print("Rating must be 0.0–10.0")
        except ValueError:
            print("Please enter a number!")
    ratings_dict[title] = rating
    print(f"✅ Saved: {title} = {rating}/10")


def list_personal_ratings(ratings_dict: dict):
    if not ratings_dict:
        print("\nNo personal ratings yet.")
        return
    print("\n📝 Your Personal Ratings:")
    for title, rating in ratings_dict.items():
        print(f"  • {title}: {rating}/10")


def show_top_imdb_movies(df: pd.DataFrame):
    if df.empty:
        print("No online data.")
        return
    top10 = df.nlargest(10, "Rating")
    print("\n🏆 Top 10 IMDb Movies:")
    print(top10[["Title", "Rating", "Genre"]].to_string(index=False))


def search_imdb_movies(df: pd.DataFrame):
    if df.empty:
        print("No online data.")
        return
    query = input("\nSearch movie title: ").strip()
    if not query:
        return
    results = df[df["Title"].str.contains(query, case=False)]
    if results.empty:
        print("No matches found.")
    else:
        print(f"\nFound {len(results)} matches:")
        print(results[["Title", "Rating", "Genre"]].to_string(index=False))


def show_comparison(comparison_df: pd.DataFrame):
    if comparison_df.empty:
        return
    print("\n🔄 Your Ratings vs IMDb:")
    print(comparison_df.to_string(index=False))
    print("\n(Difference = Your Rating - IMDb Rating)")


def show_statistics(stats: dict):
    if not stats:
        print("\nNo comparison data yet.")
        return
    print("\n📊 Statistics:")
    print(f"  Compared movies          : {stats['number_of_compared_movies']}")
    print(f"  Mean difference          : {stats['mean_difference']}")
    print(f"  Median difference        : {stats['median_difference']}")
    print(f"  Your average rating      : {stats['average_your_rating']}")
    print(f"  IMDb average rating      : {stats['average_imdb_rating']}")


def run_cli():
    global ONLINE_RATINGS
    show_welcome()

    personal_ratings = load_ratings()
    if ONLINE_RATINGS is None:
        ONLINE_RATINGS = load_online_ratings()

    while True:
        show_menu()
        choice = input("\nEnter choice (1-8): ").strip()

        if choice == "1":
            show_sample_movies()
        elif choice == "2":
            add_rating(personal_ratings)
        elif choice == "3":
            list_personal_ratings(personal_ratings)
        elif choice == "4":
            show_top_imdb_movies(ONLINE_RATINGS)
        elif choice == "5":
            search_imdb_movies(ONLINE_RATINGS)
        elif choice == "6":
            comparison_df = compare_ratings(personal_ratings, ONLINE_RATINGS)
            show_comparison(comparison_df)
        elif choice == "7":
            comparison_df = compare_ratings(personal_ratings, ONLINE_RATINGS)
            stats = calculate_statistics(comparison_df)
            show_statistics(stats)
        elif choice == "8":
            save_ratings(personal_ratings)
            print("\n👋 Goodbye! Ratings saved.")
            break
        else:
            print("❌ Invalid choice — please pick 1-8.")