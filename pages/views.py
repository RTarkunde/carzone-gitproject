from django.shortcuts import render
from .models import Team

def home(request):
    teams = Team.objects.all()
    data = {
        'teams': teams
    }
    return render(request, 'pages/home.html', data)# Create your views here.

def about(request):
    return render(request, 'pages/about.html')# Create your views here.

def services(request):
    return render(request, 'pages/services.html')# Create your views here.

def contact(request):
    return render(request, 'pages/contact.html')# Create your views here.

def IT104pc(request):
    return render(request, 'pages/IT104pc.html')# Create your views here.
