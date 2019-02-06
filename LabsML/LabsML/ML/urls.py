# -*- coding: utf8 -*-

from django.conf.urls import url

from .views import ListaIris, LogisticIris, ListaAcoes

urlpatterns = [
    # listar

    url(r'^$', ListaIris.as_view(), name='listar_iris'),
    url(r'^lista/$', ListaAcoes.as_view(), name='lista_acoes'),
    url(r'^logistica/$', LogisticIris.as_view(), name='logistica'),

    #
    # # editar
    # url(r'^edit/(?P<pk>\d+)/$', views.EditClientes.as_view(), name='editar_clientes'),
    # url(r'^estabelecimentos/edit/(?P<pk>\d+)/$', views.EditEstabelecimentos.as_view(), name='editar_estabelecimentos'),
    #
    # # novo
    # url(r'^estabelecimentos/new/$', views.CreateEstabelecimentos.as_view(), name='new_estabelecimentos'),
    # url(r'^new/$', views.CreateClientes.as_view(), name='new_clientes'),
]
