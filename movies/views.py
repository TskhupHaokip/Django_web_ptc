from django.shortcuts import render
from .movie import Movies

def home(request):

    return render(request,"home.html",{"movies":Movies})