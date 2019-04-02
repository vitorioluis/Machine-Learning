# -*- coding: utf8 -*-

from django.conf.urls import url

from .views import ListaIris, LogisticIris, ListaAcoes, LinearAcoes, ListaFilmes, RecomendacaoFilme

urlpatterns = [

    # regressão logistica
    url(r'^listar_iris$', ListaIris.as_view(), name='listar_iris'),
    url(r'^logistica/$', LogisticIris.as_view(), name='logistica'),

    # regressão Linear
    url(r'^lista_acoes/$', ListaAcoes.as_view(), name='lista_acoes'),
    url(r'^linear/$', LinearAcoes.as_view(), name='linear'),

    # Sistema de recomendação
    url(r'^lista_filmes/$', ListaFilmes.as_view(), name='lista_filmes'),
    url(r'^recomendacao/$', RecomendacaoFilme.as_view(), name='recomendacao'),

]
