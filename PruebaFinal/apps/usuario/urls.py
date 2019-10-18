from django.conf.urls import url
from django.urls import path
from apps.usuario.views import RegistroUsuario, listadousuarios

urlpatterns = [
    path('registrar/', RegistroUsuario.as_view(), name="registrar"),
    path('listado/', listadousuarios, name="listado")
]