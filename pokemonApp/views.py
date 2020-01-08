from django.shortcuts import render


# Create your pokemonApp here.
def getHome(request):
    return render(request, "pokemonApp/home.html")
