from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("search",search,name="search"),
    path("favourites",favourites,name="favourites"),
    path("add-fav/<int:movie_id>/", add_fav, name="add_fav")

]