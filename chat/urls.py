from django.urls import path,include
from .views import *

urlpatterns = [
    path("start",start_chat,name="start_chat")
]