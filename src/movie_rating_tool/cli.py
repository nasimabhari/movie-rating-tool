"""
CLI module for the Movie Rating Tool.
Demonstrates functions, control flow, and all required data structures.
"""

# Data structures
SAMPLE_MOVIES: list[str] = [
    "The Dark Knight",
    "Inception",
    "Interstellar",
    "The Matrix"
]  # list

FAVORITE_GENRES: set[str] = {"Action", "Sci-Fi", "Drama"}  # set

MOVIE_DETAILS: dict[str, tuple[float, str]] = {
    "The Dark Knight": (9.0, "Action, Crime"),
    "Inception": (8.8, "Action, Sci-Fi"),
    "Interstellar": (8.7, "Adventure, Drama, Sci-Fi"),
    "The Matrix": (8.7, "Action, Sci-Fi")
}  # dictionary with tuples inside


def show_welcome() -> None:
    """Print welcome message."""
    print("\n" + "="*50)
    print("🎬 Welcome to Movie Rating Tool v0.1.0")
    print("="*50)
    print("This tool lets you rate movies and compare with online ratings.\n")


def show_menu() -> None:
    """Display the main menu."""
    print("\nWhat would you like to do?")
    print("1. Show sample movies (demo data structures)")
    print("2. Add your own rating")
    print("3. List your current ratings")
    print("4. Exit")


def show_sample_movies() -> None:
    """Demonstrate list, set, dict and tuple."""
    print("\n📋 Sample Movies (list):")
    for movie in SAMPLE_MOVIES:          # for loop
        print(f"  • {movie}")

    print("\n❤️  Favorite Genres (set):", FAVORITE_GENRES)

    print("\n📊 Movie Details (dict of tuples):")
    for title, (rating, genres) in MOVIE_DETAILS.items():
        print(f"  • {title} → IMDb: {rating}/10 | Genres: {genres}")


def add_rating(ratings: dict) -> None:
    """Add a new personal rating (modifies the dict passed in)."""
    title = input("\nEnter movie title: ").strip()
    while True:
        try:
            rating = float(input("Enter your rating (0.0 - 10.0): "))
            if 0.0 <= rating <= 10.0:
                break
            print("Rating must be between 0.0 and 10.0")
        except ValueError:
            print("Please enter a valid number!")

    ratings[title] = rating
    print(f"✅ Saved: {title} = {rating}/10")


def list_personal_ratings(ratings: dict) -> None:
    """Show all personal ratings."""
    if not ratings:
        print("\nYou haven't rated any movies yet.")
        return

    print("\n📝 Your Personal Ratings:")
    for title, rating in ratings.items():
        print(f"  • {title}: {rating}/10")


def run_cli() -> None:
    """Main CLI loop (entry point)."""
    show_welcome()

    # Personal ratings stored in memory for now (will save to file in next phase)
    personal_ratings: dict[str, float] = {}

    while True:                                 # main loop
        show_menu()
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            show_sample_movies()
        elif choice == "2":
            add_rating(personal_ratings)
        elif choice == "3":
            list_personal_ratings(personal_ratings)
        elif choice == "4":
            print("\n👋 Thank you for using Movie Rating Tool!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3 or 4.")