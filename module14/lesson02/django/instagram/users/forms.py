from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}))

    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}))

    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))

    email = forms.CharField(max_length=100,
                            required=True,
                            widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}))

    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))

    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(
                                    attrs={"class": "form-control", "placeholder": "Confirm password"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))

    password = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))


    class Meta:
        model = User
        fields = ['username', 'password']
