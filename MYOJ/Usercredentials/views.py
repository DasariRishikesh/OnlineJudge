from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import OJUserCreationForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.
def index(request):
    return HttpResponse("Here is the first object")

def login(request):
    return HttpResponse("You have login is successfull!")

def register_view(request):
    if request.method == 'POST':
        form = OJUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = OJUserCreationForm()

    return render(request, 'registration.html', {'form': form})
