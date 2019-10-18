from django.shortcuts import render, redirect
from apps.encargado.forms import EncargadoForm
from apps.encargado.models import Encargado
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render (request, 'encargado/index.html')

class EncargadoList(ListView):
    model = Encargado
    template_name = 'encargado/encargado_list.html'
    paginate_by = 5

class EncargadoCreate(CreateView):
    model = Encargado
    form_class = EncargadoForm
    template_name = 'encargado/encargado_form.html'
    success_url = reverse_lazy('encargado:encargado_list')

class EncargadoUpdate(UpdateView):
    model = Encargado
    form_class = EncargadoForm
    template_name = 'encargado/encargado_form.html'
    success_url = reverse_lazy('encargado:encargado_list')

class EncargadoDelete(DeleteView):
    model = Encargado
    template_name = 'encargado/encargado_delete.html'
    success_url = reverse_lazy('encargado:encargado_list')