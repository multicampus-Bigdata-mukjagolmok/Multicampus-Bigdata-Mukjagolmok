from django.shortcuts import render
from mukja.models import Golmok, Restaurant, Menu

# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def golmok(request, golmokname):
    golmok = Golmok.objects.get(name = golmokname)
    id = golmok.id
    restaurants = Restaurant.objects.filter(golmok_id = id)
    menulist = []
    for i in restaurants:
        restaurant_id = i.id
        menus = Menu.objects.filter(restaurant_id = restaurant_id)
        menulist.append(menus)
    first = menulist[0]
    second = menulist[1]
    third = menulist[2]
    forth = menulist[3]
    firstname = restaurants[0].name
    secondname = restaurants[1].name
    thirdname = restaurants[2].name
    forthname = restaurants[3].name
    fifth, fifthname = [], []
    if len(restaurants)>4:
        fifth = menulist[4]
        fifthname = restaurants[4].name
    context = { 'golmok': golmok, 'restaurants': restaurants, 'first': first, 'second': second, 'third': third, 'forth': forth, 'fifth': fifth, 'firstname': firstname, 'secondname': secondname, 'thirdname': thirdname, 'forthname': forthname, 'fifthname': fifthname }
    return render(request, 'golmok.html', context)