from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded-lg'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-2 border rounded-lg'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded-lg'
            }),
        }