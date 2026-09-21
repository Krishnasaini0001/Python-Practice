# Day 38: basic rule-based recommendation

movies = {
    "Inception": ["sci-fi", "thriller"],
    "The Notebook": ["romance", "drama"],
    "Interstellar": ["sci-fi", "drama"],
    "Titanic": ["romance", "drama"],
}

def recommend(liked_genre):
    return [m for m, genres in movies.items() if liked_genre in genres]

genre = input("What genre do you like? ").lower()
results = recommend(genre)
print(f"You might like: {', '.join(results) if results else 'nothing found'}")