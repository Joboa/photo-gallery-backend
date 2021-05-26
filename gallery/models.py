from django.db import models


class Image(models.Model):

    CHOICES = (('Flower', 'flower'),
               ('Engine', 'engine'),
               ('Road', 'road'),
               ('Calculus', 'calculus'),
               ('Aero', 'aero'),
               ('Bearing', 'bearing'),
               ('Gear', 'gears'),
               ('Dish', 'dish'),
               ('Python image', 'python'),
               ('Shaft', 'shaft'),)

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/', blank=True)
    
    category = models.CharField(max_length=50, choices=CHOICES, default='')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
