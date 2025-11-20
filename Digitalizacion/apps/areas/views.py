from rest_framework import viewsets
from apps.areas.models import Area
from apps.areas.serializers import AreaSerializer

class AreaViewSet(viewsets.ModelViewSet):
    """
    API endpoints para gestionar áreas
    """

    queryset= Area.objects.all()
    serializer_class= AreaSerializer