       
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import OJUser

class OJUserCreationForm(UserCreationForm):
    class Meta:
        model = OJUser
        fields = ['email', 'username', 'password1', 'password2']
