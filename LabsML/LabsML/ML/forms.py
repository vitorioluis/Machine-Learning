# -*- coding: utf8 -*-
from django import forms

from .models import Iris, Acoes, Filmes


# from django.contrib.auth.forms import UserCreationForm


class IrisForm(forms.ModelForm):
    class Meta:
        model = Iris
        fields = ('SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm')


class AcoesForm(forms.ModelForm):
    class Meta:
        model = Acoes
        fields = ('open', 'max', 'min', 'volume')


class FilmesForm(forms.ModelForm):
    class Meta:
        model = Filmes
        fields = ('ano_lançamento', 'titulo_obra', 'genero', 'data_lançamento', 'distribuidora', 'publico_acumulado')

