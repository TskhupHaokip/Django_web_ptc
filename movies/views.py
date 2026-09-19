from django.shortcuts import render
from .tmdb_client import ApiClient

client = ApiClient()

async def home(request):
    Movies = await client.async_get_movies()
    print(Movies)

    return render(request,"home.html",{"movies":Movies})