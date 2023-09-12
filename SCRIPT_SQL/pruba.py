from django.contrib.auth.models import User
import random
import string

def generar_nombre_aleatorio():
    return ''.join(random.choices(string.ascii_uppercase, k=5))

def generar_apellido_aleatorio():
    return ''.join(random.choices(string.ascii_uppercase, k=7))

def generar_correo_aleatorio():
    dominios = ['gmail.com', 'yahoo.com', 'hotmail.com']
    nombre = generar_nombre_aleatorio()
    apellido = generar_apellido_aleatorio()
    dominio = random.choice(dominios)
    return f"{nombre.lower()}.{apellido.lower()}@{dominio}"

def llenar_base_datos(num_registros):
    for _ in range(num_registros):
        nombre = generar_nombre_aleatorio()
        apellido = generar_apellido_aleatorio()
        correo = generar_correo_aleatorio()
        Usuario.objects.create(nombre=nombre, apellido=apellido, correo_electronico=correo)