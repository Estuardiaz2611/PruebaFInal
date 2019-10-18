from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.usuario.forms import RegistroForm
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
def listadousuarios(request):
    lista = serializers.serialize('json', User.objects.all(), fields=['username', 'first_name', 'email'])
    return HttpResponse(lista, content_type='application/json')
    
class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuario/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('encargado:encargado_principal')