from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {'titulo': 'Página Principal'}
    return render(request, 'home.html', context)
