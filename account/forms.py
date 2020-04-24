from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=50, help_text="Обязательное поле")

    class Meta:
        model = Account
        fields = ("username", "first_name", "password1", "password2")

class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ("username", "password")

    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Неверный логин или пароль")