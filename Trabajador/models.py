from django.db import models

class Local(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Local")
    direccion = models.CharField(max_length=255, verbose_name="Dirección")
    tipo = models.CharField(max_length=50, verbose_name="Tipo de Local")

    def __str__(self):
        return self.nombre
    
class Trabajador(models.Model):
    cc = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    edad = models.IntegerField()
    contrasena = models.CharField(max_length=128)  # Considera usar un campo específico para contraseñas
    id_local = models.ForeignKey(Local, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre