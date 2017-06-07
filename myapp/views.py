# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Tabela, Produkty, Koszyk, Kategoria
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from itertools import chain
from operator import attrgetter


# widok domyślny - index
# def index(request):
# return HttpResponse("Hello, world !!! . Strona index.")

def index(request, filtr=None):
    # return HttpResponse("Hello, world !!! . Strona index.")
    produkty_list = Produkty.objects.filter(kategoria=filtr)
    # .order_by('nazwa')
    koszyk_list = Koszyk.objects.all()
    kategorie_list = Kategoria.objects.all()

    return render(request, 'myapp/sklep_produkty.html', {
        'post_produkty': produkty_list,
        'post_koszyk': koszyk_list,
        'post_kategorie': kategorie_list,
        'error_message': "You didn't select a choice."
    })

# widok -> templetes
def persons_list(request, zmienna_nr=None):
    osoby = Tabela.objects.order_by('nazwisko')

    return render(request, 'myapp/persons_list.html', {'dane_post': osoby, 'zmienna_nr': zmienna_nr})


def koszyk_dodaj(request, pid):

    produkt_obj = get_object_or_404(Produkty, produkt_id=pid)

    try:
        # sprobuj pobrac produkt z koszyka
        koszyk_obj = get_object_or_404(Koszyk, produkt_id=produkt_obj)
    except:
        # dodanie
        k_new = Koszyk()
        k_new.produkt_id = produkt_obj
        k_new.ilosc = 1
        k_new.save()

    else:
        # zwiekszenie
        koszyk_obj.ilosc += 1
        koszyk_obj.save()

    return redirect('index')

def koszyk_view(request):

    produkty_list = Produkty.objects.order_by('nazwa')
    koszyk_list = Koszyk.objects.all()
    kategorie_list = Kategoria.objects.all()

    # Wyliczenie ceny: cena * iosc
    for tmpObj in koszyk_list:
        tmpObj.produkt_id.cena = tmpObj.produkt_id.cena * tmpObj.ilosc

    return render(request, 'myapp/cart_view.html', {
        'post_produkty': produkty_list,
        'post_koszyk': koszyk_list,
        'post_kategorie': kategorie_list,
    })


def koszyk_kasuj(request, poz_id):
    pozycja = get_object_or_404(Koszyk, poz=poz_id)
    pozycja.delete()
    return redirect('koszyk')


# def person_detail(request, w):
#     post = get_object_or_404(Tabela, pk=w)
#     return render(request, 'myapp/post_detail.html', {'post': post})
