from django.urls import path

from . import views

urlpatterns = [
    path('', views.getHome, name="home"),
    path('equipe', views.equipe, name="equipe"),
    path('world/<str:id>', views.getWorld, name="world")
]
