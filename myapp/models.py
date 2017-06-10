# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class Kategoria(models.Model):
    kat_id = models.AutoField(primary_key=True)
    kat_nazwa = models.CharField(max_length=25)

    def __str__(self):
        return self.kat_nazwa


@python_2_unicode_compatible
class Produkty(models.Model):
    produkt_id = models.AutoField(primary_key=True)
    kategoria = models.ForeignKey(Kategoria)
    nazwa = models.CharField(max_length=25)
    opis = models.TextField(max_length=120)
    obrazek = models.CharField(max_length=25, default="")
    cena = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    stan = models.IntegerField(default=0)

    def __str__(self):
        return self.nazwa


class Koszyk(models.Model):
    poz = models.AutoField(primary_key=True)
    produkt_id = models.ForeignKey(Produkty)
    ilosc = models.IntegerField(default=0)
