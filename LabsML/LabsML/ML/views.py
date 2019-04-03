# -*- encoding:utf-8
import pickle
from os import path

import numpy as np
import pandas as pd
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import train_test_split

from .forms import IrisForm, AcoesForm, FilmesForm
from .models import Iris, Acoes, Filmes


# metricas de avaliação do modelo


def cotacao_dolar():
    url = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia"
    url += "(dataCotacao=@dataCotacao)?@dataCotacao='{0}'&$top=100&$format=json".format(
        '02-15-2019')


def convert_list_to_dataframe(lst, lst_colunas):
    # converter a list com os dados para predição em dataframe
    return pd.DataFrame(np.array(lst).reshape(1, 4), columns=lst_colunas[:-1])


def mod_regressao_logistica(lst):
    """
    Machine Learning na pratica
    """
    nome_modelo = path.join(settings.MODELOS, "modelo_iris_regresao_logistica.mod")

    lst_colunas = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
    lst_predict = convert_list_to_dataframe(lst, lst_colunas)

    if path.isfile(nome_modelo):
        lm = pickle.load(open(nome_modelo, 'rb'))
    else:
        # Gera o modelo
        data = Iris.objects.all()
        df = pd.DataFrame.from_records(
            data.values('SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species')
        )

        x = df.drop('Species', axis=1)
        y = df.Species

        # treinando o modelo
        x_train, x_teste, y_train, y_teste = train_test_split(x, y, test_size=0.33)
        lm = LogisticRegression(solver="lbfgs", multi_class="multinomial")
        lm.fit(x_train, y_train)

        # salva para futuras predições
        pickle.dump(lm, open(nome_modelo, 'wb'))

    # realiza a predição
    predicao = lm.predict(lst_predict)
    prob = lm.predict_proba(lst_predict).round(2).max() * 100

    return [predicao[0], prob]


def mod_regressao_linear(lst):
    lst_colunas = ['open', 'max', 'min', 'volume', 'close']  # close
    lst_predict = convert_list_to_dataframe(lst, lst_colunas)
    nome_modelo = path.join(settings.MODELOS, "modelo_acoes_apple_regresao_linear.mod")

    if path.isfile(nome_modelo):
        lm = pickle.load(open(nome_modelo, 'rb'))
    else:
        # dados da base de dados
        data = Acoes.objects.all()
        df = pd.DataFrame.from_records(data.values('open', 'max', 'min', 'volume', 'close'))

        x = df.drop('close', axis=1)
        y = df.close

        x_train, x_teste, y_train, y_teste = train_test_split(x, y, test_size=0.33)

        lm = LinearRegression()
        lm.fit(x_train, y_train)

        pickle.dump(lm, open(nome_modelo, 'wb'))

    # predicao
    predicao = lm.predict(lst_predict)

    return 'Valor Predito: %.2f' % (predicao[0])


class LogisticIris(CreateView):
    __title = '| Regressão Logistica'
    template_name = 'form_new_edit.html'
    models = Iris
    form_class = IrisForm
    success_url = reverse_lazy('core:home')

    def get_context_data(self, **kwargs):
        context = super(LogisticIris, self).get_context_data(**kwargs)
        context['title'] = self.__title
        return context

    def post(self, request, *args, **kwargs):
        context = {'form': self.form_class(),
                   'title': self.__title,
                   'event': False}
        form = IrisForm(request.POST or None)
        if form.is_valid():
            lst = [float(str(n).replace(',', '.'))
                   for n in form.cleaned_data.values()]
            context['predict'], context['prob'] = mod_regressao_logistica(lst)

        return render(request, self.template_name, context)


class ListaIris(View):
    template_name = 'table.html'
    __title = ['Comprimento da Sépala', 'Largura da Sépala',
               'Comprimento da Petula', 'Largura da Petula', 'Espécie']

    def get(self, request):
        iris = Iris.objects.select_related().values('id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm',
                                                    'PetalWidthCm', 'Species')
        context = {'objects': iris, 'campos': self.__title}
        return render(request, self.template_name, context)


# regressão linear
class LinearAcoes(CreateView):
    __title = '| Regressão Linear'
    template_name = 'form_new_edit.html'
    models = Acoes
    form_class = AcoesForm
    success_url = reverse_lazy('core:home')

    def get_context_data(self, **kwargs):
        context = super(LinearAcoes, self).get_context_data(**kwargs)
        context['title'] = self.__title
        return context

    def post(self, request, *args, **kwargs):
        context = {'form': self.form_class(),
                   'title': self.__title}
        form = AcoesForm(request.POST or None)
        if form.is_valid():
            lst = [float(str(n).replace(',', '.'))
                   for n in form.cleaned_data.values()]
            context['predict'] = mod_regressao_linear(lst)

        return render(request, self.template_name, context)


class ListaAcoes(View):
    template_name = 'table.html'
    __title = ['data', 'open', 'max', 'min', 'close', 'adj_close', 'volume']

    def get(self, request):
        acoes = Acoes.objects.select_related().values('id', 'data', 'open', 'max', 'min', 'close', 'adj_close',
                                                      'volume')
        context = {'objects': acoes[:100], 'campos': self.__title}
        return render(request, self.template_name, context)


# sistema de recomendações de filme
class RecomendacaoFilme(CreateView):
    __title = '| Sistema de Recomendação'
    template_name = 'form_new_edit.html'
    models = Filmes
    form_class = FilmesForm
    success_url = reverse_lazy('core:home')

    def get_context_data(self, **kwargs):
        context = super(RecomendacaoFilme, self).get_context_data(**kwargs)
        context['title'] = self.__title
        return context


class ListaFilmes(View):
    template_name = 'table.html'
    __title = ['ano_lançamento', 'titulo_obra', 'genero',
               'data_lançamento', 'distribuidora', 'publico_acumulado']

    def get(self, request):
        filmes = Filmes.objects.select_related().values('id', 'ano_lançamento', 'titulo_obra', 'genero',
                                                        'data_lançamento', 'distribuidora', 'publico_acumulado')
        context = {'objects': filmes, 'campos': self.__title, 'event': True}
        return render(request, self.template_name, context)
