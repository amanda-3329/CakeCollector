from django.db import models

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

    cake = models.ForeignKey (Cake, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_tasted_display()} on {self.date}'