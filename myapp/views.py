# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Produkty, Koszyk, Kategoria
from .forms import PostForm
from django.shortcuts import redirect


# widok domyślny - index
def index(request, filtr=None, result=None):

    koszyk_list = Koszyk.objects.all()
    kategorie_list = Kategoria.objects.all()
    if filtr:
        produkty_list = Produkty.objects.filter(kategoria=filtr).order_by('nazwa')
    else:
        produkty_list = Produkty.objects.all().order_by('nazwa')

    return render(request, 'myapp/produkty.html', {
        'post_produkty': produkty_list,
        'post_koszyk': koszyk_list,
        'post_kategorie': kategorie_list,
        'result': result,
    })


def koszyk_view(request):

    produkty_list = Produkty.objects.order_by('nazwa')
    koszyk_list = Koszyk.objects.all()
    kategorie_list = Kategoria.objects.all()

    # Wyliczenie ceny: cena * iosc
    suma = 0
    for tmpObj in koszyk_list:
        tmpObj.produkt_id.cena = tmpObj.produkt_id.cena * tmpObj.ilosc
        suma += tmpObj.produkt_id.cena

    form = PostForm()

    return render(request, 'myapp/koszyk.html', {
        'post_produkty': produkty_list,
        'post_koszyk': koszyk_list,
        'post_kategorie': kategorie_list,
        'form': form,
        'suma': suma,
    })


def koszyk_dodaj(request, poz_id):

    produkt_obj = get_object_or_404(Produkty, produkt_id=poz_id)

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

    referer = request.META.get('HTTP_REFERER').split("/")  # Podzielone HTTP Refferer

    if referer[3] == "kat":
        return redirect('filtr', filtr=referer[4], result="ok")
    else:
        return redirect('index', result="ok")


def koszyk_kasuj(request, poz_id):
    pozycja = get_object_or_404(Koszyk, poz=poz_id)
    pozycja.delete()
    return redirect('koszyk')
