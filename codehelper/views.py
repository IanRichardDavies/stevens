from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def code(request):
    return render(request, 'code_helper.html')

def add_components(request):
    return render(request, 'add_components.html')
