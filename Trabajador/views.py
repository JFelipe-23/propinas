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
                        return redirect('InicioT')
            except:
                messages.info(request, 'Email o Contraseña incorrecta!')
    else:
        form = MiFormulario()
    return render(request, 'Mesero.html', {'form': form})

def TrabajadorInicio(request):
    if not request.session.get('LogInT', False):
        return redirect('LogInT')
    if request.method == 'POST':
        del request.session['LogInT']
        return redirect('LogInT')
    return render(request, 'Mesero_INICIO.html')
