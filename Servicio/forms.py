from django import forms
from .models import Servicio

class ServicioF(forms.Form):
    id_cliente = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        opciones = kwargs.pop('opciones', [])
        super().__init__(*args, **kwargs)
        self.fields['id_cliente'].choices = opciones

class ServicioBusquedaForm(forms.Form):
    activa_choices = [(True, 'True'), (False, 'False')]
    activa = forms.ChoiceField(label='Activa', choices=activa_choices, required=False)
    id_cliente = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        opciones = kwargs.pop('opciones', [])
        super().__init__(*args, **kwargs)
        self.fields['id_cliente'].choices = opciones