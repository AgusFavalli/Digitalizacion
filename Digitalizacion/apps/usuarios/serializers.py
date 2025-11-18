from rest_framework import serializers
from apps.usuarios.models import Usuario
from apps.areas.models import Area

class UsuarioSerializer(serializers.ModelSerializer):
    """ Convierte el modelo Usuario a JSON y viceversa, crea y actualiza usuarios manejando el password de forma segura"""
    password = serializers.CharField(write_only=True, required=False) # El password es solo para escritura

    class Meta:
        model= Usuario
        fields= [
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'dni',
            'telefono',
            'rol',
            'areas',
            'activo',
            'fecha_creacion',
        ]
        read_only_fields= ['id', 'fecha_creacion'] # Campos solo de lectura

    def create(self, validated_data):
        """Crear usuario con password hasheado"""
        areas= validated_data.pop('areas', [])
        password= validated_data.pop('password', None)

        usuario= Usuario.objects.create(**validated_data) # "**" Desempaqueta los datos validados

        if password:
            usuario.set_password(password) # Encripta el password con bcrypt
            usuario.save()  # Guarda el hash 

        if areas:
            usuario.areas.set(areas)

        return usuario
    
    def update(self, instance, validated_data):
        """Actualizar usuario"""
        areas= validated_data.pop('areas', None)
        password= validated_data.pop('password', None)

        # Actualizar campos normalles
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        # Actualizar password si se proporcionó
        if password:
            instance.set_password(password)
        instance.save()

        #  Actualizar áreas si se proporcionaron
        if areas is not None:
            instance.areas.set(areas)
        
        return instance
    