from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Golmok(models.Model):
    name = models.CharField(max_length=25, unique=True)
    address = models.CharField(max_length=50)
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=25, unique=True)
    address = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    description = models.CharField(max_length=500, null=True)
    rating = models.CharField(max_length=10)
    golmok = models.ForeignKey(Golmok, blank=True, null=True, on_delete=models.SET_NULL)
    images = models.CharField(max_length=50, null=True)

    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)
    created = models.DateTimeField(auto_now_add=True)  # 포스트가 생성이 될 때 created에 자동으로 담아주게 된다.
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/mukja/golmok/{}/{}/'.format(self.golmok.pk, self.pk)

class Menu(models.Model):
    name = models.CharField(max_length=25)
    price = models.CharField(max_length=10)
    description = models.CharField(max_length=300, null=True)
    restaurant = models.ForeignKey(Restaurant, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
