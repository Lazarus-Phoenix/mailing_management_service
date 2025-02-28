from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar', 'phone', 'country']

