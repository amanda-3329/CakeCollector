from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cake, Customization, Tasting
from .forms import CakeForm, TastingForm
import uuid
import boto3

from .models import Cake, Customization, Photo

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'cakecollector'


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
#DETAIL CAKES-----------------------
@login_required
def detail(request, cake_id):
    found_cake = Cake.objects.get(id=cake_id)

# Query to get all customizations not yet selected:

    customizations_not_selected = Customization.objects.exclude(cake=cake_id)

    tasting_form = TastingForm()

    context = {'cake': found_cake, 
    'tasting_form' : tasting_form,
    'customizations' : customizations_not_selected
    }

    return render(request, 'cakes/cake_detail.html', context)

#CREATE CAKES
@login_required
def cake_new(request):
    if request.method == 'GET':
        form = CakeForm()
        context = { 'form': form }
        return render(request, 'cakes/cake_new.html', context)
    else:
        form = CakeForm(request.POST)
        if form.is_valid():
            cake = form.save(commit=False)
            cake.user=request.user
            cake = form.save()
            return redirect('detail', cake.id)


# DELETE CAKE:
@login_required
def delete_cake(request, cake_id):
    cake = Cake.objects.get(id=cake_id)
    cake.delete()
    return redirect('index')

#UPDATE CAKE-------------------------------------------
@login_required
def update_cake(request, cake_id):
    cake = Cake.objects.get(id=cake_id)

    if request.method == 'GET':
        form = CakeForm(instance=cake)
        context = {
            'form': form
        }
        return render(request, 'cakes/cake_edit.html', context)
    else: 
        form = CakeForm(request.POST, instance=cake)
        if form.is_valid():
            cake = form.save()
            return redirect('detail', cake.id)

#-----------ADD TASTING-----------------
@login_required
def taste_cake(request, cake_id):
    form = TastingForm(request.POST)
    if form.is_valid():
        new_tasting = form.save(commit=False)
        new_tasting.cake_id = cake_id
        new_tasting.save()
        return redirect('detail', cake_id)

#---------DELETE TASTING--------------
@login_required
def delete_tasting(request, cake_id, tasting_id):
    cake = Cake.objects.get(id=cake_id)
    found_tasting = Tasting.objects.get(id=tasting_id)
    cake.tasting_set.remove(found_tasting)
   
    return redirect('detail', cake_id = cake_id)
    

#------ADD A CUSTOMIZATION TO A CAKE:
@login_required
def assoc_customizations(request, cake_id, customizations_id):
    Cake.objects.get(id=cake_id).customizations.add(customizations_id)
    return redirect('detail', cake_id)

# ---DELETE CUSTOMIZATION
@login_required
def remove_customization(request, cake_id, customizations_id):
    Cake.objects.get(id=cake_id).customizations.remove(customizations_id)
    return redirect('detail', cake_id=cake_id)

# ADD a PHOTO

@login_required
def add_photo(request, cake_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, cake_id=cake_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', cake_id=cake_id)

# ADD a New Cake as a logged in user:
def cakes_index(request):
    if request.method == 'POST':
        cake_form = CakeForm(request.POST)
        if cake_form.is_valid():
            # Add the user from the request object before saving
            new_cake = cake_form.save(commit=False)
            print('===============')
            print(request.user)
            print('===============')
            new_cake.user = request.user
            new_cake.save()
            return redirect('index')
    cakes = Cake.objects.filter(user=request.user)
    cake_form = CakeForm()
    context = {'cakes': cakes, 'cake_form': cake_form}
    return render(request, 'cakes/index.html', context)

#SIGNUP

def signup(request):
  error_message = ''
  if request.method == 'POST':
  
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)