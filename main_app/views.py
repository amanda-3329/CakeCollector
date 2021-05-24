from django.shortcuts import render
from django.http import HttpResponse
from .models import Cake



# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):

    cakes = Cake.objects.all()

    context = { 'cakes': cakes }

    return render(request, 'cakes/index.html', context)

    #converts cake object into cake dictionary:

def detail(request, cake_id):
    found_cake = Cake.objects.get(id=cake_id)

    context = {'cake': found_cake}

    return render(request, 'cakes/cake_detail.html', context)
