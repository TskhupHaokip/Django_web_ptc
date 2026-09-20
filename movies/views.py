from django.shortcuts import render, redirect
from .tmdb_client import ApiClient


client = ApiClient()
MOVIES = []
Favs = []

def search(request):
    pass

def add_fav(request, movie_id):
    if request.method == "POST":
        print("about to add")

        for movie in MOVIES:
            if movie.id == movie_id:

                already_fav = any(
                    fav.id == movie_id
                    for fav in Favs
                )

                if not already_fav:
                    Favs.append(movie)
                    print("added")

                break

    return redirect(request.META.get("HTTP_REFERER", "home"))


def favourites(request):
    return render(
        request,
        "favourites.html",
        {"favourites": Favs}
    )


async def home(request):
    global MOVIES

    query = request.GET.get("q", "").strip()

    if query:
        movies = await client.search_movies(query)
    else:
        movies = await client.get_movies()

    MOVIES = movies

    return render(
        request,
        "home.html",
        {
            "movies": movies,
            "favourite_ids": [movie.id for movie in Favs]
        }
    )