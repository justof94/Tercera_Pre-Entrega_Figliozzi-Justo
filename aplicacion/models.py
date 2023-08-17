from django.db import models

# Create your models here.
class EquipoRed(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    nivel_tension = models.CharField(max_length=50)
    edificio = models.CharField(max_length=50)
    gabinete = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    mask = models.CharField(max_length=50)
    defGw = models.CharField(max_length=50)

    def __str__(self):
        return f'#{self.id} - {self.nombre}'
    
    class Meta:
        verbose_name = "Equipo de Red"
        verbose_name_plural = "Equipos de Red"

class EquipoTelecontrol(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    nivel_tension = models.CharField(max_length=50)
    edificio = models.CharField(max_length=50)
    gabinete = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    mask = models.CharField(max_length=50)
    defGw = models.CharField(max_length=50)
    
    def __str__(self):
        return f'#{self.id} - {self.nombre}'
    
    class Meta:
        verbose_name = "Equipo de Telecontrol"
        verbose_name_plural = "Equipos de Telecontrol"

class EquipoProteccion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    nivel_tension = models.CharField(max_length=50)
    edificio = models.CharField(max_length=50)
    gabinete = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    mask = models.CharField(max_length=50)
    defGw = models.CharField(max_length=50)
    
    def __str__(self):
        return f'#{self.id} - {self.nombre}'
    
    class Meta:
        verbose_name = "Equipo de Protección"
        verbose_name_plural = "Equipos de Proteccion"