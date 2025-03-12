import requests
import random


genre = input("Enter a movie genre: ").strip().lower()

api_key = "f85a0c60675b032fbcbe633e378a7879"
url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"


response = requests.get(url)
data = response.json()


genre_id = None
for item in data.get("genres", []):
    if item["name"].lower() == genre:
        genre_id = item["id"]
        break

if genre_id:

    movies_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}"
    movies_response = requests.get(movies_url)
    movies_data = movies_response.json()

    movies = movies_data.get("results", [])
    if movies:
        random_movie = random.choice(movies)
        print(f"Recommended Movie: {random_movie['title']}")
    else:
        print("No movies found for this genre.")
else:
    print("Genre not found.")
