from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User

# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()
            from django.contrib.auth import login
            login(request, newUser)
            return redirect("index")
        else:
            context = {"form": form}
            return render(request, "user/register.html", context)
    else:
        form = RegisterForm()
        context = {"form": form}
        return render(request, "user/register.html", context)


def loginUser(request):
    return render(request, "user/login.html")


def logoutUser(request):
    pass
