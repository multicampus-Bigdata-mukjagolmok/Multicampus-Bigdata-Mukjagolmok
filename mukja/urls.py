from django.urls import path
from . import views

# app_name = 'mukja'	# 이름 공간
urlpatterns = [
    path('', views.base, name = 'base'),
    path('index/', views.index, name='base'),
    path('golmok/<golmok_id>', views.golmok, name='golmok'),
]