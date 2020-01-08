from django.urls import path

from . import views

urlpatterns = [
    path('', views.getHome, name="home"),
    path('world/<str:id>', views.getWorld, name="world")
]
