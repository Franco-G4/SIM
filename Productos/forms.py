


from django import forms
from .models import Productos

# todos los formularios del modelo producto. 
class Prod_forms(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'
        widgets = {
            'codigo' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'codigo del producto',
                    'autocomplete' : 'off',
                    'autofocus' : 'autofocus',
                    'required' : 'true',
                }
            ),

            'fechaultima' : forms.DateInput(
                attrs={
                    'class' : 'form-control',
                    'invalid' : 'true',
                    'type' : 'date',
                }
            ),
            'descripcion' : forms.TextInput(
                attrs= {
                    'class' : 'form-control',
                    'placeholder' : 'Descripcion del producto',
                    'autocomplete' : 'off',
                }
            ),
            'idproveedor' : forms.Select(
                attrs={
                    'label' : 'Proveedor',
                }
            ),
            'idcategoria' : forms.Select(
                attrs={
                    'label' : 'Categoria',
                }
            )
        }
