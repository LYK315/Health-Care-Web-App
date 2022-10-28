from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def findadoctor(request):
    return render(request, "findadoctor.html")

def specialities(request):
    return render(request, "specialities.html")

# Create your views here.
