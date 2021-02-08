from django.shortcuts import render
from mukja.models import Golmok, Restaurant, Menu

# Create your views here.

def base(request):
    return render(request, 'base.html')

def golmok1(request):
    menu = Menu.objects.all()
    context = {"menu": menu}
    return render(request, 'golmok1.html', context)