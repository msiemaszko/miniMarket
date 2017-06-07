# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Produkty, Kategoria

# Register your models here.
# admin.site.register(Tabela)
admin.site.register(Produkty)
admin.site.register(Kategoria)
