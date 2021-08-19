from django import forms
from django.forms import fields
from .models import *

class agregar_musica_form (forms.ModelForm):
    class Meta:
        model = Musica
        fields = '__all__'
        exclude = ['artista',]