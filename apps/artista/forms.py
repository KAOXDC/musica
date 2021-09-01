from django import forms
from django.forms import fields, widgets
from django.contrib.auth.models import User
from .models import *

class agregar_musica_form (forms.ModelForm):
    class Meta:
        model = Musica
        fields = '__all__'
        exclude = ['artista',]
        labels = {
            'nombre':'NOMBRE',
            'archivo':'Archivo MP3',
        }
    def __init__(self, *args, **kwargs):
        super(agregar_musica_form, self).__init__(*args, **kwargs)
        for field in self.fields:	
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class agragar_user_form (forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = []

class login_form (forms.Form):
    usuario = forms.CharField(widget=forms.TextInput()) # input TEXT html
    clave   = forms.CharField(widget=forms.PasswordInput(render_value=False)) # input PASSWROD html

class register_form (forms.Form):
    username    = forms.EmailField(label='correo', widget= forms.TextInput(attrs={'class':'form-control'}))
    #email       = forms.EmailField(widget= forms.TextInput())
    password_1  = forms.CharField(label='password', widget= forms.PasswordInput(attrs={'class':'form-control'},render_value= False))
    password_2  = forms.CharField(label='repite el password', widget= forms.PasswordInput(attrs={'class':'form-control'}, render_value= False))

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            u = User.objects.get(username = username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('nombre de usuario ya registrado')

    def clean_email (self):
        email = self.cleaned_data['email']
        try:
            u = User.objects.get(email = email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError ('el correo ya exixte')
    
    def clean_password_2 (self):
        password_1 = self.cleaned_data['password_1']
        password_2 = self.cleaned_data['password_2']
        if password_1 == password_2:
            return password_2
        else:
            raise forms.ValidationError ('las claves no coinciden')




