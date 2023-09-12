
##################################################################
# Script Name: views.py - Módulo Formulario
# Description: Son las vistas de todos las funciones con relación al Módulo Formulario
# Args: N/A
# Creation/Update: 2022/12/15 
# Author: Jorge Leonardo Solis - Yordan Moncayo                                                
# Email: jorgesolis1989@gmail.com                                 
##################################################################


from distutils.log import FATAL
from fnmatch import translate
from pickle import FALSE
import re
from django.shortcuts import render
from datetime import datetime
from django.shortcuts import redirect, render
from formulario.models import EstadoFitosanitario , Dasometria, Arbol, Vulnerabilidad, Recomendacion_e_Intervencion
from django.utils import timezone
from django.conf import settings
from usuarios.models import Usuario



#from censoarboleo2022.formulario import forms
from formulario.forms import Formulario_1
# Create your views here.
from django.contrib.auth.decorators import login_required, permission_required
timezone.activate(settings.TIME_ZONE)


# Método listar formularios, corresponde a la función de listar los formularios de cualquier rol en la aplicación
@login_required
def listar_formularios_censista(request):
    
    funcion_llamada = request.session.get('funcion_llamada', 'No')
    llamarMensaje=""
    mensaje=""

    if request.method == 'POST':
        numero_arbol_eliminar = request.POST.get('btn-eliminar', "0");

        arbol_eliminar = Arbol.objects.get(id = numero_arbol_eliminar)
        arbol_eliminar.habilitado = False
        
        try:
            arbol_eliminar.save()
        except Exception as e:
            print(e)

        llamarMensaje = "exito_usuario"
        mensaje = "El registro de formulario se eliminó correctamente"
       
    usuario = Usuario.objects.get(username=request.user.username)
    arboles = None
    base_template = ""
    if usuario.rol == "Censista":
        base_template = "base-censista.html"
        arboles = Arbol.objects.filter(creado_por=usuario.username, habilitado= True).order_by('-creado')
        
        
    
    if funcion_llamada == "editar_usuario":
   
        llamarMensaje = request.session["llamarMensaje"] 
        mensaje = request.session["mensaje"]
        del request.session['funcion_llamada']


    return render(request, 'listar_formularios_censista.html',{'usuario': usuario, 'arboles': arboles, "base_template":base_template, 'mensaje': mensaje, 'llamarMensaje': llamarMensaje})




# Método listar formularios, corresponde a la función de listar los formularios del supervisor y del administrador
@login_required
def listar_formularios(request):
    
    usuario = Usuario.objects.get(username=request.user.username)
    arboles = None
    base_template = ""
    censistas = None

    if usuario.rol == "Administrador":
        base_template = "base-admin.html"
        arboles = Arbol.objects.filter(habilitado = True).order_by('-id')
            
    elif usuario.rol == "Supervisor":
        base_template = "base-supervisor.html"
        
        # Filtrar los árboles del supervisor
        #arboles = Arbol.objects.filter().order_by('-id')
        censistas = Usuario.objects.filter(Grupo=usuario.Grupo).values("cedula_usuario")

        arboles = Arbol.objects.filter(creado_por__cedula_usuario__in=censistas , habilitado= True).order_by('-id')
    
        # programar cuando sea supervisor

    else:
        base_template = "base-supervisor-forestal.html"


    funcion_llamada = request.session.get('funcion_llamada', 'No')
    llamarMensaje=""
    mensaje=""
    if funcion_llamada == "editar_usuario":
   
        llamarMensaje = request.session["llamarMensaje"] 
        mensaje = request.session["mensaje"]
        del request.session['funcion_llamada']


    return render(request, 'listar_formularios.html',{'usuario': usuario, 'arboles': arboles, "base_template":base_template, 'mensaje': mensaje, 'llamarMensaje': llamarMensaje})


# Método ver formularios, corresponde a la función de editar los formularios de cualquier rol en la aplicación y que tenga los permisos correspondientes.
@login_required
def ver_formulario(request , id_arbol=None):

    arbol = Arbol.objects.get(id=id_arbol)

    dasometria = Dasometria.objects.get(arbol_id=id_arbol)

    estado_fitosanitario = EstadoFitosanitario.objects.get(arbol_id=id_arbol)

    recomendacion_e_intervencion = Recomendacion_e_Intervencion.objects.get(arbol_id=id_arbol)

    vulnerabilidad = Vulnerabilidad.objects.get(arbol_id=id_arbol)

    usuario = Usuario.objects.get(username=request.user.username)


    if request.method == 'POST' and 'btnActualizar' in request.POST:
        
        arbol.actualizado = timezone.now()
        arbol.modificado_por = usuario.username
        crear_actualizar_arbol(request, arbol, dasometria,estado_fitosanitario , recomendacion_e_intervencion , vulnerabilidad, True)

   
        
        return redirect("listar_formularios")
        
    
    # Metodo GET
    base_template = ""
    if usuario.rol == "Administrador":
        base_template = "base-admin.html"
    elif usuario.rol == "Censista":
        base_template = "base-censista.html"
    elif usuario.rol == "Supervisor":
        base_template = "base-supervisor.html"

        # programar cuando sea supervisor

    else:
        base_template = "base-supervisor-forestal.html"

    # Consultas de los formulario   

    return render(request, 'ver_formulario.html', {'usuario': usuario, 'arbol': arbol, "dasometria":dasometria,"estado_fitosanitario":estado_fitosanitario,
    "vulnerabilidad":vulnerabilidad, 
    "recomendacion_e_intervencion":recomendacion_e_intervencion, 'base_template':base_template})



# Método editar formularios, corresponde a la función de editar los formularios de cualquier rol en la aplicación y que tenga los permisos correspondientes.
@login_required
def editar_formulario(request , id_arbol=None):

    arbol = Arbol.objects.get(id=id_arbol)

    dasometria = Dasometria.objects.get(arbol_id=id_arbol)

    estado_fitosanitario = EstadoFitosanitario.objects.get(arbol_id=id_arbol)

    recomendacion_e_intervencion = Recomendacion_e_Intervencion.objects.get(arbol_id=id_arbol)

    vulnerabilidad = Vulnerabilidad.objects.get(arbol_id=id_arbol)

    usuario = Usuario.objects.get(username=request.user.username)


    if request.method == 'POST' and 'btnActualizar' in request.POST:
        
        arbol.actualizado = timezone.now()
        arbol.modificado_por = usuario.username

        crear_actualizar_arbol(request, arbol, dasometria,estado_fitosanitario , recomendacion_e_intervencion , vulnerabilidad, True)

        llamarMensaje = "exito_usuario"
        mensaje = "El registro de formulario No "+ str(arbol.id)+" se actualizó correctamente"
        request.session["llamarMensaje"]  = llamarMensaje
        request.session["mensaje"]  = mensaje
        request.session["funcion_llamada"]  = "editar_usuario"

        return redirect("listar_formularios")
        
    
    # Metodo GET
    base_template = ""
    if usuario.rol == "Administrador":
        base_template = "base-admin.html"
    elif usuario.rol == "Censista":
        base_template = "base-censista.html"
    elif usuario.rol == "Supervisor":
        base_template = "base-supervisor.html"

        # programar cuando sea supervisor

    else:
        base_template = "base-supervisor-forestal.html"

    # Consultas de los formulario   

    return render(request, 'edit-formulario.html', {'usuario': usuario, 'arbol': arbol, "dasometria":dasometria,"estado_fitosanitario":estado_fitosanitario,
    "vulnerabilidad":vulnerabilidad, 
    "recomendacion_e_intervencion":recomendacion_e_intervencion, 'base_template':base_template})

# Método crear  formularios, corresponde a la función de crear  un  formularios de cualquier rol en la aplicación
@login_required
@permission_required("usuarios.Censista", login_url="/")
def crear_formulario_view(request):
    usuario = Usuario.objects.get(username=request.user.username)
    mensaje = ""
    llamarMensaje = ""


    if request.method == 'POST' and 'btnFinalizar' in request.POST:
        
        arbol_nuevo = Arbol()
        dasometria_nuevo = Dasometria()
        estadofitosanitario_nuevo = EstadoFitosanitario()
        recomendacion_e_intervencion = Recomendacion_e_Intervencion()
        vulnerabilidad = Vulnerabilidad()
        crear_actualizar_arbol(request, arbol_nuevo, dasometria_nuevo,estadofitosanitario_nuevo , recomendacion_e_intervencion , vulnerabilidad, False)

        mensaje = "El arbol se guardó correctamente"
        llamarMensaje = "exito_usuario"
      
    return render(request, 'formulario.html', {'mensaje': mensaje, 'llamarMensaje': llamarMensaje, "usuario":usuario})



#Mpetodo auxiliar que sirve oara crear y editar un arbol en la BD
def crear_actualizar_arbol(request, arbol, dasometria_nuevo, estadofitosanitario_nuevo , recomendacion_e_intervencion , vulnerabilidad, actualizar ):

    latitude = request.POST["textLatitude"] 
    longitude = request.POST["textLongitude"]

    estado_registro = request.POST["estado_registro"]

    placaAntigua = request.POST.get("placa_antigua", 0)

    requiere_revision = False
    if "requiere_revision" in request.POST and not actualizar:
        requiere_revision = True
    
        
    direccion = request.POST["direccion"]
    
    nombre_comun = request.POST["nombre_comun"]
    nombre_cientifico = request.POST.get('nombre_cientifico', False);
    familia = request.POST.get('familia', False);
    genero = request.POST.get('genero', False);

    estado_madurez = request.POST["estado_madurez"]

    
    # Falta especie

    codigo_qr = request.POST["qr"]
    cobertura = request.POST["cobertura"]
    emplazamiento = request.POST["emplazamiento"]
    confinamiento = request.POST.get('confinamiento');
    dist_confinamiento = 0

    
    # arbol_id es  generado por SQL ---  combina comuna y otras variables 
    arbol.arbolid =  0

    #Creado por

    # Si no es actualización del arbol para la creación o modificación
    if  actualizar:
        arbol.modificado_por =  request.user.username
        arbol.actualizado =  timezone.now()
        arbol.requiere_revision = False
    else:
        usuario_creador_arbol = Usuario.objects.get(username = request.user.username)
        arbol.creado_por = usuario_creador_arbol
        arbol.creado =  timezone.now()

    #  codigo es el código de la placa nueva asociado al QR
    arbol.codigo = codigo_qr

    
    #requiere revision 
    arbol.requiere_revision = requiere_revision

    # No aparece registro en la base de datos
    arbol.estado = estado_registro

    # Si está actualizando y el registro es nuevo por antiguo
    if actualizar and estado_registro == "Nuevo":
        placaAntigua = 0    

    # Placa antigua                 
    arbol.Placa_ant = placaAntigua

    #Qr code
    arbol.qrcode = codigo_qr

    # Latitude y Longitude 
    arbol.longitud = float(longitude.replace(',', '.'))
    arbol.latitud = float(latitude.replace(',', '.'))

    # Norte Este se obtiene por SQL
    arbol.este = 0.0
    arbol.norte = 0.0
    
    # Comuna, barrio, dirección ,

    arbol.direccion = direccion

    # Especie es el nombre científico
    arbol.nombre_cientifico = nombre_cientifico
    arbol.especie = nombre_cientifico
    arbol.familia = familia
    arbol.nombre_comun = nombre_comun
    arbol.genero = genero

    arbol.madurez = estado_madurez






    # Cobertura
    arbol.cobertura = cobertura

    # Confinamiento
    if confinamiento == "si":
        arbol.confinamiento = True
        dist_confinamiento = request.POST["dist_confinamiento"]
    else:
        arbol.confinamiento = False
        dist_confinamiento = 0
        
    arbol.dist_confinamiento = dist_confinamiento

    # E
    arbol.emplazamiento = emplazamiento

    try:
        arbol.save()

    except Exception as e:
        print(e)
    
    arbol.arbolid = arbol.id

        

    # Imágenes de los árboles

    if 'avatar' in request.POST: 
        if not actualizar:
            arbol.foto1 = None
    else: 
        if request.FILES['avatar']:
            arbol.foto1 = request.FILES['avatar']
        else:
            arbol.foto1 = None    
    

    if 'avatar2' in request.POST:
        if not actualizar:     
            arbol.foto2 = None

    else: 
        if request.FILES['avatar2']:
            arbol.foto2 = request.FILES['avatar2']
        else:
            arbol.foto2 = None


    if 'avatar3' in request.POST: 
        if not actualizar:
            arbol.foto3 = None
    
    else:
        if request.FILES['avatar3']:   
            arbol.foto3 = request.FILES['avatar3']    
        else:
            arbol.foto3 = None
    
    if 'avatar4' in request.POST: 
        if not actualizar:
            arbol.foto4 = None
    
    else:
        if request.FILES['avatar4']:   
            arbol.foto4 = request.FILES['avatar4']    
        else:
            arbol.foto4 = None

    arbol.area = 0.0
    arbol.perimetro =0.0
    arbol.hito = 0.0
    arbol.observaciones = ""






    try:
        arbol.save()

    except Exception as e:
        print(e)



################################################################# Tabla Dasometría


    fuste = request.POST.get('tipofuste')
    cap = 0
    cap1= 0
    cap2= 0
    cap3= 0
    cap4= 0
    cap5= 0
    numtallos = 1

    
    dasometria_nuevo.fuste = fuste

    if fuste == "Fuste Único":
        cap = request.POST["cap"]
    else:
        cap1 = request.POST["capa1"]
        cap2 = request.POST["capa2"]
        cap3 = request.POST["capa3"]
        cap4 = request.POST["capa4"]
        cap5 = request.POST["capa5"]



        if cap1 == "":
            cap1 = 0
        if cap2 == "":
            cap2 = 0
        if cap3 == "":
            cap3 = 0
        if cap4 == "":
            cap4 = 0
        if cap5 == "":
            cap5 = 0
        
        numtallos = request.POST["numero_tallos"]
        print(numtallos)



    dasometria_nuevo.cap = cap  
    dasometria_nuevo.cap1 = cap1
    dasometria_nuevo.cap2 = cap2
    dasometria_nuevo.cap3 = cap3
    dasometria_nuevo.cap4 = cap4
    dasometria_nuevo.cap5 = cap5

    dasometria_nuevo.numtallos = numtallos

    altura_fuste =  request.POST["comercial_fuste"]
    altura_arbol = request.POST["totalarbol"]

    orientacion = request.POST["orientacion"]
    inclinacion = request.POST["inclinacion"]

    dasometria_nuevo.altura_arbol = altura_arbol
    dasometria_nuevo.altura_fuste = altura_fuste
    dasometria_nuevo.orientacion = orientacion
    dasometria_nuevo.inclinacion = inclinacion
    
    # Circunferencia
    dasometria_nuevo.circunferencia = 0


    diacopa_mayor = request.POST["ejemayor"]
    diacopa_menor = request.POST["ejemenor"]
    exposicion_luz = request.POST["exposicionluz"]

    dasometria_nuevo.diacopa_mayor = diacopa_mayor
    dasometria_nuevo.diacopa_menor = diacopa_menor
    dasometria_nuevo.expcopaluz = exposicion_luz


    copaviva  = request.POST["copa_viva"]
    copa_ausente = request.POST["copa_ausente"]
    
    dasometria_nuevo.copaviva = copaviva
    dasometria_nuevo.copausente = copa_ausente

    diametro_ramas = request.POST["diametro"]

    dasometria_nuevo.diametro_ramas = diametro_ramas

    sistemaradicular = request.POST["sistemaradicular"]
    dasometria_nuevo.tiporaiz = sistemaradicular

    dasometria_nuevo.arbol_id = arbol

    if actualizar:
        dasometria_nuevo.actualizado = timezone.now()
        dasometria_nuevo.modificadopor   = request.user.username


    try:
        dasometria_nuevo.save()
    except Exception as e:
        print(e)    

################################################################# Tabla EstadoFitosanitario

    #

    vitalidad = request.POST["vitalidad"]

    estadofitosanitario_nuevo.vitalidad = vitalidad
    estadofitosanitario_nuevo.arbol_id = arbol

    estadofitosanitario_nuevo = crear_EstadoFitosanitario(estadofitosanitario_nuevo, request)


    try:
        estadofitosanitario_nuevo.save()
    except Exception as e:
        print(e)

############################################################# Tabla Vulnerabilidad

 

    vulnerabilidad.arbol_id = arbol

    personas = False
    construcciones = False
    redes_aereas = False
    vehiculos = False



    if "personas" in request.POST:
        personas = True

    if "construcciones" in request.POST:
        construcciones = True

    if "redes_aereas" in request.POST:
        redes_aereas = True
    
    if "vehiculos" in request.POST:
        vehiculos = True

    vulnerabilidad.personas = personas
    vulnerabilidad.construcciones = construcciones
    vulnerabilidad.redes_aereas = redes_aereas
    vulnerabilidad.vehiculos = vehiculos

    try:
        vulnerabilidad.save()
    except Exception as e:
        print(e)

############################################################# Tabla Recomendaciones e Intervención



    erradicacion = False
    poda_aclareo = False
    poda_equilibrio = False
    poda_formacion = False
    poda_limpieza = False
    poda_ramas_laterales = False
    poda_realce = False
    poda_ramas_secas  = False
    poda_sanitaria = False
    poda_reduccion_altura = False
    poda_redes_secundarias = False
    poda_limpieza_parasitas = False
    poda_despeje_redes = False
    poda_reduccion_altura = False
    transplante = False
    eliminar_piso_duro = False
    controlfitosanitario = False
    otros_control_fitosanitario = False
    porque_tala = "" 
    comentarios_control_fitosanitario = ""
    comentarios = ""

    if "erradicacion" in request.POST:
        erradicacion = True

    if "poda_aclareo" in request.POST:
        poda_aclareo = True

    if "poda_equilibrio" in request.POST:
        poda_equilibrio = True

    if "poda_formacion" in request.POST:
        poda_formacion = True

    if "poda_limpieza" in request.POST:
        poda_limpieza = True

    if "poda_ramas_laterales" in request.POST:
        poda_ramas_laterales = True

    if "poda_ramas_secas" in request.POST:
        poda_ramas_secas = True

    if "poda_sanitaria" in request.POST:
        poda_sanitaria = True

    if "poda_redes_secundarias" in request.POST:
        poda_redes_secundarias = True

    if "poda_reduccion_altura" in request.POST:
        poda_reduccion_altura = True

    if "poda_despeje_redes" in request.POST:
        poda_despeje_redes = True

    if "transplante" in request.POST:
        transplante = True

    if "eliminar_piso_duro" in request.POST:
        eliminar_piso_duro = True

    if "limpieza_parasistas" in request.POST:
        poda_limpieza_parasitas = True

    if "controlfitosanitario" in request.POST:
        controlfitosanitario = True
    
    if "otros_control_fitosanitario" in request.POST:
        otros_control_fitosanitario = True
    
    if estadofitosanitario_nuevo.vitalidad == "Mala":
        erradicacion = True

    if "poda_realce" in request.POST:
        poda_realce = True

    if "porquetala" in request.POST:
        porque_tala = request.POST["porquetala"]

    if "comentarios_en_general" in request.POST:
        comentarios = request.POST["comentarios_en_general"]

    if "comentarios_otros" in request.POST and otros_control_fitosanitario:
        comentarios_control_fitosanitario = request.POST["comentarios_otros"]




    recomendacion_e_intervencion.erradicacion = erradicacion
    recomendacion_e_intervencion.poda_aclareo = poda_aclareo
    recomendacion_e_intervencion.poda_equilibrio = poda_equilibrio
    recomendacion_e_intervencion.poda_formacion = poda_formacion
    recomendacion_e_intervencion.poda_limpieza = poda_limpieza
    recomendacion_e_intervencion.poda_ramas_laterales = poda_ramas_laterales
    recomendacion_e_intervencion.poda_ramas_secas = poda_ramas_secas
    recomendacion_e_intervencion.poda_sanitaria = poda_sanitaria
    recomendacion_e_intervencion.poda_reduccion_altura = poda_reduccion_altura
    recomendacion_e_intervencion.poda_redes_secundarias = poda_redes_secundarias
    recomendacion_e_intervencion.poda_despeje_redes = poda_despeje_redes
    recomendacion_e_intervencion.transplante = transplante
    recomendacion_e_intervencion.eliminar_piso_duro = eliminar_piso_duro
    recomendacion_e_intervencion.arbol_id = arbol
    recomendacion_e_intervencion.poda_realce = poda_realce
    recomendacion_e_intervencion.poda_limpieza_parasitas = poda_limpieza_parasitas
    recomendacion_e_intervencion.control_fitosanitario = controlfitosanitario
    recomendacion_e_intervencion.otros_control_fitosanitario = otros_control_fitosanitario
    recomendacion_e_intervencion.porque_tala = porque_tala
    recomendacion_e_intervencion.comentarios = comentarios
    recomendacion_e_intervencion.comentarios_control_fitosanitario = comentarios_control_fitosanitario

    
    try:
        recomendacion_e_intervencion.save()
    except Exception as e:
        print(e)



# Método auxiliar para crear la Tabla EstadoFitosanitario.
def crear_EstadoFitosanitario(estadofitosanitario_nuevo, request):

    mecanica_fuste = False
    mecanica_f_heridas = False
    mecanica_f_anillado = False
    mecanica_f_quemaduras = False
    
    biologica_fuste = False
    biologica_f_perfobarrenado = False
    biologica_f_necrosis = False
    biologica_f_descortezado = False
    biologica_f_tumores = False
    
    antropologica_fuste = False
    antropica_f_poda = False
    antropica_f_escombros = False
    antropica_f_pintura = False

    mecanica_copa = False
    mecanica_c_heridas = False
    mecanica_c_quemaduras = False
    
    biologica_copa = False
    biologica_c_defoliacion = False
    biologica_c_clorosis = False
    biologica_c_minado = False
    biologica_c_necrosis = False
    biologica_c_parasitas = False
    
    
    antropologica_copa = False
    antropica_c_poda = False
    antropica_c_contamatmosferica = False

    mecanica_raiz = False
    mecanica_r_heridas  = False
    mecanica_r_quemaduras  = False

    biologica_r_necrosis = False
    biologica_raiz = False
    
    antropica_r_poda = False
    antropica_r_escombro =False
    antropica_r_prd_toxicos = False
    antropica_raiz = False

    general_f_sano = False
    general_c_sano = False
    general_r_sano = False

    if estadofitosanitario_nuevo.vitalidad == "Regular":

    ############################################### Afectacion Fuste. 

        if "mecanica_f_heridas" in request.POST:
            mecanica_f_heridas = True
        
        if "mecanica_f_quemaduras" in request.POST:
            mecanica_f_quemaduras = True
        
        if "mecanica_f_anillado" in request.POST:
            mecanica_f_anillado = True

        if "biologica_f_perfobarrenado" in request.POST:
            biologica_f_perfobarrenado = True

        if "biologica_f_necrosis" in request.POST:
            biologica_f_necrosis = True

        if "biologica_f_descortezado" in request.POST:
            biologica_f_descortezado = True

        if "biologica_f_tumores" in request.POST:
            biologica_f_tumores = True

        if "antropica_f_poda" in request.POST:
            antropica_f_poda = True

        if "antropica_f_escombros" in request.POST:
            antropica_f_escombros = True

        if "antropica_f_pintura" in request.POST:
            antropica_f_pintura = True

        if(mecanica_f_heridas or  mecanica_f_quemaduras or  mecanica_f_anillado):
            mecanica_fuste= True

        if(biologica_f_necrosis or  biologica_f_descortezado or biologica_f_tumores or biologica_f_perfobarrenado):
            biologica_fuste = True

        if(antropica_f_poda or antropica_f_escombros or antropica_f_pintura):
            antropologica_fuste = True

    
    


    ############################################### Afectacion Copa. 

        
        if "mecanica_c_heridas" in request.POST:
            mecanica_c_heridas = True
        
        if "mecanica_c_quemaduras" in request.POST:
            mecanica_c_quemaduras = True
        
        if "biologica_c_defoliacion" in request.POST:
            biologica_c_defoliacion = True

        if "biologica_c_clorosis" in request.POST:
            biologica_c_clorosis = True

        if "biologica_c_minado" in request.POST:
            biologica_c_minado = True

        if "biologica_c_necrosis" in request.POST:
            biologica_c_necrosis = True

        if "biologica_c_parasitas" in request.POST:
            biologica_c_parasitas = True

        if "antropica_c_contamatmosferica" in request.POST:
            antropica_c_contamatmosferica = True

        if "antropica_c_poda" in request.POST:
            antropica_c_poda = True


        if(mecanica_c_heridas or  mecanica_c_quemaduras):
            mecanica_copa= True

        if(biologica_c_defoliacion or  biologica_c_clorosis or biologica_c_minado or biologica_c_necrosis or biologica_c_parasitas):
            biologica_copa = True

        if(antropica_c_contamatmosferica or antropica_c_poda):
            antropologica_copa = True

    

############################################### Afectacion  Raices. 


        if "mecanica_r_heridas" in request.POST:
            mecanica_r_heridas = True
        
        if "mecanica_r_quemaduras" in request.POST:
            mecanica_r_quemaduras = True
        
        if "biologica_r_necrosis" in request.POST:
            biologica_r_necrosis = True
                    
        if "antropica_r_poda" in request.POST:
            antropica_r_poda = True
            
        if "antropica_r_escombro" in request.POST:
            antropica_r_escombro = True
                        
        if "antropica_r_prd_toxicos" in request.POST:
            antropica_r_prd_toxicos = True

        if(mecanica_r_heridas or  mecanica_r_quemaduras):
            mecanica_raiz = True

        if(biologica_r_necrosis):
            biologica_raiz = True

        if(antropica_r_poda or antropica_r_escombro or antropica_r_prd_toxicos ):
            antropica_raiz = True


################################################Estado general

        if "general_f_sano" in request.POST:
            general_f_sano = True

        if "general_c_sano" in request.POST:
            general_c_sano = True

        if "general_r_sano" in request.POST:
            general_r_sano = True

    
    #Asignamos 
    estadofitosanitario_nuevo.mecanica_c_heridas = mecanica_c_heridas
    estadofitosanitario_nuevo.mecanica_c_quemaduras = mecanica_c_quemaduras
    estadofitosanitario_nuevo.mecanica_copa = mecanica_copa
    
    estadofitosanitario_nuevo.biologica_c_defoliacion =  biologica_c_defoliacion
    estadofitosanitario_nuevo.biologica_c_clorosis = biologica_c_clorosis
    estadofitosanitario_nuevo.biologica_c_minado = biologica_c_minado
    estadofitosanitario_nuevo.biologica_c_necrosis = biologica_c_necrosis
    estadofitosanitario_nuevo.biologica_c_parasitas = biologica_c_parasitas
    estadofitosanitario_nuevo.biologica_copa = biologica_copa

    estadofitosanitario_nuevo.antropica_c_contamatmosferica = antropica_c_contamatmosferica
    estadofitosanitario_nuevo.antropica_c_poda = antropica_c_poda
    estadofitosanitario_nuevo.antropologica_copa = antropologica_copa

    #Asignamos 
    estadofitosanitario_nuevo.mecanica_r_heridas = mecanica_r_heridas
    estadofitosanitario_nuevo.mecanica_r_quemaduras = mecanica_r_quemaduras
    estadofitosanitario_nuevo.mecanica_raiz = mecanica_raiz
    
    estadofitosanitario_nuevo.biologica_r_necrosis =  biologica_r_necrosis
    estadofitosanitario_nuevo.biologica_raiz = biologica_raiz

    estadofitosanitario_nuevo.antropica_r_poda = antropica_r_poda
    estadofitosanitario_nuevo.antropica_r_escombro = antropica_r_escombro
    estadofitosanitario_nuevo.antropica_r_prd_toxicos = antropica_r_prd_toxicos
    estadofitosanitario_nuevo.antropologica_raiz = antropica_raiz    
    
    estadofitosanitario_nuevo.mecanica_f_heridas = mecanica_f_heridas
    estadofitosanitario_nuevo.mecanica_f_anillado = mecanica_f_anillado
    estadofitosanitario_nuevo.mecanica_f_quemaduras = mecanica_f_quemaduras
    estadofitosanitario_nuevo.mecanica_fuste = mecanica_fuste
    
    estadofitosanitario_nuevo.biologica_f_perfobarrenado =  biologica_f_perfobarrenado
    estadofitosanitario_nuevo.biologica_f_necrosis = biologica_f_necrosis
    estadofitosanitario_nuevo.biologica_f_descortezado = biologica_f_descortezado
    estadofitosanitario_nuevo.biologica_f_tumores = biologica_f_tumores
    estadofitosanitario_nuevo.biologica_fuste = biologica_fuste

    estadofitosanitario_nuevo.antropica_f_escombros = antropica_f_escombros
    estadofitosanitario_nuevo.antropica_f_poda = antropica_f_poda
    estadofitosanitario_nuevo.antropica_f_pintura = antropica_f_pintura
    estadofitosanitario_nuevo.antropologica_fuste = antropologica_fuste

    estadofitosanitario_nuevo.general_f_sano =general_f_sano
    estadofitosanitario_nuevo.general_c_sano = general_c_sano
    estadofitosanitario_nuevo.general_r_sano = general_r_sano

    
    return estadofitosanitario_nuevo

