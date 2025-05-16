from django import forms

class MiFormulario(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100, show_hidden_initial= True)