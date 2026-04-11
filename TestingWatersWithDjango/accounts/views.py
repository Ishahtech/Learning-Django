from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Add the user to the "Voter" group
            voter_group = Group.objects.get(name="Voter")
            user.groups.add(voter_group)

            login(request, user)
            return redirect("home") 
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})

def home(request):
    return render(request, "accounts/home.html")
# Create your views here.
