from django import forms

class ClienteLogIn(forms.Form):
    cc = forms.CharField(label='Cedula', max_length=100)

class Cliente_NEW(forms.Form):
    cc = forms.CharField(label='Cedula', max_length=100)
    nombre = forms.CharField(label='Nombre', max_length=100)