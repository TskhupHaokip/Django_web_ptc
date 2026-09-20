import requests as req
from dotenv import load_dotenv
import os
import httpx
from .movie import Movie,EMPTY_IMG,to_movies
load_dotenv()

API_KEY = os.getenv("MOVIE_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

class ApiClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.api_key = API_KEY
        
    async def get_movies(self):
        url = f"{self.base_url}/movie/popular"
        params = {
            "api_key": API_KEY
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)

        response.raise_for_status()
        data = response.json()
        return to_movies(data["results"])
       
    async def search_movies(self, name: str):
        url = f"{self.base_url}/search/movie"
        params = {
            "api_key": API_KEY,
            "query": name
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)

        response.raise_for_status()
        data = response.json()
        return to_movies(data["results"])