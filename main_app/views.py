from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cake
from .forms import CakeForm



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

#CREATE CAKES

def create_cake(request):
    if request.method == 'GET':
        form = CakeForm()
        context = { 'form': form }
        return render(request, 'cakes/cake_new.html', context)
    else:
        form = CakeForm(request.POST)
        if form.is_valid():
            cake = form.save()
            return redirect('detail', cake.id)


# DELETE CAKE:

def delete_cake(request, cake_id):
    cake = Cake.objects.get(id=cake_id)
    cake.delete()
    return redirect('index')

#UPDATE CAKE-------------------------------------------
def update_cake(request, cake_id):
    cake = Cake.objects.get(id=cake_id)

    if request.method == 'GET':
        form= CakeForm(instance=cake)
        context = {
            'form': form
        }
        return render(request, 'cakes/cake_edit.html', context)
    else: 
        form = CakeForm(request.POST, instance=cake)
        if form.is_valid():
            cake = form.save()
            return redirect('detail', cake.id)


