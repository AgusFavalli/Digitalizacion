from django.db import models

class Area(models.Model):
    nombre= models.CharField(max_length=100, unique=True, verbose_name='Nombre del área')
    descripcion= models.TextField(blank=True, verbose_name='Descripción')
    es_mesa_entrada= models.BooleanField(default=False, verbose_name='¿Es Mesa de Entrada?', help_text='Marca si esta área recibe trámites nuevos de ciudadanos')
    activa= models.BooleanField(default=True, verbose_name='Activa')
    # Auditoría
    fecha_creacion= models.DateTimeField(auto_now_add=True)
    fecha_modificacion= models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'
        ordering= ['nombre']
    
    def __str__(self):
        mesa=  " [Mesa de Entrada]" if self.es_mesa_entrada else ""
        return f"{self.nombre}{mesa}"
