from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from Cliente.models import Cliente
from Trabajador.models import Trabajador

from .models import Servicio
from .forms import ServicioF, ServicioBusquedaForm

emailist = []

def  NewOrder(request):
    if not request.session.get('LogInT', False):
        return redirect('LogInT')
    email = request.GET.get('dato')
    if request.method == 'POST':
        form = ServicioF(request.POST, opciones=buscarClientes)
        if form.is_valid():
            # Procesa los datos del formulario aquí
            clienteid = int(form.cleaned_data['id_cliente'])
            cliente = Cliente.objects.get(pk=clienteid)
            trabajador = Trabajador.objects.get(correo=email)
            try:
                servicio = Servicio(activa= True,calificacion=3,nota=None, id_cliente=cliente, id_trabajador=trabajador)
                servicio.save()
                url_redireccion = reverse('InicioT') + f'?dato={email}'
                return redirect(url_redireccion)
            except:
                url_redireccion = reverse('InicioT') + f'?dato={email}'
                return redirect(url_redireccion)
    else:
        form = ServicioF(opciones=buscarClientes)
    return render(request, 'NEW_Order.html',{'form': form})

def gestionar_estado_servicio_simple(request):
    if not request.session.get('LogInT', False):
        return redirect('LogInT')
    resultados = []
    form_busqueda = ServicioBusquedaForm()
    if request.method == 'GET':
        form_busqueda = ServicioBusquedaForm(request.GET, opciones=buscarClientes)
        if form_busqueda.is_valid():
            activa = form_busqueda.cleaned_data.get('activa')
            id_cliente = form_busqueda.cleaned_data.get('id_cliente')

            resultados = Servicio.objects.filter(activa = activa, id_cliente = id_cliente).values('id','fecha','activa', 'id_cliente').order_by('-fecha')

    elif request.method == 'POST' and 'servicio_id' in request.POST and 'activa' in request.POST:
        try:
            servicio_id = request.POST['servicio_id']
            nuevo_estado = request.POST['activa']
            servicio = Servicio.objects.get(id=servicio_id)
            servicio.activa = nuevo_estado
            servicio.save()
            return redirect('LogInT')
        except Servicio.DoesNotExist:
            pass
        
    email = request.GET.get('dato')
    context = {
        'form_busqueda': form_busqueda,
        'resultados': resultados,
        'email':email
    }
    return render(request, 'EDIT_Order.html', context)
def Inicio(request):
    return render(request, 'INICIO.html')

def buscarClientes():
    clientes =  Cliente.objects.values_list('cc', flat=True)
    Resultado = []
    for cliente in clientes:
        Resultado.append((cliente,cliente))
    return Resultado