from django.conf.urls import url, include
from django.urls import path
from apps.encargado.views import index, EncargadoList, EncargadoCreate, EncargadoUpdate, EncargadoDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index, name='encargado_principal'),
    path('nuevo/', login_required(EncargadoCreate.as_view()), name='encargado_create'),
    path('listar/', login_required(EncargadoList.as_view()), name='encargado_list'),
    path('editar/<int:pk>/', login_required(EncargadoUpdate.as_view()), name='encargado_edit'),
    path('eliminar/<int:pk>/', login_required(EncargadoDelete.as_view()), name='encargado_delete'),
]
