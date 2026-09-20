import random

EMPTY_IMG = "../static/assets/fail.svg"

TMDB_GENRES = {
    28: "Action", 12: "Adventure", 16: "Animation", 35: "Comedy", 
    80: "Crime", 99: "Documentary", 18: "Drama", 10751: "Family", 
    14: "Fantasy", 36: "History", 27: "Horror", 10402: "Music", 
    9648: "Mystery", 10749: "Romance", 878: "Science Fiction", 
    10770: "TV Movie", 53: "Thriller", 10752: "War", 37: "Western"
}

def random_runtime():
    minutes = random.randint(90, 210)
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}h {mins}m"

def get_genres(genre_ids):
    return [TMDB_GENRES[genre_id] for genre_id in genre_ids if genre_id in TMDB_GENRES]

class Movie:
    def __init__(self,movie_id,title, poster, rating, year,description,genres="N/A",runtime="2h 30 m"):
        self.id = movie_id
        self.title = title
        self.poster = poster
        self.rating = rating
        self.year = year
        self.description = description
        self.genres = genres
        self.runtime = runtime

def to_movies(results):
    movies = []
    image_url =  "https://image.tmdb.org/t/p/w500"
     
    for movie in results:
        genres = get_genres(movie["genre_ids"])
        runtime = random_runtime()
        poster = (
            f"{image_url}{movie['poster_path']}"
            if movie["poster_path"]
            else EMPTY_IMG
        )
        movies.append(
            Movie(
                movie["id"],
                movie["title"],
                poster,
                movie["vote_average"],
                movie["release_date"][:4] if movie["release_date"] else "",
                movie["overview"],
                genres,
                runtime

            )
        )
    return movies
