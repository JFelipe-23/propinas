from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from Servicio.models import Servicio,Propina
from Cliente.models import Cliente
from Trabajador.models import Trabajador

from .forms import ClienteLogIn, Cliente_NEW

def ClientLogIn(request):
    if request.method == 'POST':
        form = ClienteLogIn(request.POST)
        if form.is_valid():
            # Procesa los datos del formulario aquí
            Cedula = form.cleaned_data['cc']
            try:
                url_redireccion = reverse('InicioC') + f'?dato={Cedula}'
                return redirect(url_redireccion)
            except:
                messages.info(request, 'No existe el Usuario o no tiene servicios!')
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

def Order(request):
    Cedula = request.POST.get('id_cliente')
    if request.method=='POST':
        if request.POST.get('send')=="0":
            ID = request.POST.get('servicio_id')
            nota = request.POST.get('nota')
            puntuacion = int(request.POST.get('Puntuacion'))
            servicio = Servicio.objects.get(id=ID)
            servicio.nota = nota
            servicio.calificacion = puntuacion
            servicio.activa = False
            servicio.save()
            url_redireccion = reverse('InicioC') + f'?dato={Cedula}'
            return redirect(url_redireccion)
        if request.POST.get('send')=="1":
            try:
                propina = float(request.POST.get('Propina'))
                ID = request.POST.get('servicio_id')
                servicio = Servicio.objects.get(id=ID)
                propina2 = Propina(Cantidad = propina, servicio = servicio)
                propina2.save()
                messages.info(request, 'Propina Valida!')
                url_redireccion = reverse('InicioC') + f'?dato={Cedula}'
                return redirect(url_redireccion)
            except:
                messages.info(request, 'Propina invalida o Ya existe!')
                url_redireccion = reverse('InicioC') + f'?dato={Cedula}'
                return redirect(url_redireccion)
    return render(request, 'Order.html')

def ClienteInicio(request):
    dato_recibido = request.GET.get('dato')
    servicios = Servicio.objects.filter(id_cliente=dato_recibido, activa=True).values('id', 'fecha', 'activa', 'id_cliente')
    if request.method == 'POST':
        servicio_id = request.POST['servicio_id']
        servicio = Servicio.objects.filter(id=servicio_id).values('id', 'fecha','calificacion','nota', 'activa', 'id_cliente', 'id_trabajador')
        trabajador = Trabajador.objects.filter(cc=servicio[0]['id_trabajador']).values('nombre')
        return render(request, 'Order.html', {'servicio': servicio[0],'trabajador':trabajador[0]})
    return render(request, 'Cliente_INICIO.html', {'servicios': servicios})