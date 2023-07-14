from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Creating the New user registration form here

class NewUserCreation(UserCreationForm):
    email = forms.EmailField( required=True)
    class Meta:
        model = User
        
        fields = ("Username", "email", "College/Institution/Company", "Mobile_Number","Password1", "Password2")
    
    def save(self, commit= True):
        user = super(NewUserCreation, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user