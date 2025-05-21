from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .forms import MiFormulario
from .models import Trabajador

def TrabajadorLogIn(request):
    if request.method == 'POST':
        form = MiFormulario(request.POST)
        if form.is_valid():
            # Procesa los datos del formulario aquí
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            servicios = Trabajador.objects.filter(correo = email, contrasena = password).values()
            try:
                if servicios[0]['correo']==email:
                    if servicios[0]['contrasena']==password:
                        request.session['LogInT'] = True
                        url_redireccion = reverse('InicioT') + f'?dato={email}'
                        return redirect(url_redireccion)
            except:
                messages.info(request, 'Email o Contraseña incorrecta!')
    else:
        form = MiFormulario()
    return render(request, 'Mesero.html', {'form': form})

def TrabajadorInicio(request):
    if not request.session.get('LogInT', False):
        return redirect('LogInT')
    email = request.GET.get('dato')
    if request.method == 'POST':
        if request.POST.get('Botton1')=='1':
            url_redireccion = reverse('NewC') + f'?dato={email}'
            return redirect(url_redireccion)
        if request.POST.get('Botton2')=='2':
            url_redireccion = reverse('NewO') + f'?dato={email}'
            return redirect(url_redireccion)
        if request.POST.get('Botton3')=='3':
            url_redireccion = reverse('gestionar_estado_simple') + f'?dato={email}'
            return redirect(url_redireccion)
        if request.POST.get('Botton4')=='4':
            del request.session['LogInT']
            return redirect('LogInT')
    return render(request, 'Mesero_INICIO.html')