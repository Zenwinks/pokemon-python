from django.shortcuts import render
import requests


GET_POKEMON = 'https://pokeapi.co/api/v2/pokemon/'


def getHome(request):
    return render(request, "pokemonApp/home.html")


def equipe(request):
    # TODO remplacer l'appel des pokemons par ceux de l'équipe
    pokemonList = requests.get(GET_POKEMON + "?limit=6")
    context = {'pokemonList': pokemonList.json()}
    for i in range(len(context['pokemonList']['results'])):
        id = context['pokemonList']['results'][i]['url'].split("/")
        context['pokemonList']['results'][i]['id'] = id[-2]

    # TODO le clique sur le bouton "changer un membre de l'équipe" doit permettre de selectionner un des pokémons de l'équipe
    # TODO lors de la selection du pokémon, envoi sur la page des pokémons capturés où l'utilisateur doit sélectionner le pokémon qu'il veut ajouter
    # UPDATE equipe WHERE id_pokemon = $id_pokemon_ancien SET id_pokemon = $id_pokemon_nouveau

    return render(request, "pokemonApp/equipe.html", context)


def getWorld(request, id):
    context = {'id': id}
    return render(request, "pokemonApp/world.html", context)
