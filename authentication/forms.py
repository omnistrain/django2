from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from . import models

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Identifiant')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, label='password')


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'role']



class upload_profil_photo_form(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['photo']