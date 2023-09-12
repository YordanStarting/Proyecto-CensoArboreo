##################################################################
# Script Name: views.py - Módulo Usario
# Description: Son las vistas de todos las funciones con relación al Módulo usuario
# Args: N/A
# Creation/Update: 2022/12/15 
# Author: Jorge Leonardo Solis - Yordan Moncayo                                                
# Email: jorgesolis1989@gmail.com       

##################################################################



# Librerías a importar
from django.shortcuts import render, redirect
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import permission_required
from usuarios.models import Usuario

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from usuarios.forms import FormularioLogin, FormularioRegistroUsuario
from formulario.views import crear_formulario_view
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from json import dumps
from datetime import timedelta
from datetime import datetime

from formulario.models import Arbol

import random
 


# Pagina principal para usuario Administrador
@permission_required("usuarios.Administrador" , login_url="/")
def administrador_home(request , usuario):
    
    censistas = Usuario.objects.filter(rol = "Censista")
    supervisores = Usuario.objects.filter(rol = "Supervisor")

    numero_formularios = Arbol.objects.filter(habilitado= True).count()

  # Fechas apartir de hoy
    d = datetime.now() # current date and time
    
    list_dates = []
    list_dates_1 = []
     
    for x in range(0, 7):
        d1 = d.strftime("%d/%m/%Y")
        list_dates.append(d1)
        list_dates_1.append(d)
        d = d - timedelta(days=1)
    
    list_dates.sort()

    data = []

    grupos = Usuario.objects.values('Grupo').distinct()


    for grupo in grupos:
        dictionary =  dict()
        dictionary["name"] = str(grupo)

        # Por ahora está con números aleatorios entre 20 y 80
        lista_arboles_por_grupo = []
        for fecha in list_dates_1:
            
            cantidad_arboles = Arbol.objects.filter(habilitado = True, creado__date = fecha, creado_por__Grupo = grupo).count()
            #print("fecha ", fecha,  Arbol.objects.filter(habilitado = True, creado__date = fecha, creado_por__Grupo = usuario.Grupo).count())
            lista_arboles_por_grupo.append(cantidad_arboles)

        dictionary["data"] = lista_arboles_por_grupo

        data.append(dictionary)

    list_dates = dumps(list_dates)
    data = dumps(data)

    return render(request, 'administrador.html', {'usuario': usuario, 'numero_censistas':censistas.count(),
                                                  'numero_supervisores':supervisores.count(),
                                               'numero_formularios': numero_formularios, "censistas": censistas, 'data':data , 'list_dates': list_dates})




# Pagina principal para usuario Censista
@permission_required("usuarios.Censista" , login_url="/")
def censista_home(request , usuario):
    if request.method == 'POST' and "btnFormulario" in request.POST:
        return redirect("formulario")
    return render(request, 'censista.html', {'usuario': usuario})


# Pagina principal para usuario Supervisor
@permission_required("usuarios.Supervisor" , login_url="/")
def supervisor_home(request , usuario):
    
    censistas = Usuario.objects.filter(Grupo = usuario.Grupo, rol = "Censista")

    numero_formularios = Arbol.objects.filter(creado_por__cedula_usuario__in=censistas , habilitado= True).count()


    # Fechas apartir de hoy
    d = datetime.now() # current date and time
    
    list_dates = []
    list_dates_1 = []
    for x in range(0, 7):
        d1 = d.strftime("%d/%m/%Y")
        list_dates.append(d1)
        list_dates_1.append(d)
        d = d - timedelta(days=1)
    
    list_dates.sort()
    data = []


    for censista in censistas:
        dictionary =  dict()

        dictionary["name"] = censista.get_full_name()

        lista_arboles_por_censistas = []
        for fecha in list_dates_1:
            
            cantidad_arboles = Arbol.objects.filter(habilitado = True, creado__date = fecha, creado_por__cedula_usuario = censista.username).count()
            #print("fecha ", fecha,  Arbol.objects.filter(habilitado = True, creado__date = fecha, creado_por__Grupo = usuario.Grupo).count())
            lista_arboles_por_censistas.append(cantidad_arboles)

        # Por ahora está con números aleatorios entre 20 y 80
        #dictionary["data"] = [random.randint(20,100) for _ in range(7)]
        dictionary["data"] = lista_arboles_por_censistas

        data.append(dictionary)

    list_dates = dumps(list_dates)
    data = dumps(data)

    return render(request, 'supervisor.html', {'usuario': usuario, 'numero_censistas':censistas.count(),
                                               'numero_formularios': numero_formularios, "censistas": censistas, 'data':data , 'list_dates': list_dates})


# Pagina principal para usuario Supervisor Forestal
@permission_required("usuarios.SuperForestal" , login_url="/")
def supervisor_forestal_home(request , usuario):
    return render(request, 'supervisor_forestal.html', {'usuario': usuario})


# Vista cambiar contraseña
@login_required
def cambiar_contrasena(request):
    usuario = Usuario.objects.get(username=request.user.username)
    mensaje = ""
    llamarMensaje = ""
    pestana = "perfil"


    retornarvista_segun_rol = "cambiar_contrasena_"+ usuario.rol + ".html"

    # Cambiar contraseña
    if request.method == 'POST' and "btnCambiarContrasena" in request.POST:
        
        print("entró post con btnCambiarContrasena")
        contrasenaAntigua = request.POST["currentPassword"]
        contrasenaNueva = request.POST["newPassword"]
    
        pestana = "contrasena"

        if not usuario.check_password(contrasenaAntigua):
            mensaje = "La contraseña antigua no es igual a la registrada en el sistema"
            llamarMensaje = "fracaso_usuario"
            

        else:
            usuario.set_password(contrasenaNueva)
            
            try:
                usuario.save()
            except Exception as e:
                print(e)
            user = authenticate(username=usuario.username, password=contrasenaNueva)
            login(request, user)
        
            mensaje = "Se registro el cambio sactisfactoriamente"
            llamarMensaje = "exito_usuario"

    # Cambiar datos personales de los usuarios 
    elif request.method == 'POST' and "btnCambiarPerfil" in request.POST:
        #Implementar mañana viernes
        usuario.first_name =  request.POST["nombre"] 
        usuario.last_name =  request.POST["apellidos"]
        usuario.direccion = request.POST["address"]
        usuario.telefono = request.POST["phone"]
        usuario.email = request.POST["email"]
        pestana = "editar_perfil"


        if 'imagenperfil' in request.POST:
            print("imagen antigua") 

        else: 
            if request.FILES['imagenperfil']:
                usuario.foto = request.FILES['imagenperfil']
            else:
                print("imagen antigua") 
            
        usuario.email = request.POST["email"]
        
        try:
            usuario.save()
        except Exception as e:
            print(e)
        
        mensaje = "Se actualizaron los datos sactisfactoriamente"
        llamarMensaje = "exito_usuario"
    else:
        print("get")

        if "mensaje" in request.session.keys():
            del request.session["mensaje"]

        if "llamarMensaje" in request.session.keys():
            del request.session["llamarMensaje"]

      
    return render(request, retornarvista_segun_rol, {'usuario': usuario, "mensaje": mensaje,  "llamarMensaje": llamarMensaje , "pestana": pestana })


# Vista para editar usuario por parte del administrador y(/)
@permission_required("usuarios.Administrador" , login_url="/")
def editar_usuario(request , username=None):
    usuario = Usuario.objects.get(username=request.user.username)
    llamarMensaje = ""
    mensaje = ""

    try:
        usuario_editar = Usuario.objects.get(username=username)
    except Usuario.DoesNotExist:
        llamarMensaje ="fracaso_usuario"
        mensaje = "El usuario "+str(username)+" No existe en el sistema"
        request.session["llamarMensaje"] = llamarMensaje
        request.session["mensaje"] = mensaje
        request.session["funcion_llamada"] = "editar_usuario"
        return redirect("listar_usuarios_administrador")


    if request.method == 'POST' and 'btnactivarUsuario' in request.POST:

        if request.POST["rol"] == "NoAsignado":

            llamarMensaje ="fracaso_usuario"
            mensaje = "No asignado Rol al Usuario"

 
        else:

            rol = request.POST["rol"]
            grupo = request.POST["grupo"]
            activo = False
            if "usuario_active" in request.POST:
                activo = True

                
            usuario_editar.is_staff = activo
            usuario_editar.Grupo = grupo
            
            usuario_editar.user_permissions.clear()

            # Modificando los roles de usuario
            usuario_editar.rol = rol
            content_type = ContentType.objects.get_for_model(Usuario)
            permission = Permission.objects.get(
            codename=rol,
            content_type=content_type,)
            usuario_editar.user_permissions.add(permission)


            try:
                usuario_editar.save()
            except Exception as e:
                print(e)
            llamarMensaje ="exito_usuario"
            mensaje = "El usuario "+str(usuario_editar.first_name) +" se cambió con exito"
            request.session["llamarMensaje"] = llamarMensaje
            request.session["mensaje"] = mensaje
            request.session["funcion_llamada"] = "editar_usuario"
            return redirect("listar_usuarios_administrador")


    return render(request, 'editar_usuario_Administrador.html', {'usuario_editar':usuario_editar,'usuario': usuario,'llamarMensaje': llamarMensaje,'mensaje': mensaje})

# Método retornar_vista, recibe el requets y según el rol del usuario autenticado, este retorna la vista o tmeplate correspondiente.
def retornar_vista(request, usuario):
    if usuario.has_perm("usuarios.Administrador"):
        return administrador_home(request, usuario)
    elif usuario.has_perm("usuarios.Censista"):
        return censista_home(request, usuario)
    elif usuario.has_perm("usuarios.Supervisor"):
      return supervisor_home(request, usuario)
    elif usuario.has_perm("usuarios.SuperForestal"):
      return supervisor_forestal_home(request, usuario)
    return render(request, 'login.html', {'usuario': usuario})



#Página de la vista de prinicpal del login de la aplicación
def login_view(request):
    
    mensaje = ""
    llamarMensaje = ""
    
    if request.session.get('tipoMensaje', False):
        try:
            mensaje = request.session["mensaje"]
            llamarMensaje = request.session["llamarMensaje"]

        except Exception as e:
            mensaje = ""
            llamarMensaje = ""

    if request.user.is_authenticated and not request.user.is_superuser:
        usuario = Usuario.objects.get(username=request.user.username)

        return retornar_vista(request, usuario)


    # Cuando se presiona el Botón autenticar desde la ventana login
    elif request.method == 'POST' and 'btnlogin' in request.POST:
        form = FormularioLogin(request.POST)
        if form.is_valid():

            cd = form.cleaned_data
            
            # Verificando que el usuario exista
            if User.objects.filter(username=cd['usuario']).exists():
                user = authenticate(username=cd['usuario'], password=cd['password']) 
                if user is not None:
                    if user.is_staff:
                        login(request, user)
                        #Redireccionar
                        usuario =  Usuario.objects.get(username=request.user.username)
                        return retornar_vista(request, usuario)
                    else:
        
                        mensaje = "Usuario no activado, comuniquese con el Administrador"
                        llamarMensaje = "fracaso_usuario"
                else:

                        mensaje = "Contraseña incorrecta"
                        llamarMensaje = "fracaso_usuario"
            else:
                   mensaje = "El usuario "+ str(cd['usuario'])+ " no existe"
                   llamarMensaje = "fracaso_usuario"
    form = FormularioLogin()
    
    request.session["tipoMensaje"] = False

    return render(request, 'login.html', {'mensaje': mensaje, 'form': form, 'llamarMensaje': llamarMensaje})


#Página de la vista de prinicpal del login de la aplicación
def registro_usuario_view(request):

    mensaje = ""
    llamarMensaje = ""

    #Verificación para crear un solo usuario
    if request.method == 'POST' and "btncreate" in request.POST:
        form = FormularioRegistroUsuario(request.POST)

        #Si el formulario es valido y tiene datos
        if form.is_valid():
            
            # Comprobamos si el usuario a crear, es el administradpr
            if not Usuario.objects.exists():

                usuario_administrador = Usuario()
                crear_usuario(usuario_administrador, form)
                
                print("creando usuario administrador")
                
                usuario_administrador.is_staff = True
                usuario_administrador.Grupo = 1
                # Modificando los roles de usuario
                usuario_administrador.rol = "Administrador"
                

#                content_type = ContentType.objects.get_for_model(Usuario)
                permission = Permission.objects.get( codename="Administrador")

                usuario_administrador.user_permissions.add(permission)


                try:
                    usuario_administrador.save()
                except Exception as e:
                    print(e)
                
                mensaje = "Usuario administrador creado correctamente, puede iniciar sesión"
                llamarMensaje = "info_usuario"
                request.session["llamarMensaje"] = llamarMensaje
                request.session["mensaje"] = mensaje
                request.session["tipoMensaje"] = True

                return redirect('login')
            
            #Capture la cedula del usuario
            cedula_usuario = form.cleaned_data["usuario"]
            
            
            #Consultando el usuario en la base de datos.            
            existe_usuario = Usuario.objects.filter(username=cedula_usuario).exists()
            #print("existe el usuario" + str(usuario))
            #print(usuario)
            if not existe_usuario:
                usuario = Usuario()
                print("creando usuario " + str(cedula_usuario))
                crear_usuario(usuario, form)
                mensaje = "El usuario se guardo correctamente, debe esperar su activación por parte del administrador"
                llamarMensaje = "info_usuario"
                request.session["llamarMensaje"] = llamarMensaje
                request.session["mensaje"] = mensaje
                request.session["tipoMensaje"] = True


                return redirect('login')

            # Si el usuario ya existe en la BD y esta activo
            else:
                
                mensaje = "El usuario " + str(cedula_usuario)  + " ya esta registrado"
                print(mensaje)
                llamarMensaje = "fracaso_usuario"
                form = FormularioRegistroUsuario()

                return render(request, 'registro_usuario.html',{'mensaje': mensaje, 'form': form, 'llamarMensaje': llamarMensaje})
            
        else:
            print("No valido  formulario de registro")

        #si no es valido el formulario crear
            
    form = FormularioRegistroUsuario()
    
    return render(request, 'registro_usuario.html',{'mensaje': mensaje, 'form': form, 'llamarMensaje': llamarMensaje})


#Vista para salir de la aplicación
def custom_logout(request):
    logout(request)
    return redirect("login")


#Metodo auxiliar para crear un usuario en la apliación atraves de los datos obtenidos de un formulario.
def crear_usuario(usuario, form):
    usuario.cedula_usuario = form.cleaned_data["usuario"]
    usuario.first_name = form.cleaned_data["nombres"]
    usuario.last_name = form.cleaned_data["apellidos"]
    usuario.email = form.cleaned_data["correo"]
    usuario.username = form.cleaned_data["usuario"]
    usuario.direccion = ""
    usuario.telefono = 0
 
    
    usuario.is_active = True
    usuario.is_staff = False
    #generando el password aleatorio.
    password = form.cleaned_data["password"]
    usuario.set_password(password)

    
    #Crea el usuario en la BD s i hay excepcion
    try:
        usuario.save()
    except Exception as e:
        print(e)

    
    
#Vista que permite al usuario supervisor   listar  los censistas que pertenecen a su grupo .
@permission_required("usuarios.Supervisor", login_url="/")
def listar_censistas_supervisor(request):
    usuario = Usuario.objects.get(username=request.user.username)
    censistas = Usuario.objects.filter(rol="Censista", Grupo=usuario.Grupo)
    
    llamarMensaje = ""
    mensaje = ""

    return render(request, 'listar_censistas_supervisor.html', {'usuario': usuario, 'usuarios': censistas,'llamarMensaje': llamarMensaje,'mensaje': mensaje})
    

#Vista que permite al usuario administrador listar  los usuarios de la Base de Datos.
@permission_required("usuarios.Administrador", login_url="/")
def listar_usuarios_administrador(request):
    usuario = Usuario.objects.get(username=request.user.username)
    usuarios = Usuario.objects.filter()

    llamarMensaje = ""
    mensaje = ""
    
    funcion_llamada = request.session.get('funcion_llamada', 'No')

    if funcion_llamada == "editar_usuario":
   
        llamarMensaje = request.session["llamarMensaje"] 
        mensaje = request.session["mensaje"]
        del request.session['funcion_llamada']

    return render(request, 'listar_usuarios_administrador.html', {'usuario': usuario, 'usuarios': usuarios,'llamarMensaje': llamarMensaje,'mensaje': mensaje})
