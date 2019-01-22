# -*- coding: utf8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Iris


class IrisForm(forms.ModelForm):
    class Meta:
        model = Iris
        fields = ('SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm')


class RegisterIris3Form(UserCreationForm):
    def save(self, commit=True):
        iris = super(IrisForm, self).save(commit=False)
        if commit:
            iris.save()
        return iris
