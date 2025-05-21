"""
URL configuration for propinas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Cliente.views import ClientLogIn, NewClient, ClienteInicio, Order
from Trabajador.views import TrabajadorLogIn, TrabajadorInicio
from Servicio.views import NewOrder, gestionar_estado_servicio_simple, Inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('LogIn/', ClientLogIn),
    path('NewClient/',NewClient, name= "NewC"),
    path('ClienteInicio/', ClienteInicio, name= "InicioC"),
    path('LogIn_2/',TrabajadorLogIn , name= "LogInT"),
    path('TrabajadorInicio/',TrabajadorInicio, name= "InicioT"),
    path('NewOrder/',NewOrder, name= "NewO"),
    path('EditOrder/', gestionar_estado_servicio_simple, name='gestionar_estado_simple'),
    path('Order/',Order, name= "Orden"),
    path('', Inicio)
]
