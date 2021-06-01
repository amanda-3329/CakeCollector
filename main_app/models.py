from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User

TASTED = (
    ('H', 'Homemade'),
    ('B', 'Bakery'),
    ('S', 'Storebought'),
    ('E', 'Elsewhere')
)

class Customization(models.Model):
    name = models.CharField(max_length=100)
    
#This code below names the object in the admin site:
    def __str__(self):
     return f'{self.name}'


# Create your models here.
class Cake(models.Model):
    name = models.CharField (max_length=100)
    flavor = models.CharField (max_length=100)
    icing_flavor = models.CharField (max_length=100)
    description = models.TextField (max_length=250)
#Sets up the many to many relationship between Cake and Customization:
    customizations = models.ManyToManyField(Customization, blank=True)
#Add the foreign key linking to a user instane
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name} | {self.flavor}'
 

class Tasting(models.Model):
    date = models.DateField('Tasting date')
    tasted = models.CharField(
        ('Cake Origin'),
        max_length=1,
        choices=TASTED,
        default=TASTED[0][0]
    )

    cake = models.ForeignKey (Cake, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.get_tasted_display()} on {self.date}'


class Photo(models.Model):
    url = models.CharField(max_length=200)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for cake_id: {self.cake_id} @ {self.url}"