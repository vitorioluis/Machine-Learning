# -*- encoding:utf-8
import numpy as np
import pandas as pd
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from .forms import IrisForm
from .models import Iris, tb_ml_acoes


# metricas de avaliação do modelo


def cotacao_dolar():
    url = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia"
    url += "(dataCotacao=@dataCotacao)?@dataCotacao='{0}'&$top=100&$format=json".format('02-15-2019')


def mod_regressao_logistica(lst):
    """
    Machine Learning na pratica
    """
    lst_colunas = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
    # converter a list com os dados para predição em dataframe
    lst_predict = pd.DataFrame(np.array(lst).reshape(1, 4), columns=lst_colunas[:-1])

    # dados de iris obtido da base de dados
    data = Iris.objects.all()
    df = pd.DataFrame.from_records(
        data.values('SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species')
    )

    x = df.drop('Species', axis=1)
    y = df.Species

    # treinando o modelo
    x_train, x_teste, y_train, y_teste = train_test_split(x, y, test_size=0.7, random_state=101)
    lm = LogisticRegression(solver="lbfgs", multi_class="multinomial")
    lm.fit(x_train, y_train)

    # predicao
    predicao = lm.predict(lst_predict)
    prob = lm.predict_proba(lst_predict).round(2).max() * 100
    return [predicao[0], prob]


class LogisticIris(CreateView):
    __title = '| Regressão Logistica'
    template_name = 'new_edit.html'
    models = Iris
    form_class = IrisForm
    success_url = reverse_lazy('MachineLearning:logistica')

    def get_context_data(self, **kwargs):
        context = super(LogisticIris, self).get_context_data(**kwargs)
        context['title'] = self.__title
        return context

    def post(self, request, *args, **kwargs):
        context = {'form': self.form_class(),
                   'title': self.__title}
        form = IrisForm(request.POST or None)
        if form.is_valid():
            lst = [float(str(n).replace(',', '.')) for n in form.cleaned_data.values()]
            context['predict'], context['prob'] = mod_regressao_logistica(lst)

        return render(request, self.template_name, context)


class ListaIris(View):
    template_name = 'table.html'
    titulo = ['Comprimento da Sépala', 'Largura da Sépala', 'Comprimento da Petula', 'Largura da Petula', 'Espécie']

    def get(self, request):
        iris = Iris.objects.select_related()
        context = {'objects': iris, 'campos': self.titulo}
        return render(request, self.template_name, context)


## regressão linear
class ListaAcoes(View):
    template_name = 'table.html'
    titulo = ['Ano lançamento', 'Título da obra', 'Gênero', 'País produtor da obra', 'Nacionalidade da obra',
              'Data lançamento', 'Distribuidora', 'Salas lançamento', 'Máximo salas ocupadas', 'Público acumulado',
              'Renda acumulada']

    def get(self, request):
        acoes = tb_ml_acoes.objects.select_related()
        context = {'objects': acoes, 'campos': self.titulo}

        return render(request, self.template_name, context)
