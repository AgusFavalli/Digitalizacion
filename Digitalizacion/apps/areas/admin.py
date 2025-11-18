from django.contrib import admin
from apps.areas.models import  Area

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    """
    Configuración del admin para área
    """
    list_display= ['nombre', 'es_mesa_entrada', 'activa', 'cantidad_empleados', 'fecha_creacion']
    list_filter= ['es_mesa_entrada', 'activa']
    search_fields= ['nombre', 'descripcion']

    def cantidad_empleados(self, obj):
        return obj.empleados.count()
    cantidad_empleados.short_description = 'Empleados'
    