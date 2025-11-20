from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.areas.views import AreaViewSet

router=  DefaultRouter()
router.register(r'', AreaViewSet, basename='area')

urlpatterns= [
    path('',  include(router.urls)),
]