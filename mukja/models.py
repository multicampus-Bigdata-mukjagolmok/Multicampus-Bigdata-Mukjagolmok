from django.db import models

# Create your models here.

class Golmok(models.Model):
    name = models.CharField(max_length=25, unique=True)
    address = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=25, unique=True)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    rating = models.CharField(max_length=10)
    golmok = models.ForeignKey(Golmok, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=25, unique=True)
    price = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=300, unique=True)
    restaurant = models.ForeignKey(Restaurant, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
