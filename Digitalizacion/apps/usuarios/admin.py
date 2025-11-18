from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.usuarios.models import  Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    """
    Configuración del admin para usuario
    """
    list_display= ['username', 'email', 'dni', 'rol', 'activo', 'fecha_creacion'] # Campos a mostrar en la lista
    list_filter= ['rol', 'activo', 'is_staff', 'is_superuser'] # Filtros laterales
    search_fields= ['username', 'email', 'dni', 'first_name', 'last_name'] # Campos para buscar

    fieldsets= UserAdmin.fieldsets + ( 
        ('Información adicional', {
            'fields': ('dni', 'telefono', 'rol', 'areas', 'activo')
        }),
    ) # Agrega campos adicionales al formulario de edición

    add_fieldsets= UserAdmin.add_fieldsets + (
        ('Información adicional', {
            'fields': ('dni', 'telefono', 'rol', 'areas')
        }),
    )

    filter_horizontal = ['areas', 'groups', 'user_permissions'] # Permite seleccionar múltiples áreas en el admin