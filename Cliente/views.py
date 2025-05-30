from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
import webbrowser, pyautogui
from time import sleep

from Servicio.models import Servicio,Propina
from Cliente.models import Cliente
from Trabajador.models import Trabajador, Local

from .forms import ClienteLogIn, Cliente_NEW

def ClientLogIn(request):
    if request.method == 'POST':
        form = ClienteLogIn(request.POST)
        if form.is_valid():
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
    if not request.session.get('LogInT', False):
        return redirect('LogInT')
    email = request.GET.get('dato')
    if request.method == 'POST':
        form = Cliente_NEW(request.POST)
        if form.is_valid():
            Cedula = form.cleaned_data['cc']
            Nombre = form.cleaned_data['nombre']
            if len(Cliente.objects.values('cc').filter(cc = Cedula))==0:
                try:
                    cliente = Cliente(cc=Cedula,nombre=Nombre)
                    cliente.save()
                    url_redireccion = reverse('InicioT') + f'?dato={email}'
                    return redirect(url_redireccion)
                except:
                    messages.info(request, 'ingreso un dato erroneo!')
            else:
                messages.info(request, 'Ya existe el Usuario!')
    else:
        form = Cliente_NEW()
    return render(request, 'NEW_Cliente.html', {'form': form,'email':email})

def Order(request):
    Cedula = request.POST.get('id_cliente')
    if request.method=='POST':
        if request.POST.get('send')=="0":
            url_redireccion = reverse('InicioC') + f'?dato={Cedula}'
            return redirect(url_redireccion)
        if request.POST.get('send')=="1":
            try:
                ID = request.POST.get('servicio_id')
                nota = request.POST.get('nota')
                propina = float(request.POST.get('Propina'))
                puntuacion = int(request.POST.get('Puntuacion'))
                servicio = Servicio.objects.get(id=ID)
                servicio.nota = nota
                servicio.calificacion = puntuacion
                servicio.activa = False
                servicio.save()
                propina2 = Propina(Cantidad = propina, servicio = servicio)
                propina2.save()
                messages.info(request, '---Gracias---')
                url_redireccion = reverse('InicioC') + f'?dato={Cedula}'
                return redirect(url_redireccion)
            except:
                messages.info(request, 'Ubo un Error vuelve a intentarlo!')
                url_redireccion = reverse('InicioC') + f'?dato={Cedula}'
                return redirect(url_redireccion)
        if request.POST.get('send')=="2":
            ID = request.POST.get('servicio_id')
            TrabajadorID = request.POST.get('Trabajador_id')
            puntuacion = int(request.POST.get('Puntuacion'))
            cliente = Cliente.objects.get(cc=Cedula)
            trabajador = Trabajador.objects.get(cc=TrabajadorID)
            Numero = str(request.POST.get('Numero'))
            if Numero[0] == "3":
                Url=f"https://web.whatsapp.com/send?phone=+57{Numero}"
                webbrowser.open(Url)
                sleep(10)
                pyautogui.typewrite(f"{cliente.nombre} Te acaba de enviar una recomendacion del restaurante ({trabajador.id_local}), con una puntacion de {puntuacion} de 5, atendido por {trabajador.nombre}")
                pyautogui.press('enter')
                url_redireccion = reverse('InicioC') + f'?dato={Cedula}'
                return redirect(url_redireccion)
            else:
                messages.info(request, 'El numero tiene que empesar por 3')
                url_redireccion = reverse('InicioC') + f'?dato={Cedula}'
                return redirect(url_redireccion)
        if request.POST.get('send')=="3":
            try:
                ID = request.POST.get('servicio_id')
                nota = request.POST.get('nota')
                puntuacion = int(request.POST.get('Puntuacion'))
                servicio = Servicio.objects.get(id=ID)
                servicio.nota = nota
                servicio.calificacion = puntuacion
                servicio.activa = False
                servicio.save()
                messages.info(request, '---Gracias---')
                url_redireccion = reverse('InicioC') + f'?dato={Cedula}'
                return redirect(url_redireccion)
            except:
                messages.info(request, 'Ubo un Error vuelve a intentarlo!')
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