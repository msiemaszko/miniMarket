# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Tabela(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)

    def __str__(self):
        return self.imie + " " + self.nazwisko

class Kategoria(models.Model):
    kat_id = models.AutoField(primary_key=True)
    kat_nazwa = models.CharField(max_length=25)

    def __str__(self):
        return self.kat_nazwa
 

class Produkty(models.Model):
    produkt_id = models.AutoField(primary_key=True)
    kategoria = models.ForeignKey(Kategoria)
    nazwa = models.CharField(max_length=25)
    opis = models.TextField(max_length=120)
    obrazek = models.CharField(max_length=25, default="")
    cena = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    stan = models.IntegerField(default=0)

    def __str__(self):
        return self.nazwa


class Koszyk(models.Model):
    poz = models.AutoField(primary_key=True)
    # produkt_id = models.IntegerField()
    produkt_id = models.ForeignKey(Produkty)
    ilosc = models.IntegerField(default=0)


    # def ilosc(self):
        # return self.ilosc


# produkt = models.ForeignKey(Produkty, on_delete=models.CASCADE)
    # produkt_id = models.AutoField(primary_key=True)

    # def __str__(self):
        # return self.nazwa
        # return self.ilosc
    #
    # def ilosc(self):
    #     return self.ilosc

# def dodaj_do_koszyka(procuct_id):
