##################################################################
# Script Name: forms.py - Módulo Formulario
# Description: Este formulario tendrá solo las coordenadas Latitud y Longitud del formulario de ingreso de un árbol.
# Args: N/A
# Creation/Update: 2022/12/15 
# Author: Jorge Leonardo Solis - Yordan Moncayo                                                
# Email: jorgesolis1989@gmail.com                                 
##################################################################


from logging import disable
from tkinter import DISABLED
from django import forms

"""
Este formulario se encuentran los datos para logueo del usuario
"""
class Formulario_1(forms.Form):
    latitude = forms.CharField(
        widget=forms.TextInput(attrs={'readonly':'readonly' , 'name':'textLatitude', 'id':'textLatitude', 'class':'form-control text-center', 'placeholder':'Esperando calcular latitud'}))
    longitude = forms.CharField(
        widget=forms.TextInput(attrs={'readonly':'readonly' , 'name':'textLongitude', 'id':'textLongitude', 'class':'form-control text-center', 'placeholder':'Esperando calcular longitude'}))
