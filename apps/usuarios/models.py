from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    """
    Modelo de usuario extendido, hereda de AbstractUser (trae username, email, password, etc.)
    """

    # Diferentes roles de usuario
    ROL_CHOICES  = [
        ('CIUDADANO', 'Ciudadano'),
        ('EMPLEADO', 'Empleado Municipal'),
        ('ADMIN', 'Administrador'),
    ]

    # Campos adicionales
    dni = models.CharField(max_length=8, unique=True, verbose_name='DNI', help_text='Documento Nacional de Identidad (sin puntos)')
    telefono = models.CharField(max_length=20, blank=True, verbose_name='Teléfono')
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='CIUDADANO', verbose_name='Rol')

    # Relacion con areas (en caso que un empleado pueda estar en varias areas)
    areas = models.ManyToManyField('areas.Area', blank=True, related_name='empleados', verbose_name='Áreas asignadas')

    # Campos de auditoría
    fecha_creacion = models.DateTimeField(auto_now_add=True) 
    fecha_modificacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.get_full_name()} ({self.dni})"
    
    # Métodos personalizados
    def es_ciudadano(self):
        return self.rol == 'CIUDADANO'
    
    def es_empleado(self):
        return self.rol == 'EMPLEADO'
    
    def es_admin(self):
        return self.rol == 'ADMIN'
    
    def es_mesa_entrada(self): 
        """Verifica si trabaja en Mesa de Entrada"""
        return self.areas.filter(es_mesa_entrada=True).exists()
    
    def puede_recibir_tramites_nuevos(self):
        """Lógica de negocio"""
        return self.es_empleado() and self.es_mesa_entrada()