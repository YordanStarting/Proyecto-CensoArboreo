##################################################################
# Script Name: forms
# .py - Módulo Usario
# Description: Creación del Modelo el cual se migrará a la base de datos.
# Args: N/A
# Creation/Update: 2022/12/15 
# Author: Jorge Leonardo Solis - Yordan Moncayo                                                
# Email: jorgesolis1989@gmail.com                                 
##################################################################


from django import forms
from usuarios.models import Usuario

"""
Este formulario se encuentran los datos para logueo del usuario
"""
class FormularioLogin(forms.Form):
    usuario = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'input' ,'type':'number' , 'value':''}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input'}))


"""
Este formulario se encuentran los datos para el registro de usuario
"""
class FormularioRegistroUsuario(forms.Form):
    usuario = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'input' , 'required':'true'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input'}))
    
    apellidos = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'required':'true'}))
    nombres = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'required':'true'}))

    correo = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'input', 'required':'true'}))

    password_confirmar = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input'}))



# Método auxuliar para confirmar el campo username.
    def confirmar_password(self):
        diccionario_limpio = self.cleaned_data
        cedula = diccionario_limpio.get('username')
        if cedula != int:
            raise forms.ValidationError("La cedula debe de ser enteros")
        return cedula


