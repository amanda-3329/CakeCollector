from django.contrib import admin
from .models import Cake,Tasting, Customization


# Register your models here.
from .models import Cake

admin.site.register(Cake)
admin.site.register(Tasting)
admin.site.register(Customization)
