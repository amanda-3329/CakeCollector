from django import forms
from .models import Cake

class CakeForm (forms.ModelForm):
    class Meta:
        model = Cake
        fields = ('name', 'flavor', 'icing_flavor', 'description')