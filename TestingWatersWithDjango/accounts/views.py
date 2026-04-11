from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  #  Create user

            # Add the user to the "Voter" group
            voter_group = Group.objects.get(name="Voter")   # Get group
            user.groups.add(voter_group)  # Add user to group

            login(request, user)
            return redirect("home") # Redirect to home page after registration
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})

def home(request):
    return render(request, "accounts/home.html")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})
