from django import forms
from .models import Cake, Tasting

class CakeForm (forms.ModelForm):
    class Meta:
        model = Cake
        fields = ('name', 'flavor', 'icing_flavor', 'description')

class TastingForm(forms.ModelForm):
    class Meta:
        model = Tasting
        fields = ('date', 'tasted')
        #Amanda add other fields once you know this works