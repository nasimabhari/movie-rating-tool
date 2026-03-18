"""
OOP Models — demonstrates Classes & Object-Oriented Programming.
"""

class Movie:
    """Represents one movie with title, genre and IMDb rating."""
    def __init__(self, title: str, genre: str, imdb_rating: float):
        self.title = title
        self.genre = genre
        self.imdb_rating = imdb_rating

    def __str__(self) -> str:
        return f"{self.title} ({self.imdb_rating}/10) — {self.genre}"

    def to_dict(self) -> dict:
        return {"title": self.title, "genre": self.genre, "imdb_rating": self.imdb_rating}


class RatingsManager:
    """Manages personal ratings and provides recommendations (OOP core)."""
    def __init__(self):
        self.personal_ratings: dict[str, float] = {}   # title → your rating

    def add_rating(self, title: str, rating: float) -> None:
        if 0.0 <= rating <= 10.0:
            self.personal_ratings[title] = rating
            print(f"✅ Added: {title} = {rating}/10")
        else:
            print("Rating must be between 0.0 and 10.0")

    def get_recommendations(self, online_df) -> list[str]:
        """Simple genre-based recommendation (bonus feature)."""
        if not self.personal_ratings:
            return ["Add some ratings first!"]

        # Find your favorite genres (from highest rated movies)
        favorite_genres = set()
        for title, your_rating in list(self.personal_ratings.items())[-3:]:  # last 3
            match = online_df[online_df["Title"].str.lower() == title.lower()]
            if not match.empty:
                genres = match.iloc[0]["Genre"].split(",")
                favorite_genres.update(g.strip() for g in genres)

        # Recommend unrated movies from favorite genres
        recommendations = []
        for _, row in online_df.iterrows():
            if row["Title"] not in self.personal_ratings:
                movie_genres = set(g.strip() for g in row["Genre"].split(","))
                if movie_genres & favorite_genres:   # intersection
                    recommendations.append(row["Title"])
                    if len(recommendations) >= 5:
                        break

        return recommendations if recommendations else ["No recommendations yet — rate more movies!"]