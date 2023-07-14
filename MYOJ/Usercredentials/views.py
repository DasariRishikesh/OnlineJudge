from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Here is the first object")

def login(request):
    return HttpResponse("You have login is successfull!")

def register(request):
    return HttpResponse("You have registered successfully!")