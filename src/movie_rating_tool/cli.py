"""
CLI module for the Movie Rating Tool.
Now using persistent storage via data_loader.
"""

from .data_loader import load_ratings, save_ratings

# Data structures
SAMPLE_MOVIES = [
    "The Dark Knight",
    "Inception",
    "Interstellar",
    "The Matrix"
]  # list

FAVORITE_GENRES = {"Action", "Sci-Fi", "Drama"}  # set

MOVIE_DETAILS = {
    "The Dark Knight": (9.0, "Action, Crime"),
    "Inception": (8.8, "Action, Sci-Fi"),
    "Interstellar": (8.7, "Adventure, Drama, Sci-Fi"),
    "The Matrix": (8.7, "Action, Sci-Fi")
}  # dict of tuples


def show_welcome():
    print("\n" + "="*50)
    print("🎬 Welcome to Movie Rating Tool v0.1.0")
    print("="*50)
    print("Your ratings are now saved automatically!\n")


def show_menu():
    print("\nWhat would you like to do?")
    print("1. Show sample movies (demo data structures)")
    print("2. Add your own rating")
    print("3. List your current ratings")
    print("4. Exit")


def show_sample_movies():
    print("\n📋 Sample Movies (list):")
    for movie in SAMPLE_MOVIES:
        print(f"  • {movie}")

    print("\n❤️  Favorite Genres (set):", FAVORITE_GENRES)

    print("\n📊 Movie Details (dict of tuples):")
    for title, (rating, genres) in MOVIE_DETAILS.items():
        print(f"  • {title} → {rating}/10 | {genres}")


def add_rating(ratings_dict: dict):
    title = input("\nEnter movie title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    while True:
        try:
            rating = float(input("Enter your rating (0.0 - 10.0): "))
            if 0.0 <= rating <= 10.0:
                break
            print("Rating must be between 0.0 and 10.0")
        except ValueError:
            print("Please enter a valid number!")

    ratings_dict[title] = rating
    print(f"✅ Saved: {title} = {rating}/10")


def list_personal_ratings(ratings_dict: dict):
    if not ratings_dict:
        print("\nYou haven't rated any movies yet.")
        return

    print("\n📝 Your Personal Ratings:")
    for title, rating in ratings_dict.items():
        print(f"  • {title}: {rating}/10")


def run_cli():
    """Main entry point with persistent storage."""
    show_welcome()

    # Load saved ratings at startup
    personal_ratings = load_ratings()

    while True:
        show_menu()
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            show_sample_movies()
        elif choice == "2":
            add_rating(personal_ratings)
        elif choice == "3":
            list_personal_ratings(personal_ratings)
        elif choice == "4":
            save_ratings(personal_ratings)   # ← save before exit
            print("\n👋 Thank you! Your ratings have been saved.")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3 or 4.")