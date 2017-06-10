from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^r/(?P<result>([a-z]+))^$', views.index, name='index'),  # z result ok
    url(r'^(?P<result>([a-z]+))/$', views.index, name='index'),
    url(r'^kat/(?P<filtr>([0-9]+))/$', views.index, name='filtr'),
    url(r'^kat/(?P<filtr>([0-9]+))/(?P<result>([a-z]+))/$', views.index, name='filtr'),  # z result ok

    url(r'^cart$', views.koszyk_view, name='koszyk'),
    url(r'^dodaj/(?P<poz_id>[0-9]+)/$', views.koszyk_dodaj, name='koszyk_dodaj'),
    url(r'^kasuj/(?P<poz_id>[0-9]+)/$', views.koszyk_kasuj, name='koszyk_kasuj'),
]
# url(r'^kat/(?P<filtr>[0-9]+)/(?P<result>[a-z]+)/$', views.index, name='filtr'),
# url(r'^persons$', views.persons_list, name='persons_list'),
