from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def equipe(request):
    return render(request, 'app/equipe.html')

def sobre(request):
    return render(request, 'app/sobre.html')


