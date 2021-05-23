from django.shortcuts import render
from django.http import HttpResponse

class Cake:
    def __init__ (self, name, flavor, icing_flavor, description):
        self.name = name
        self.flavor = flavor
        self.icing_flavor = icing_flavor
        self.description = description
#cakes list from the above class:
cakes = [
    Cake('Champagne', 'Vanilla and Champagne', 'Vanilla Buttercream', 'Creamy vanilla champagne cake with  pink curls shaved from rich white chocolate'),
    Cake('Black Forest', 'Chocolate and cherry', 'Chocolate', 'Chocolate cherry cake with decadent rich chocolate frosting and a cherry glaze'),
    Cake('Red Velvet', 'Chocolate', 'Cream cheese', 'Red velvet cake with mini chocolate chips, floating inside topped with a decadent cream cheese frosting')
]

# Create your views here.

def home(request):
    return HttpResponse('<h1>Cake Collector</h1>')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'cakes/index.html', { 'cakes': cakes })
