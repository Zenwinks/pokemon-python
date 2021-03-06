"""pokemonPython URL Configuration

The `urlpatterns` list routes URLs to pokemonApp. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function pokemonApp
    1. Add an import:  from my_app import pokemonApp
    2. Add a URL to urlpatterns:  path('', pokemonApp.home, name='home')
Class-based pokemonApp
    1. Add an import:  from other_app.pokemonApp import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokemon/', include('pokemonApp.urls'))
]
