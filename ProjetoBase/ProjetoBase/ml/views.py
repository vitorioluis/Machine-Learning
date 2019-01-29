# -*- encoding:utf-8
import numpy as np
import pandas as pd
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# metricas de avaliação do modelo
from sklearn.metrics import confusion_matrix,accuracy_score


from .forms import IrisForm
from .models import Iris


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
    # print(lm.predict_proba(lst_predict))
    return predicao[0]


class LogisticIris(CreateView):
    __title = '| Regressão Logistica'
    template_name = 'new_edit.html'
    models = Iris
    form_class = IrisForm
    success_url = reverse_lazy('ml:logistica')

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
            context['predict'] = mod_regressao_logistica(lst)

        return render(request, self.template_name, context)


class ListaIris(View):
    template_name = 'dashboard.html'

    def get(self, request):
        iris = Iris.objects.select_related()
        return render(request, self.template_name, {'objects': iris})
