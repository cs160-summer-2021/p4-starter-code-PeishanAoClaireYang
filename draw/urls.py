# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('home', views.home, name='home'),
    path('search1', views.search1, name='search1'),
    path('search2', views.search2, name='search2'),
    path('info', views.info, name='info'),
]
