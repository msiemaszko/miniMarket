Pierwszy projekt DJANGO!
===================
Notatki własne podczas tworzenia pierwszej aplikacji django

----------

###0. Środowisko wirtualne

**a) Tworzenie wirtualnego środowiska**
```python -m virtualenv myenv```
**b) Aktywowanie środowiska:**
```.\myenv\Scripts\activate```
**c) Instalacja django**
```(myenv) pip install django```

###1. Tworzenie projektu

**a) tworzenie projektu, *project* :**
```django-admin startproject project .```

**b) tworzenie bazy danych dla projektu:**
```python manage.py migrate```

**c) uruchom projekt django:**
```
python manage.py runserver
testujemy na: http://127.0.0.1:8000/
```


###2. Tworzenie aplikacji myapp
**a) tworzenie aplikacji *myapp* :**
```python manage.py startapp myapp```

**b) tworzenie bazy danych dla projektu :**
Niektóre z aplikacji używają tabel, więc żebyśmy mogli ich używać musimy stworzyć bazę danych, poprzez komendę:
```python manage.py migrate```

**c) dołączenie konfiguracji URL myapp do project, *project/urls.py* :**
```
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('myapp.urls')),
]
# funkcja include() pozwala na odniesienia do innych URLconfów.
```

**e) konfiguracja URL aplikacji myapp, *myapp/urls.py* :**
*urls.py* zawiera listę powiązanych adresów URL z akcjami wywoływanymi w przypadku dopasowania URLa.
```
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	# Przyporządkowujemy widok (view) o nazwie index do adresu.
	url(r'^persons$', views.persons_list, name='url_osoby'),
]
```


**d) pierwsze widoki, *myapp/views.py* : **
```
from django.http import HttpResponse
from django.shortcuts import render

# widok domyślny - index
def index(request):
    return HttpResponse("Hello, world!!! Strona index.")

# widok -> templetes
def person_list(request):
    return render(request, 'myapp/persons_list.html', {})

```
Metoda *person_list*, która przyjmuje zapytanie (request) i zwraca metodę zwaną render, której zadaniem jest wyrenderowanie (złożenie w całość) naszego szablonu myapps/persons_list.html.


**f) włączenie modelu naszej aplikacji w *project/settings.py* :**
 Do INSTALLED_APPS dodajemy naszą aplikacje
```
INSTALLED_APPS = [
    [ ... ]
    # zawarcie aplikacji  w projekcie
    'myapp',
]
```
**g) konfiguracja modelu**
models.py* zawiera modele naszej aplikacji. Podstawa to struktura tabel. Każdy model to klasa opisująca strukturę tabeli w bazie danych.
```
from __future__ import unicode_literals
from django.db import models

class Tabela(models.Model):
    # definicja struktury tablicy
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)

    # funkcja prywatna klasy
    def __str__(self):
        return self.imie + " " + self.nazwisko
```

**h) migracja modeli do bazy danych:**
```
python manage.py makemigrations #  przygotowuje migracje
python manage.py migrate # tworzy tworzy tabele modeli w bazie
```

**i) testowanie bazy w shellu django: **
```
python manage.py shell
from myapp.models import Tabela
tt = Tabela(imie="Marek", nazwisko="Prezes")  # Tworzy obiekt - 'krotka'
tt.save()  # zapisuje obiekt do bazy

Tabela.objects.all() # zwróci wszystkie wiersze tabeli
Tabela.objects.filter(imie="Marek")  # filtrowanie wierszy
Tabela.objects.all().order_by('nazwisko')  # sortowanie
```

**j) tworzenie szablonu z danymi dynamicznymi :**

* stwórz zmodyfikuj widok persons_list o obiekt QuerySet:
```
from .models import Tabela

def persons_list(request):
    osoby = Tabela.objects.order_by('nazwisko')
    return render(request, 'myapp/persons_list.html', {'dane_post': osoby})
```
- stwórz strukturę katalogów ```myapp/templates/myapp```, a wewnątrz plik szablonu *persons_list.html* :
```
hello persons!
<table border="1px">
   <tr><th>#id</th><th>#imie</th><th>#nazwisko</th></tr>
   {% for dane in dane_post %}
       <tr>
         <td>{{ dane.id }}</td>
         <td>{{ dane.imie }}</td>
         <td>{{ dane.nazwisko }}</td>
      </tr>
   {% endfor %}
</table>
```

**h) Style CSS oraz Bootstrap w projekcie**

- stwórz strukturę katalogów  ```static/css/``` a w nim ```style.css```
- w pliku ```project/settings.py``` dodaj kod:
```
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
```
-  w szablonie HTML wprowadz informację o stylu CSS:
```
{% load staticfiles %}
[...]
<head>
	<!-- Dodawanie frameworka Bootstrap -->
	<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
	<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">

	<!-- nasz styl CSS -->
	<link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
[...]
```

**i) tworzenie szablonu bazowego**
Szablon bazowy umieszczamy w:  ```myapp\templates\myapp\base.html```
```
<body>
    <div class="page-header">
        <h1><a href="/">Pierwsza strona w Django</a></h1>
    </div>
    <div class="content container">
        <div class="row">
            {% block content %}
            {% endblock %}
        </div>
    </div>
</body>
```
teraz wystarczy, że w pliku szablonu ```persons_list.html``` umieścimy samo:
```
{% extends 'myapp/base.html' %}
	{% block content %}
	hello persons!
	<table border="1px">
		<tr><th>#id</th><th>#imie</th><th>#nazwisko</th></tr>
		{% for dane in dane_post %}
		    <tr>
		      <td>{{ dane.id }}</td>
		      <td>{{ dane.imie }}</td>
		      <td>{{ dane.nazwisko }}</td>
		   </tr>
		{% endfor %}
	</table>
{% endblock content %}
```

**j) tworzenie dynamicznych linków**
``<h1><a href="{% url 'podglad' pk=post.pk %}">{{ post.title }}</a></h1>``

**k) Jak włączyć panelu admina**

* stwórz super-użytkownika polecenim: ```python manage.py createsuperuser```
* w pliku ```project\urls.py``` dodaj:
```
from django.contrib import admin
[...]
    url(r'^admin/', admin.site.urls),
```
* w pliku ```myapp\admin.py``` wpisz:
```
from django.contrib import admin
from .models import Tabela	# zaimportuj swoj model
admin.site.register(Tabela)	# zarejestruj swoj model
```
* Panel dostępny pod adresem: http://localhost:8080/admin
