from django.urls import path
from . import views

urlpatterns = [
    path('', views.getHome, name="home"),
    path('equipe', views.equipe, name="equipe"),
    path('inventory', views.getInventory, name="inventory"),
    path('world/<str:id>', views.getWorld, name="world"),
    path('explore/<str:id>', views.getExplore, name="explore"),
    path('addPokemon/<str:id>', views.addToTeam, name="addPokemon"),
    path('shop', views.getShop, name="shop")
]
