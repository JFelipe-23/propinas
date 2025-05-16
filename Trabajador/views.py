from django.shortcuts import render, redirect

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
            if servicios[0]['correo']==email:
                if servicios[0]['contrasena']==password:
                    return redirect('InicioT')
    else:
        form = MiFormulario()
    return render(request, 'Mesero.html', {'form': form})

def TrabajadorInicio(request):
    return render(request, 'Mesero_INICIO.html')
