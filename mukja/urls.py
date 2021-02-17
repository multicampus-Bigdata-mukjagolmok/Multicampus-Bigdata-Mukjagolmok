from django.urls import path
from . import views

# app_name = 'mukja'	# 이름 공간
urlpatterns = [
    path('', views.index),
    path('index/', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('golmok/<int:pk>/', views.golmok, name='golmok'),
    # path('golmok/<int:pk>/new_comment/', views.new_comment),
    path('golmok/<int:fk>/<int:pk>/', views.restaurant),
    path('golmok/<int:fk>/<int:pk>/new_comment/', views.new_comment),
    path('delete_comment/<int:pk>/', views.delete_comment),
    path('edit_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('restaurant/', views.restaurant),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]