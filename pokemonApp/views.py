from django.shortcuts import render
from pokemonApp.models import Inventaire, Shop, Money, Equipe
import requests
import random

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


def getInventory(request):
    inventaire = Inventaire.objects.filter(qte__gt=0)
    money = Money.objects.all()
    context = {'inventaire': inventaire, 'money': money}
    return render(request, "pokemonApp/inventory.html", context)


def getWorld(request, id):
    idMonde = str(id)
    context = {'idMonde': idMonde}
    return render(request, "pokemonApp/world.html", context)

def getFight(request, id):
    random_id = ''
    if id == '1':
        random_id = str(random.randint(1, 151))
    elif id == '2':
        random_id = str(random.randint(152, 251))
    elif id == '3':
        random_id = str(random.randint(252, 386))
    elif id == '4':
        random_id = str(random.randint(387, 493))
    elif id == '5':
        random_id = str(random.randint(494, 649))
    elif id == '6':
        random_id = str(random.randint(650, 721))
    pokemon = requests.get(GET_POKEMON + random_id).json()

    idPokemons = Equipe.objects.all()
    equipe= []
    for i in range(len(idPokemons)):
        equipe.append(requests.get(GET_POKEMON + str(idPokemons[i])).json())

    movesteam = []
    for pokeMove in equipe[0]["moves"]:
        t = requests.get(pokeMove["move"]["url"])
        movesteam.append(t.json())
        if (len(movesteam) > 3):
            break;

    moves = []
    for pokeMove in pokemon["moves"]:
        t = requests.get(pokeMove["move"]["url"])
        moves.append(t.json())
        if(len(moves)>3):
            break;
    context = {'idMonde': id, 'random_id': random_id, 'pokemon': pokemon, 'moves': moves, 'equipe': equipe, 'movesTeam': movesteam}
    return render(request, "pokemonApp/fight.html", context)

def getExplore(request, id):
    random_id = ''
    if id == '1':
        random_id = str(random.randint(1, 151))
    elif id == '2':
        random_id = str(random.randint(152, 251))
    elif id == '3':
        random_id = str(random.randint(252, 386))
    elif id == '4':
        random_id = str(random.randint(387, 493))
    elif id == '5':
        random_id = str(random.randint(494, 649))
    elif id == '6':
        random_id = str(random.randint(650, 721))

    pokemon = requests.get(GET_POKEMON + random_id).json()

    types = []
    for pokeType in pokemon["types"]:
        t = requests.get(pokeType["type"]["url"])
        types.append(t.json())

    base_xp = pokemon["base_experience"]
    taux_capture = 0
    if base_xp <= 100:
        taux_capture = 70
    elif 100 < base_xp <= 200:
        taux_capture = 45
    elif 200 < base_xp <= 300:
        taux_capture = 15
    elif base_xp > 300:
        taux_capture = 5

    for inventaire in Inventaire.objects.filter(item="pokeball"):
        qte_pokeball = inventaire.qte
    for inventaire in Inventaire.objects.filter(item="superball"):
        qte_superball = inventaire.qte
    for inventaire in Inventaire.objects.filter(item="hyperball"):
        qte_hyperball = inventaire.qte
    for inventaire in Inventaire.objects.filter(item="masterball"):
        qte_masterball = inventaire.qte

    context = {'idMonde': id, 'random_id': random_id, 'pokemon': pokemon, 'types': types, 'base_xp': base_xp,
               'taux_capture': taux_capture, 'qte_pokeball': qte_pokeball, 'qte_superball': qte_superball,
               'qte_hyperball': qte_hyperball, 'qte_masterball': qte_masterball}
    return render(request, "pokemonApp/explore.html", context)


def getShop(request):
    money = Money.objects.get()
    shop = Shop.objects.all()
    context = {'items': shop, 'money': money}
    return render(request, "pokemonApp/shop.html", context)


def buyItemInShop(request, item, prix):
    money = Money.objects.get()
    money.qte = str(int(money.qte) - int(prix))
    money.save()
    inventaire = Inventaire.objects.get(item=item.lower())
    inventaire.qte = str(int(inventaire.qte) + 1)
    inventaire.save()
    return getShop(request)


def addToTeam(request, id):
    Equipe.objects.create(idPokemon=id)
    pokemon = requests.get(GET_POKEMON + id).json()
    context = {'idPokemon': id, 'pokemon': pokemon}
    return render(request, "pokemonApp/catchedPokemon.html", context)

