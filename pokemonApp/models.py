from django.db import models


class Inventaire(models.Model):
    item = models.CharField(max_length=40)
    qte = models.IntegerField(default=0)
    description = models.CharField(max_length=250)
    en_name = models.CharField(max_length=40)

    def __str__(self):
        return self.item


class Shop(models.Model):
    item = models.CharField(max_length=40)
    description = models.CharField(max_length=250)
    prix = models.IntegerField(default=0)
    url = models.CharField(max_length=250)
    en_name = models.CharField(max_length=40)

    def __str__(self):
        return self.item


class Money(models.Model):
    qte = models.IntegerField(default=0)

    def __str__(self):
        return str(self.qte)


class Equipe(models.Model):
    idPokemon = models.IntegerField(default=0)

    def __str__(self):
        return str(self.idPokemon)