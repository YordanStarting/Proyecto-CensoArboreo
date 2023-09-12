##################################################################
# Script Name: models.py - Módulo Formulario
# Description: Este archivo encontrarás las clases que luego se convierten en Tablas de la Base de datos, todas dedicadas al Formulario
# Args: N/A
# Creation/Update: 2022/12/15 
# Author: Jorge Leonardo Solis - Yordan Moncayo                                                
# Email: jorgesolis1989@gmail.com                                 
##################################################################




from email.policy import default
from time import timezone
from django.db import models
import os
from uuid import uuid4
from usuarios.models import Usuario

def path_and_rename(instance, filename):
    upload_to = 'photos'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)



# Create your models here.
class Arbol(models.Model):
    id = models.BigAutoField(primary_key=True)
    arbolid = models.BigIntegerField(null=False)
    codigo = models.TextField(null=False)
    Placa_ant = models.TextField(null=True)
    qrcode = models.CharField(max_length=200)
    barrio = models.TextField(null=False)
    direccion = models.TextField(null=False)
    comuna = models.CharField(null=False, max_length=2)
    latitud = models.FloatField(null=False)
    longitud = models.FloatField(null=False)

    norte = models.FloatField(null=False)
    este = models.FloatField(null=False)
    
    nombre_comun = models.TextField(null=False)
    nombre_cientifico = models.TextField(null=False)
    familia = models.TextField(null=False)
    genero = models.TextField(null=False)

    madurez = models.TextField(null=False)

    especie = models.TextField(null=False)
    tipo_vegetacion = models.TextField(null=False)
    area = models.FloatField(null=True)
    perimetro = models.FloatField(null=True)
    hito = models.TextField(null=True)
    estado_conservacion = models.TextField(null=True)
    intervencion = models.TextField(null=True)

    cobertura = models.TextField(null=False)
    emplazamiento = models.TextField(null=False)
    confinamiento = models.BooleanField(null=False)
    dist_confinamiento = models.IntegerField(null=True)

    

    
    class Meta:
        ordering = ["id"]
        db_table = 'arbol'


    def _generar_ruta_imagen_1(instance, filename):
        # El primer paso es extraer la extension de la imagen del
        # archivo original
        extension = os.path.splitext(filename)[1][1:]

        # Generamos la ruta relativa a MEDIA_ROOT donde almacenar
        # el archivo, usando la fecha actual (año/mes)
        ruta = os.path.join('fotos_arboles/', str(instance.id))

        # Generamos el nombre del archivo con un identificador
        # aleatorio, y la extension del archivo original.
        nombre_archivo = '{}.{}'.format(str(instance.id)+"_foto1", extension)

        # Devolvermos la ruta completa
        return os.path.join(ruta, nombre_archivo)


    def _generar_ruta_imagen_2(instance, filename):
        # El primer paso es extraer la extension de la imagen del
        # archivo original
        extension = os.path.splitext(filename)[1][1:]

        # Generamos la ruta relativa a MEDIA_ROOT donde almacenar
        # el archivo, usando la fecha actual (año/mes)
        ruta = os.path.join('fotos_arboles/', str(instance.id))

        # Generamos el nombre del archivo con un identificador
        # aleatorio, y la extension del archivo original.
        nombre_archivo = '{}.{}'.format(str(instance.id)+"_foto2", extension)

        # Devolvermos la ruta completa
        return os.path.join(ruta, nombre_archivo)


    def _generar_ruta_imagen_3(instance, filename):
        # El primer paso es extraer la extension de la imagen del
        # archivo original
        extension = os.path.splitext(filename)[1][1:]

        # Generamos la ruta relativa a MEDIA_ROOT donde almacenar
        # el archivo, usando la fecha actual (año/mes)
        ruta = os.path.join('fotos_arboles/', str(instance.id))

        # Generamos el nombre del archivo con un identificador
        # aleatorio, y la extension del archivo original.
        nombre_archivo = '{}.{}'.format(str(instance.id)+"_foto3", extension)

        # Devolvermos la ruta completa
        return os.path.join(ruta, nombre_archivo)


    def _generar_ruta_imagen_4(instance, filename):
        # El primer paso es extraer la extension de la imagen del
        # archivo original
        extension = os.path.splitext(filename)[1][1:]

        # Generamos la ruta relativa a MEDIA_ROOT donde almacenar
        # el archivo, usando la fecha actual (año/mes)
        ruta = os.path.join('fotos_arboles/', str(instance.id))

        # Generamos el nombre del archivo con un identificador
        # aleatorio, y la extension del archivo original.
        nombre_archivo = '{}.{}'.format(str(instance.id)+"_foto4", extension)

        # Devolvermos la ruta completa
        return os.path.join(ruta, nombre_archivo)



    foto1 =  models.ImageField(upload_to=_generar_ruta_imagen_1 )
    foto2 =  models.ImageField(upload_to=_generar_ruta_imagen_2 )
    foto3 =  models.ImageField(upload_to=_generar_ruta_imagen_3 )
    foto4 =  models.ImageField(upload_to=_generar_ruta_imagen_4 )


    observaciones = models.TextField(null=True)

    habilitado =  models.BooleanField(default=True)
    requiere_revision = models.BooleanField(default=False)
    estado = models.TextField(null=True)
    creado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True, blank=True)
    modificado_por = models.BigIntegerField(null=True)
    actualizado =  models.DateTimeField(auto_now_add=True, blank=True)
    version = models.DateField(auto_now_add=True, blank=True)


################################################################# Tabla Dasometría

class Dasometria(models.Model):
    id = models.BigAutoField(primary_key=True)
    arbol_id = models.ForeignKey(Arbol, on_delete=models.CASCADE)
    fuste = models.TextField(null = False)
    numtallos = models.IntegerField(null=True)
    cap = models.IntegerField(null=True)
    cap1 = models.IntegerField(null=True)
    cap2 = models.IntegerField(null=True)
    cap3 = models.IntegerField(null=True)
    cap4 = models.IntegerField(null=True)
    cap5 = models.IntegerField(null=True)
    altura_fuste = models.FloatField(null=False)
    altura_arbol = models.FloatField(null=False)
    circunferencia = models.FloatField(null=True)
    
    diacopa_mayor = models.FloatField(null=False)
    diacopa_menor = models.FloatField(null=False)
    inclinacion = models.TextField(null=True)
    orientacion = models.TextField(null=True)
    
    copaviva = models.FloatField(null=True) #Altura
    copausente = models.FloatField(null=True)
    expcopaluz = models.TextField(null=False)
    tiporaiz = models.TextField(null=False)
    diametro_ramas = models.TextField(null=True)


    comentarios = models.TextField(null=True)
    modificadopor = models.TextField(null=True)
    actualizado = models.DateTimeField(null=True)
    version = models.DateField(null=True)

  
    class Meta:
        ordering = ["id"]
        db_table = 'dasometria'



class EstadoFitosanitario(models.Model):
    id = models.BigAutoField(primary_key=True)
    arbol_id = models.ForeignKey(Arbol, on_delete=models.CASCADE)
    vitalidad = models.TextField(null=False)

 #   tiposafectacion = models.TextField(null=True)
    mecanica_fuste = models.BooleanField(null=False)
    mecanica_copa = models.BooleanField(null=False)
    mecanica_raiz = models.BooleanField(null=False)
    
    biologica_fuste = models.BooleanField(null=False)
    biologica_copa = models.BooleanField(null=False)
    biologica_raiz = models.BooleanField(null=False)

    antropologica_fuste = models.BooleanField(null=False)
    antropologica_copa = models.BooleanField(null=False)
    antropologica_raiz = models.BooleanField(null=False)
    
    # Afectación de fuste
    mecanica_f_heridas  = models.BooleanField(null=False)
    mecanica_f_anillado  = models.BooleanField(null=False)
    mecanica_f_quemaduras  = models.BooleanField(null=False)
    biologica_f_perfobarrenado  = models.BooleanField(null=False)
    biologica_f_necrosis  = models.BooleanField(null=False)
    biologica_f_descortezado = models.BooleanField(null=False)
    biologica_f_tumores = models.BooleanField(null=False)
    antropica_f_poda = models.BooleanField(null=False)
    antropica_f_escombros = models.BooleanField(null=False)
    antropica_f_pintura = models.BooleanField(null=False)

    # Afectación de Copa
    mecanica_c_heridas  = models.BooleanField(null=False)
    mecanica_c_quemaduras = models.BooleanField(null=False)
    biologica_c_defoliacion = models.BooleanField(null=False)
    biologica_c_clorosis = models.BooleanField(null=False)
    biologica_c_minado = models.BooleanField(null=False)
    biologica_c_necrosis = models.BooleanField(null=False)
    biologica_c_parasitas = models.BooleanField(null=False)
    antropica_c_poda = models.BooleanField(null=False)
    antropica_c_contamatmosferica = models.BooleanField(null=False)

    # Afectaciones de raices
    mecanica_r_heridas  = models.BooleanField(null=False)
    mecanica_r_quemaduras  = models.BooleanField(null=False)
    biologica_r_necrosis = models.BooleanField(null=False)
    antropica_r_poda = models.BooleanField(null=False)
    antropica_r_escombro = models.BooleanField(null=False)
    antropica_r_prd_toxicos = models.BooleanField(null=False)


    # 
    general_f_sano  = models.BooleanField(null=False)
    general_c_sano = models.BooleanField(null=False)
    general_r_sano = models.BooleanField(null=False)


    comentarios = models.TextField(null=True)
    modificadopor = models.TextField(null=True)
    actualizado = models.DateTimeField(null=True)
    version = models.DateField(null=True)

    class Meta:
        ordering = ["id"]
        db_table = 'estadoFitosanitario'

############################################## Clase Vulnerabilidad
class Vulnerabilidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    arbol_id = models.ForeignKey(Arbol, on_delete=models.CASCADE)
    personas = models.BooleanField(null=False)
    vehiculos =models.BooleanField(null=False)
    construcciones =models.BooleanField(null=False)
    redes_aereas =models.BooleanField(null=False)
    
    comentarios = models.TextField(null=True)
    creado = models.DateField(auto_now_add=True, blank=True)
    modificadopor = models.TextField(null=True)
    actualizado = models.DateTimeField(null=True)
    version = models.DateField(null=True)

    class Meta:
        ordering = ["id"]
        db_table = 'vulnerabilidad'


class Recomendacion_e_Intervencion(models.Model):
    id = models.BigAutoField(primary_key=True)
    arbol_id = models.ForeignKey(Arbol, on_delete=models.CASCADE)
    control_fitosanitario = models.BooleanField(null=False) # Ok
    
    erradicacion =models.BooleanField(null=False) # Ok
    poda_aclareo =models.BooleanField(null=False)# Ok
    poda_equilibrio =models.BooleanField(null=False)# Ok
    poda_formacion =models.BooleanField(null=False)# Ok
    poda_limpieza =models.BooleanField(null=False) # Ok
    poda_realce =models.BooleanField(null=False) # Ok
    

    poda_ramas_laterales = models.BooleanField(null=False) # Ok
    poda_ramas_secas = models.BooleanField(null=False) # Ok
    poda_sanitaria = models.BooleanField(null=False) # Ok
    poda_reduccion_altura = models.BooleanField(null=False)# Ok
 
    poda_redes_secundarias = models.BooleanField(null=False)# Ok
    poda_limpieza_parasitas =  models.BooleanField(null=False) # Ok

    poda_despeje_redes =  models.BooleanField(null=False)# Ok
    poda_reduccion_altura   =  models.BooleanField(null=False)
    transplante = models.BooleanField(null=False)# Ok
    eliminar_piso_duro = models.BooleanField(null=False)# Ok
    otros_control_fitosanitario = models.BooleanField(null=False) # Ok
    comentarios_control_fitosanitario = models.TextField(null=True)
    porque_tala= models.TextField(null=True)
    comentarios = models.TextField(null=True)
    creado = models.DateField(auto_now_add=True, blank=True)
    modificadopor = models.TextField(null=True)
    actualizado = models.DateTimeField(null=True)
    version = models.DateField(null=True)

    class Meta:
        ordering = ["id"]
        db_table = 'Recomendacion_e_intervencion'

