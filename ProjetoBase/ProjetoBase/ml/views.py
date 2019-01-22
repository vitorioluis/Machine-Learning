# -*- encoding:utf-8
from django.urls import reverse_lazy
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from .models import Iris

from django.views import View
from django.views.generic import UpdateView, CreateView
from django.shortcuts import render
from .forms import IrisForm


# def mod_linear_multivariado(*args):
#     x = iris[['sepal_length', 'sepal_width', 'petal_length']]
#     y = iris['petal_width']
#     x_train, x_teste, y_train, y_teste = train_test_split(x, y, test_size=0.4, random_state=101)
#     lm = LinearRegression()
#     lm.fit(x_train, y_train)
#     predicao = lm.predict(x_teste)
#     return predicao

#
# def mod_regresao_logistica():
#     pass


class ListaIris(View):
    template_name = 'dashboard.html'

    def get(self, request):
        iris = Iris.objects.select_related()
        return render(request, self.template_name, {'objects': iris})


class LinearIris(CreateView):
    template_name = 'new_edit.html'
    models = Iris
    form_class = IrisForm
    success_url = reverse_lazy('ml:linear')

    def get_context_data(self, **kwargs):
        context = super(LinearIris, self).get_context_data(**kwargs)
        return context
