from rest_framework import serializers
from apps.areas.models import Area

class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model= Area
        fields= [
            'id',
            'nombre',
            'descripcion',
            'es_mesa_entrada',
            'activa',
            'fecha_creacion',
        ]
        read_only_fields= ['id', 'fecha_creacion']