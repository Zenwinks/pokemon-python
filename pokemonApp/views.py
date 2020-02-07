from django.shortcuts import render
from pokemonApp.models import Inventaire, Shop, Money, Equipe, PokemonJoueur
import requests
import random

GET_POKEMON = 'https://pokeapi.co/api/v2/pokemon/'


def getHome(request):
    return render(request, "pokemonApp/home.html")


def getPokedex(request):
    pokemonList = requests.get(GET_POKEMON + "?limit=1000000")
    context = {'pokemonList': pokemonList.json()}
    for i in range(len(context['pokemonList']['results'])):
        id = context['pokemonList']['results'][i]['url'].split("/")
        context['pokemonList']['results'][i]['id'] = id[-2]
    return render(request, "pokemonApp/pokedex.html", context)


def getPokemonByName(request, name):
    p = requests.get(GET_POKEMON + name)
    pokemon = p.json()
    pokemon["height"] = int(pokemon["height"] / 0.032808)
    abilities = []
    for ability in pokemon["abilities"]:
        a = requests.get(ability['ability']['url'])
        abilities.append(a.json())
    types = []
    for pokeType in pokemon["types"]:
        t = requests.get(pokeType["type"]["url"])
        types.append(t.json())
    context = {'pokemon': pokemon, 'abilities': abilities, 'types': types}
    return render(request, "pokemonApp/infoPokemon.html", context)


def getEquipe(request):
    results = []
    pokemonId = []
    idPokemon = Equipe.objects.all()
    i = 0
    while i < 6:
        try:
            pokemonList = requests.get(GET_POKEMON + '/' + str(idPokemon[i]))
            results.append(pokemonList.json())
            pokemonId.append(idPokemon[i])
        except:
            results.append({''})
        i = i + 1

    context = {'pokemonList': results, 'pokemonId': pokemonId}

    return render(request, "pokemonApp/equipe.html", context)


def getPlayerPokemonList(request):
    results = []
    idPokemons = PokemonJoueur.objects.all()
    for i in range(len(idPokemons)):
        results.append(requests.get(GET_POKEMON + str(idPokemons[i])).json())

    context = {'pokemonList': results}

    return render(request, "pokemonApp/playerPokemonList.html", context)


def getChangeEquipe(request, idOldPokemon):
    results = []
    idPokemons = PokemonJoueur.objects.all()
    for i in range(len(idPokemons)):
        results.append(requests.get(GET_POKEMON + str(idPokemons[i])).json())

    context = {'pokemonList': results, 'idOldPokemon': idOldPokemon}

    return render(request, "pokemonApp/changeEquipe.html", context)


def modifEquipe(request, idOldPokemon, idNewPokemon):
    pokemon = Equipe.objects.get(idPokemon=idOldPokemon)
    pokemon.idPokemon = idNewPokemon
    pokemon.save()
    return getEquipe(request)


def getInventory(request):
    inventaire = Inventaire.objects.filter(qte__gt=0)
    money = Money.objects.get()
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
    equipe = []
    for i in range(len(idPokemons)):
        equipe.append(requests.get(GET_POKEMON + str(idPokemons[i])).json())

    movesteam = []
    for pokeMove in equipe[0]["moves"]:
        t = requests.get(pokeMove["move"]["url"])
        print(pokeMove["move"]["url"])
        movesteam.append(t.json())
        if (len(movesteam) > 3):
            break;

    moves = []
    for pokeMove in pokemon["moves"]:
        t = requests.get(pokeMove["move"]["url"])
        moves.append(t.json())
        if (len(moves) > 3):
            break;

    money = Money.objects.get()

    context = {'idMonde': id, 'random_id': random_id, 'pokemon': pokemon, 'moves': moves, 'equipe': equipe,
               'movesTeam': movesteam, 'money': money}
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


def addToPlayerPokemonList(request, id):
    PokemonJoueur.objects.create(idPokemon=id)
    pokemon = requests.get(GET_POKEMON + id).json()
    context = {'idPokemon': id, 'pokemon': pokemon}
    return render(request, "pokemonApp/catchedPokemon.html", context)


def fightWon(request, loot):
    money = Money.objects.get()
    money.qte = str(int(money.qte) + int(loot))
    money.save()

def fightLose(request, lost):
    money = Money.objects.get()
    money.qte = str(int(money.qte) - int(lost))
    money.save()
