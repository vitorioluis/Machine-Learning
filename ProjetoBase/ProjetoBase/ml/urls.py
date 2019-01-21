# -*- coding: utf8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    # listar

    url(r'^listar/$', views.ListaIris.as_view(), name='listar_iris'),

    # url(r'^createiris/$', views.CreateIris.as_view(), name='create_iris'),
    #
    # # editar
    # url(r'^edit/(?P<pk>\d+)/$', views.EditClientes.as_view(), name='editar_clientes'),
    # url(r'^estabelecimentos/edit/(?P<pk>\d+)/$', views.EditEstabelecimentos.as_view(), name='editar_estabelecimentos'),
    #
    # # novo
    # url(r'^estabelecimentos/new/$', views.CreateEstabelecimentos.as_view(), name='new_estabelecimentos'),
    # url(r'^new/$', views.CreateClientes.as_view(), name='new_clientes'),
]
