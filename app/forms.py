from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TrackCreateForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['performer', 'coperformer', 'song', 'year', 'image', 'author']
