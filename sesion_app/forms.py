from django import forms

class Page_a_form(forms.Form):
    primer_nombre = forms.CharField(label = 'Nombre')
    apellido = forms.CharField(label='Apellido')

class PageBForm(forms.Form):
    direccion = forms.CharField(label='Dirección')
    celular = forms.CharField(label='Número de teléfono')
    correo = forms.EmailField(label='Correo electrónico')

class Page_c_form(forms.Form):
    comentario = forms.CharField(label='Comentario', widget=forms.Textarea)
