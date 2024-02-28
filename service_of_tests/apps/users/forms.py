from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from apps.users.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput)
    date_of_birth = forms.DateField(label="Дата рождения", widget=forms.DateInput)
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "date_of_birth", "password1", "password2")


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput)
    password = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "date_of_birth", "password1", "password2")
