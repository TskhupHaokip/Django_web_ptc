from django.urls import path
from .views import *

urlpatterns = [
    path("", home),
    path("login/",login ),
    path("register/",register ),
    path("subscription",subsciption,name="subscription"),
    path("plans/free",free_page,name="free_page"),
    path("plans/pro", pro_page, name="pro_page"),
    path("plans/business", business_page, name="business_page"),
    path("subscription/upgrade",upgrade_plan,name="upgrade_plan" ),
    path("users/profile",profile,name="profile")

]