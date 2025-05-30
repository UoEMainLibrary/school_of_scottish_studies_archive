from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=80)
    status = forms.CharField(max_length=80)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "status", "email", "password1", "password2")