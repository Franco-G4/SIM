from django import forms
from .models import Categorias

class Cat_form(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = '__all__'
    