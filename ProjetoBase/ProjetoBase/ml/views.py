# -*- encoding:utf-8
import pandas as pd
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from .forms import IrisForm
from .models import Iris


def mod_regressao_logistica(lst):
    nova_predicao = pd.DataFrame(lst,
                                 columns=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'])

    data = Iris.objects.all()
    df = pd.DataFrame.from_records(
        data.values('SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species')
    )
    x = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
    y = df['Species']

    x_train, x_teste, y_train, y_teste = train_test_split(x, y, test_size=100, random_state=101)
    lm = LogisticRegression()
    lm.fit(x_train, y_train)
    predicao = lm.predict(data)
    return predicao


class LogisticIris(CreateView):
    template_name = 'new_edit.html'
    models = Iris
    form_class = IrisForm
    success_url = reverse_lazy('ml:logistica')

    def get_context_data(self, **kwargs):
        context = super(LogisticIris, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form = IrisForm(request.POST or None)
        if form.is_valid():
            lst = [float(str(n).replace(',', '.')) for n in form.cleaned_data.values()]
            mod_regressao_logistica(lst)
            print(lst)


class ListaIris(View):
    template_name = 'dashboard.html'

    def get(self, request):
        iris = Iris.objects.select_related()
        return render(request, self.template_name, {'objects': iris})
