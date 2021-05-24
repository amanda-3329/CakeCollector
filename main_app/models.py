from django.db import models

# Create your models here.
class Cake(models.Model):
    name = models.CharField (max_length=100)
    flavor = models.CharField (max_length=100)
    icing_flavor = models.CharField (max_length=100)
    description = models.TextField (max_length=250)
    