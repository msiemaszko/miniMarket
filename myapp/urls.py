from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^result:(?P<result>([a-z]+))$', views.index, name='index'),  # index z parametrem OK
    # url(r'^(?Pok)/$', views.index, name='index'),  # index z parametrem OK

    url(r'^kat/(?P<filtr>([0-9]+))/$', views.index, name='filtr'),
    url(r'^kat/(?P<filtr>([0-9]+))/result:(?P<result>([a-z]+))$', views.index, name='filtr'),  # z result par. ok

    url(r'^koszyk$', views.koszyk_view, name='koszyk'),
    url(r'^dodaj/(?P<poz_id>[0-9]+)/$', views.koszyk_dodaj, name='koszyk_dodaj'),
    url(r'^kasuj/(?P<poz_id>[0-9]+)/$', views.koszyk_kasuj, name='koszyk_kasuj'),
]
