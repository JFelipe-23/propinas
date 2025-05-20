from django.contrib import admin
from .models import Local, Trabajador 

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'tipo') 
    search_fields = ('nombre', 'direccion')

@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('cc', 'nombre', 'correo', 'edad', 'id_local')
    list_filter = ('id_local', 'edad')
    search_fields = ('nombre', 'cc', 'correo')
    raw_id_fields = ('id_local',)