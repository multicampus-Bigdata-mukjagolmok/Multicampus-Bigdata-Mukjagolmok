from django.urls import path
from . import views

# app_name = 'mukja'	# 이름 공간
urlpatterns = [
    path('', views.base, name = 'base'),
    path('golmok1/', views.golmok1, name='golmok1')
]