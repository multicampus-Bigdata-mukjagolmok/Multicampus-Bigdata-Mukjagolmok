from django.shortcuts import render
from mukja.models import Golmok, Restaurant, Menu, Comment


# Create your views here.

def index(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def golmok(request, pk):
    golmok_pk = pk
    mukjagolmok = Golmok.objects.get(id=pk)
    restaurants = Restaurant.objects.filter(golmok_id=golmok_pk)
    context = {
        'mukjagolmok': mukjagolmok,
        'restaurants': restaurants,
    }
    return render(request, "golmok.html", context)


def restaurant(request, fk, pk):
    golmok_pk = fk
    restaurant_pk = pk
    restaurant = Restaurant.objects.get(id=restaurant_pk)
    menus = Menu.objects.filter(restaurant_id=restaurant_pk)
    if request.method == 'POST' :
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        makecomment = Comment(name=name, comment=comment, restaurant_id=restaurant_pk)
        makecomment.save()
    comments = Comment.objects.filter(restaurant_id=restaurant_pk)
    context = {
        'golmok_id': golmok_pk,
        'restaurant': restaurant,
        'menus': menus,
        'comments': comments,
    }
    return render(request, "restaurant.html", context)
