import requests as req
from dotenv import load_dotenv
import os
import httpx
from .movie import Movie,EMPTY_IMG
load_dotenv()

API_KEY = os.getenv("MOVIE_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

class ApiClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.api_key = API_KEY
        self.image_url =  "https://image.tmdb.org/t/p/w500"

    def get_movies(self):
        url = f"{self.base_url}/movie/popular"
        params = {
            "api_key": API_KEY
        }

        response = req.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        movies = []

        for movie in data["results"]:
            title = movie["title"]
            poster = movie["poster_path"] or EMPTY_IMG
            rating = movie["vote_average"]
            year = movie["release_date"][:4] if movie["release_date"] else ""

            movies.append(
                Movie(
                    title,
                    poster,
                    rating,
                    year
                )
            )

        return movies

    async def async_get_movies(self):
        url = f"{self.base_url}/movie/popular"
        params = {
            "api_key": API_KEY
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)

        response.raise_for_status()
        data = response.json()
        movies = []
        for movie in data["results"]:
            movies.append(
                Movie(
                    movie["title"],
                    f"{self.image_url}{movie['poster_path']}",
                    movie["vote_average"],
                    movie["release_date"][:4]
                )
            )
        return movies
       
    def search_movies(self,name:str):
        pass

    async def async_search_movies(self, name: str):
        pass