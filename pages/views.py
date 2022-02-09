from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')# Create your views here.

def about(request):
    return render(request, 'pages/about.html')# Create your views here.

def services(request):
    return render(request, 'pages/services.html')# Create your views here.

def contact(request):
    return render(request, 'pages/contact.html')# Create your views here.

def IT104pc(request):
    return render(request, 'pages/IT104pc.html')# Create your views here.
