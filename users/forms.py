
from django import forms
from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar', 'phone', 'country']

class UserRegistrationForm(forms.ModelForm):
    pass
