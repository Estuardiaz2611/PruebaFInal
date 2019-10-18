from django import forms

from apps.task.models import Task

class TaskForm (forms.ModelForm):
    
    class Meta:
        model = Task

        fields = [
            'titulo_task',
            'descripcion',
            'fecha_entrega',
            'encargado',
        ]
        label = {
            'titulo_task': 'Titulo Task',
            'descripcion': 'Descripcion',
            'fecha_entrega': 'Fecha Entrega',
            'encargado': 'Encargado',
        }
        widgets = {
            'titulo_task': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_entrega': forms.TextInput(attrs={'class':'form-control'}),
            'encargado': forms.Select(attrs={'class': 'form-control'})
        }