from django.db import models
from Cliente.models import Cliente
from Trabajador.models import Trabajador

class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    activa = models.BooleanField()
    calificacion = models.IntegerField()
    nota = models.TextField(blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)

    def __str__(self):
        return f"Servicio #{self.id} - {self.fecha}"
