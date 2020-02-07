from django.urls import path
from . import views

urlpatterns = [
    path('', views.getHome, name="home"),
    path('equipe', views.getEquipe, name="equipe"),
    path('pokedex', views.getPokedex, name="pokedex"),
    path('infoPokemon/<str:name>', views.getPokemonByName, name="infoPokemon"),
    path('inventory', views.getInventory, name="inventory"),
    path('world/<str:id>', views.getWorld, name="world"),
    path('explore/<str:id>', views.getExplore, name="explore"),
    path('shop', views.getShop, name="shop"),
    path('buyItemInShop/<str:item>/<str:prix>', views.buyItemInShop, name="buyItemInShop"),
    path('shop', views.getShop, name="shop"),
    path('fight/<str:id>', views.getFight, name="fight"),
    path('addPokemon/<str:id>', views.addToPlayerPokemonList, name="addPokemon"),
]
