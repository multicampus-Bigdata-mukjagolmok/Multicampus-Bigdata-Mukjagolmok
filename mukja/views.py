from django.shortcuts import render
from mukja.models import Golmok, Restaurant, Menu

# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def golmok(request, name):
    restaurants = Restaurant.objects.get(golmok = name)
    menulist = []
    for i in restaurants:
        menus = Menu.objects.get(restaurant = i.name)
        menulist.appennd(menus)
    context = { 'name': name, 'restaurants': restaurants, 'menulist': menulist }
    return render(request, 'golmok.html', context)