from django.shortcuts import render


# Create your pokemonApp here.
def getHome(request):
    return render(request, "pokemonApp/home.html")


def getWorld(request, id):
    context = {'id': id}
    return render(request, "pokemonApp/world.html", context)
