from django import forms

from apps.encargado.models import Encargado

class EncargadoForm (forms.ModelForm):
    
    class Meta:
        model = Encargado

        fields = [
            'nombre_encargado',
            'apellido_encargado',
            'genero',
            'nombre_usuario',
            'fecha_nacimiento',
        ]   
        label = {
            'nombre_encargado':'Nombre Encargado',
            'apellido_encargado':'Apellido Encargado',
            'genero':'Genero',
            'nombre_usuario':'Nombre Usuario',
            'fecha_nacimiento':'Fecha Nacimiento',
        }
        widgets = {
            'nombre_encargado': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_encargado': forms.TextInput(attrs={'class':'form-control'}),
            'genero': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control'}),
        }