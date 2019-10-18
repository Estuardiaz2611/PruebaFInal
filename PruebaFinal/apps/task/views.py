from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.task.forms import TaskForm
from apps.task.models import Task

class TaskList(ListView):
    model = Task
    template_name = 'task/task_list.html'
    paginate_by = 5

class TaskListTar(ListView):
    model = Task
    template_name = 'task/task_tar_list.html'

class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('task:task_list')

class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('task:task_list')

class TaskDelete(DeleteView):
    model = Task
    template_name = 'task/task_delete.html'
    success_url = reverse_lazy('task:task_list')