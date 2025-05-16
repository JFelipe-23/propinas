from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from Servicio.models import Servicio
from Cliente.models import Cliente

from .forms import ClienteLogIn, Cliente_NEW

def ClientLogIn(request):
    if request.method == 'POST':
        form = ClienteLogIn(request.POST)
        if form.is_valid():
            # Procesa los datos del formulario aquí
            Cedula = form.cleaned_data['cc']
            servicios = Servicio.objects.filter(id_cliente_id=Cedula).values('id', 'fecha', 'activa', 'id_cliente_id')
            # Redirige a una página de éxito
            return render(request, 'Cliente_INICIO.html',{"servicios":servicios})
    else:
        form = ClienteLogIn()
    return render(request, 'Cliente.html', {'form': form})
def NewClient(request):
    if request.method == 'POST':
        form = Cliente_NEW(request.POST)
        if form.is_valid():
            # Procesa los datos del formulario aquí
            Cedula = form.cleaned_data['cc']
            Nombre = form.cleaned_data['nombre']
            if Cliente.objects.values('cc').filter(cc = Cedula)==[]:
                try:
                    cliente = Cliente(cc=Cedula,nombre=Nombre)
                    cliente.save()
                    return redirect('InicioT')
                except:
                    messages.info(request, 'Ya existe el Usuario!')
            else:
                messages.info(request, 'Ya existe el Usuario!')
    else:
        form = Cliente_NEW()
    return render(request, 'NEW_Cliente.html', {'form': form})
def ClienteInicio(request):
    template = loader.get_template("Cliente_INICIO.html")
    context = {}
    return HttpResponse(template.render(context, request))