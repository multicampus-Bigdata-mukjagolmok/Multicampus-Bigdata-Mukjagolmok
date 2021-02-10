from django.shortcuts import render
from mukja.models import Golmok, Restaurant, Menu

# Create your views here.

def index(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def golmok(request, pk):
    golmok_pk = pk
    mukjagolmok = Golmok.objects.get(id = pk)
    restaurants = Restaurant.objects.filter(golmok_id= golmok_pk)
    context = {
        'mukjagolmok' : mukjagolmok,
        'restaurants' : restaurants,
               }
    return render(request, "golmok.html", context)

def restaurant(request, fk, pk):
    golmok_pk = fk
    restaurant_pk = pk
    restaurant = Restaurant.objects.get(id = restaurant_pk)
    menus = Menu.objects.filter(restaurant_id = restaurant_pk)
    context = {
        'restaurant' : restaurant,
        'menus' : menus,
    }
    return render(request, "restaurant.html", context)