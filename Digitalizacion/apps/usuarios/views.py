from rest_framework import viewsets
from apps.usuarios.models import Usuario
from apps.usuarios.serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoints para gestionar usuarios
    """

    queryset= Usuario.objects.all()
    serializer_class= UsuarioSerializer