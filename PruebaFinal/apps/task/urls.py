from django.conf.urls import url, include
from django.urls import path
from apps.task.views import Task, TaskList, TaskCreate, TaskUpdate, TaskDelete, TaskListTar
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('nuevo/', login_required(TaskCreate.as_view()), name='task_create'),
    path('listar/', login_required(TaskList.as_view()), name='task_list'),
    path('listarTask/', login_required(TaskListTar.as_view()), name='task_list_tar'),
    path('editar/<int:pk>)/', login_required(TaskUpdate.as_view()), name='task_edit'),
    path('eliminar/<int:pk>)/', login_required(TaskDelete.as_view()), name='task_delete'),
]
