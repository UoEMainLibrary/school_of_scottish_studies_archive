from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from sssa_app.views import *
from sssa_project.urls import *
from django.contrib.auth.forms import  UserCreationForm
from .forms import *

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('sssa_home')
        else:
            messages.success(request, ("Sorry, wrong username or password. Please try again"))
            return redirect('login')

    else:
        return render(request, 'authentication/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Log Out!"))
    return redirect('sssa_home')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('sssa_home')
    else:
        form = RegisterUserForm()

    return render(request, 'authentication/register_user.html', {
        'form': form,
    })