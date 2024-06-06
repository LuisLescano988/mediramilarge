from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PacienteViewSet

router = DefaultRouter()
router.register(r'', PacienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]