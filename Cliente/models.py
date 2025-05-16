from django.db import models

class Cliente(models.Model):
    cc = models.CharField(max_length=50, primary_key=True, verbose_name="Cédula de Ciudadanía")
    nombre = models.CharField(max_length=255, verbose_name="Nombre Completo")

    def __str__(self):
        return f"{self.nombre} ({self.cc})"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"