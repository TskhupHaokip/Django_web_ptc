class Movie:
    def __init__(self, title, poster, rating, year):
        self.title = title
        self.poster = poster
        self.rating = rating
        self.year = year

EMPTY_IMG = "../static/assets/fail.svg"

Movies = [
        Movie("Inception", EMPTY_IMG, 8.8, 2010),
        Movie("Interstellar", EMPTY_IMG, 8.7, 2014),
        Movie("The Dark Knight", EMPTY_IMG, 9.0, 2008),
        Movie("Avengers: Endgame", EMPTY_IMG, 8.4, 2019),
    ]