from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})))
    first_name = forms.CharField(widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})))
    last_name = forms.CharField(widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})))
    password1 = forms.CharField(
        widget=(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})))
    password2 = forms.CharField(
        widget=(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'})))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', "username", "password1", "password2")
