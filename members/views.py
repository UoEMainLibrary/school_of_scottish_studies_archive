from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from sssa_app.views import *
from sssa_project.urls import *
from django.contrib.auth.forms import  UserCreationForm
from .forms import *
from django.core.mail import send_mail
from django.conf import settings

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('sssa_home')
            else:
                messages.error(request, "Your account is pending approval. Please wait for admin approval.")
                return redirect('login')
        else:
            messages.error(request, "Sorry, wrong username or password. Please try again.")
            return redirect('login')
    else:
        return render(request, 'authentication/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out!")
    return redirect('sssa_home')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # new users are inactive
            user.save()

            # Send email notification to admin
            send_mail(
                subject="New User Registration Pending Approval",
                message=(
                    f"A new user has registered:\n\n"
                    f"Username: {user.username}\n"
                    f"First name: {user.first_name}\n"
                    f"Last name: {user.last_name}\n"
                    f"Email: {user.email}\n\n"
                    f"Please activate them in the admin panel."
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],  # define ADMIN_EMAIL in settings.py
            )

            messages.info(request, "Your registration is successful! Please wait for admin approval.")
            return redirect('login')
    else:
        form = RegisterUserForm()

    return render(request, 'authentication/register_user.html', {
        'form': form,
    })