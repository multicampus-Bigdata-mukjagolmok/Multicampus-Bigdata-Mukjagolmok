from django.urls import path
from . import views

# app_name = 'mukja'	# 이름 공간
urlpatterns = [
    path('', views.index),
    path('index/', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('golmok/<int:pk>/', views.golmok, name='golmok'),
    path('golmok/<int:fk>/<int:pk>/', views.restaurant),
    # path('restaurant/', views.restaurant),
]