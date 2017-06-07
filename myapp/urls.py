from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^kat/(?P<filtr>[0-9]+)/$', views.index, name='filtr'),

    url(r'^persons$', views.persons_list, name='persons_list'),
    url(r'^persons/(?P<zmienna_nr>[0-9]+)/$', views.persons_list, name='name_gowno'),

    url(r'^dodaj/(?P<pid>[0-9]+)/$', views.koszyk_dodaj, name='koszyk_dodaj'),
    url(r'^cart$', views.koszyk_view, name='koszyk'),
    url(r'^kasuj/(?P<poz_id>[0-9]+)/$', views.koszyk_kasuj, name='koszyk_kasuj'),
]
