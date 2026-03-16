"""
CLI module. now with real IMDb data.
"""

from .data_loader import load_ratings, save_ratings, load_online_ratings
import pandas as pd 

ONLINE_RATINGS: pd.DataFrame | None = None


def show_welcome():
    print("\n" + "="*60)
    print("🎬 Welcome to Movie Rating Tool v0.2.0")
    print("="*60)
    print("Now using real IMDb data (1,000 movies)!\n")


def show_menu():
    print("\nWhat would you like to do?")
    print("1. Show sample movies (demo data structures)")
    print("2. Add your own rating")
    print("3. List your current ratings")
    print("4. Browse top IMDb movies (new!)")
    print("5. Search IMDb movies by title")
    print("6. Exit")


def show_sample_movies():
    print("\n📋 Sample Movies (list): The Dark Knight, Inception, etc.")
    print("❤️  Favorite Genres (set): Action, Sci-Fi, Drama")
    print("📊 Movie Details (dict of tuples): ...")


def add_rating(ratings_dict: dict):
    """Add personal rating. """
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
        print("No online data available.")
        return
    top10 = df.nlargest(10, "Rating")
    print("\n🏆 Top 10 IMDb Movies (by Rating):")
    print(top10[["Title", "Rating", "Genre"]].to_string(index=False))


def search_imdb_movies(df: pd.DataFrame):
    if df.empty:
        print("No online data.")
        return
    query = input("\nSearch movie title (or part of it): ").strip()
    if not query:
        return
    results = df[df["Title"].str.contains(query, case=False)]
    if results.empty:
        print("No matches found.")
    else:
        print(f"\nFound {len(results)} matches:")
        print(results[["Title", "Rating", "Genre"]].to_string(index=False))


def run_cli():
    global ONLINE_RATINGS
    show_welcome()

    personal_ratings = load_ratings()
    if ONLINE_RATINGS is None:
        ONLINE_RATINGS = load_online_ratings()

    while True:
        show_menu()
        choice = input("\nEnter choice (1-6): ").strip()

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
            save_ratings(personal_ratings)
            print("\n👋 Goodbye! Ratings saved.")
            break
        else:
            print("❌ Invalid choice — please pick 1-6.")