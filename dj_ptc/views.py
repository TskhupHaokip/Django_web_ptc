from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import LoginForm,RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from .models import User,Subscription

@login_required
def profile(request):
    return render(request, "users/profile.html")


def pro_page(request):
    return render(request, "subs_plan/pro.html")

def upgrade_plan(request):
    return HttpResponse("Upgraded Successfuly")

def business_page(request):
    return render(request, "subs_plan/business.html")

def free_page(request):
    return render(request, "subs_plan/free.html")

def subsciption(request):
    subs = Subscription.objects.filter(user=request.user).first()
    return render(request, "users/subscription.html", {"subs":subs})


@login_required(login_url="/login/")
def home(request):
    return render(request, "home.html")

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        messages.success(request, "Account created successfully.")
        return redirect("")

    return render(request, "users/register.html", {"form": form})

def view_users(request):
    users = User.objects.all()
    return HttpResponse(f"{users}")

def login(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data["username"]

        try:
            actual_username = User.objects.get(
                username__iexact=username
            ).username
        except User.DoesNotExist:
            actual_username = username

        user = authenticate(
            username=actual_username,
            password=form.cleaned_data["password"]
        )

        if user:
            auth_login(request, user)
            return redirect("/")

        messages.error(request, "Invalid username or password.")

    return render(request, "users/login.html", {"form": form})