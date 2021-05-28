from django.contrib import admin
from .models import Cake,Tasting, Customization, Photo


# Register your models here.
from .models import Cake

admin.site.register(Cake)
admin.site.register(Tasting)
admin.site.register(Customization)
admin.site.register(Photo)
