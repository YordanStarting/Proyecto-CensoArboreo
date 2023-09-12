
/*--------------------------------------------------------------
# Seleccionar estado del registro pag 1
--------------------------------------------------------------*/
function validacionCtr()
{

    //var value = JSON.parse(document.getElementById('hello-data').textContent);
    var newpassword = document.getElementById("newpassword").value;


    var renewpassword = document.getElementById("renewpassword").value;


    if (newpassword == renewpassword){
        return true;
        
    }else{
        swal('Contraseñas incorrectas','Las contraseñas no coinciden','error')
        return false;
    }

}



/* -----------FUNCION OCULTAR CAMPOS------------- */
/*--------------------------------------------------------------
# Seleccionar estado del registro pag 1
--------------------------------------------------------------*/
function otros() {
    /* Hola mundo*/
    var checkbox = document.getElementById("otros_control_fitosanitario");
    if (checkbox.checked) {
        document.getElementById("otros_coment").style.display = "block";
    } else {
        document.getElementById("otros_coment").style.display = "none";
    }
}
/*--------------------------------------------------------------
# Seleccionar estado del registro pag 1
--------------------------------------------------------------*/
function estadoRegistro() {
    /* Hola mundo*/
    var estadoRegistro = document.getElementById("estado_registro");
    estadoRegistro = estadoRegistro.options[estadoRegistro.selectedIndex].value;
    if (estadoRegistro == "Antiguo") {
        document.getElementById("antigua_placa").style.display = "block";
    }
    else{
        document.getElementById("antigua_placa").style.display = "none";
    }
}
/*--------------------------------------------------------------
# Seleccionar estado del Confinamiento pag 2
--------------------------------------------------------------*/
function estadoConfinamiento() {
    /* Hola mundo*/
    var Confinamiento = document.getElementById("confinamiento");
    Confinamiento = Confinamiento.options[Confinamiento.selectedIndex].value;
    if (Confinamiento == "si") {
        document.getElementById("formView").style.display = "block";
    }
    else{
        document.getElementById("formView").style.display = "none";
    }
}
/*--------------------------------------------------------------
# Seleccionar numero de tallos en la pag 3
--------------------------------------------------------------*/
    function fuste_polifurcado() {
        var ocultarfuste = document.getElementById("numero_tallos");
        ocultarfuste = ocultarfuste.options[ocultarfuste.selectedIndex].value;
        if (ocultarfuste == "1") {
            document.getElementById("fuste1").style.display = "block";
            document.getElementById("fuste2").style.display = "none";
            document.getElementById("fuste3").style.display = "none";
            document.getElementById("fuste4").style.display = "none";
            document.getElementById("fuste5").style.display = "none";



            
        }
        else if (ocultarfuste == "2") {
            document.getElementById("fuste1").style.display = "block";
            document.getElementById("fuste2").style.display = "block";
            document.getElementById("fuste3").style.display = "none";
            document.getElementById("fuste4").style.display = "none";
            document.getElementById("fuste5").style.display = "none";
        }
        else if (ocultarfuste == "3") {
            document.getElementById("fuste1").style.display = "block";
            document.getElementById("fuste2").style.display = "block";
            document.getElementById("fuste3").style.display = "block";
            document.getElementById("fuste4").style.display = "none";
            document.getElementById("fuste5").style.display = "none";
        }
        else if (ocultarfuste == "4") {
            document.getElementById("fuste1").style.display = "block";
            document.getElementById("fuste2").style.display = "block";
            document.getElementById("fuste3").style.display = "block";
            document.getElementById("fuste4").style.display = "block";
            document.getElementById("fuste5").style.display = "none";
        }
        else if (ocultarfuste == "5") {
            document.getElementById("fuste1").style.display = "block";
            document.getElementById("fuste2").style.display = "block";
            document.getElementById("fuste3").style.display = "block";
            document.getElementById("fuste4").style.display = "block";
            document.getElementById("fuste5").style.display = "block";
        }

    }
/*--------------------------------------------------------------
# Checkbox de la pag 3
--------------------------------------------------------------*/
function formFusteUnico(){
    var table = document.getElementById("formViewUnico");
    table.style.display = "block";

    var table1 = document.getElementById("formViewPolifurcado");
    table1.style.display = "none"
}

function formFusteFolicurcado(){
    var table = document.getElementById("formViewUnico");
    table.style.display = "none";

    var table = document.getElementById("formViewPolifurcado");
    table.style.display = "block";


    
}
/*--------------------------------------------------------------
# Ocultar confinamiento pag 2
--------------------------------------------------------------*/
/*
function formView(){
    var table = document.getElementById("formView");
    table.style.display = "block";
}

function formNone(){
    var table = document.getElementById("formView");
    table.style.display = "none";
}

/*--------------------------------------------------------------
# Ocultar selects pag 4
--------------------------------------------------------------*/

function hidde4(){
    var table = document.getElementById("form4");
    table.style.display = "none";

    var table = document.getElementById("form5");
    table.style.display = "block";


    var table = document.getElementById("boton4");
    table.style.display = "none";

    var table = document.getElementById("boton5");
    table.style.display = "block";

    
}


function tipoVitalidad(){

    var valorvitalidad = document.getElementById("talamuerto");
    valorvitalidad.
    if 

    var table = document.getElementById("talamuerto");
    table.style.display = "block"; 


}

//***************************************************** VALIDACIONES ************************************************************** */

//Formulario 1
function formshidde(){
    const placaAntigua = document.getElementById("placa_antigua")
    const estadoRegistro = document.getElementById("estado_registro")
    const selectRegistro = estadoRegistro.options[estadoRegistro.selectedIndex]
    const selectValue = selectRegistro.value

  
    if (selectValue == "Antiguo") {
        console.log("Entró a la validación");
        if( placaAntigua.value < 1 || placaAntigua.value % 1 !== 0){
            console.log("Placa antigua es inválida");
            placaAntigua.className+=' is-invalid ';
            swal('Digite la Placa Antigua','Debe ingresar un dígito de QR válido debe ser mayor a 1 y entero','error')
            return false;
        }else{       
          console.log("Placa antigua es válida");
      
          placaAntigua.classList.remove('is-invalid');
          placaAntigua.className+=' is-valid ';
          

          
        }
        
    }
    
   /* var RE = /^\d*(\.\d{1})?\d{0,1}$/
    /*   Agregue una condicional para validar el formulario  Placa antigua solo se pueden digitar 10 numeros   */


        var table = document.getElementById("form1");
        table.style.display = "none";
    
        var table = document.getElementById("form2");
        table.style.display = "block";
    
    
        var table = document.getElementById("boton1");
        table.style.display = "none";
    
        var table = document.getElementById("boton2");
        table.style.display = "block";
    
     

}

function deleteInValid(){
    const placaAntigua = document.getElementById("placa_antigua");
    const qr = document.getElementById('qr');
    const Confinamiento = document.getElementById("dist_confinamiento");
    var comercial = document.getElementById('comercial_fuste');
    var totalarbol = document.getElementById('totalarbol');
    const ejemayor = document.getElementById('ejemayor');
    const ejemenor = document.getElementById('ejemenor');
    const copa_viva = document.getElementById('copa_viva');
    const copa_ausente = document.getElementById('copa_ausente');
    placaAntigua.classList.remove('is-invalid');
    qr.classList.remove('is-invalid');
    Confinamiento.classList.remove('is-invalid');
    comercial.classList.remove('is-invalid');
    totalarbol.classList.remove('is-invalid');
    ejemayor.classList.remove('is-invalid');
    ejemenor.classList.remove('is-invalid');
    copa_viva.classList.remove('is-invalid');
    copa_ausente.classList.remove('is-invalid');
    placaAntigua.classList.remove('is-valid');
    qr.classList.remove('is-valid');
    Confinamiento.classList.remove('is-valid');
    comercial.classList.remove('is-valid');
    totalarbol.classList.remove('is-valid');
    ejemayor.classList.remove('is-valid');
    ejemenor.classList.remove('is-valid');
    copa_viva.classList.remove('is-valid');
    copa_ausente.classList.remove('is-valid');
}

function text_invalid(){
    const area_Invalid = document.getElementById("comentarios_otros");
    const porqueTala = document.getElementById("porquetala");

    area_Invalid.classList.remove('is-invalid');
    area_Invalid.classList.remove('is-valid');
    porqueTala.classList.remove('is-invalid');
    porqueTala.classList.remove('is-valid');
}

function capa_invalid(){
    const Cap = document.getElementById('cap');
    const Cap1 = document.getElementById('capa1');
    Cap.classList.remove('is-invalid');
    Cap1.classList.remove('is-invalid');
    Cap.classList.remove('is-valid');
    Cap1.classList.remove('is-valid');
}
function capa_invalid1(){
    const Cap2 = document.getElementById('capa2');
    Cap2.classList.remove('is-invalid');
    Cap2.classList.remove('is-valid');
}


function capa_invalid2(){
    const Cap3 = document.getElementById('capa3');
    Cap3.classList.remove('is-invalid');
    Cap3.classList.remove('is-valid');
}

function capa_invalid3(){
    const Cap4 = document.getElementById('capa4');
    Cap4.classList.remove('is-invalid');
    Cap4.classList.remove('is-valid');
}

function capa_invalid4(){
    const Cap5 = document.getElementById('capa5');
    Cap5.classList.remove('is-invalid');
    Cap5.classList.remove('is-valid');
}


//Formulario 2
function formshidde2(){

    let qr = document.getElementById('qr');
    //const confinamiento-radio = document.getElementById('radio2');
    const avatar = document.getElementById('avatar');
    const avatar2 = document.getElementById('avatar2');
    const delet = document.getElementById('delet');
    const dist_confinamiento = document.getElementById("dist_confinamiento")
    const Confinamiento = document.getElementById("confinamiento")
    const selectConfinamiento = Confinamiento.options[Confinamiento.selectedIndex]
    const ValueConfinamiento = selectConfinamiento.value
    
   

    /* -------- VALIDACION DE RADIO BUTTONS ---------------------- */
  

    if( qr.value < 1 || qr.value % 1 !== 0){
        qr.className+=' is-invalid ';
        swal('Digite el código QR','Debe ingresar un dígito de QR válido debe ser mayor a 1 y entero','error')
        return false;
    }else{
    
      delet.classList.remove('delet');
      qr.classList.remove('is-invalid');
      qr.className+=' is-valid ';
     
    }


    if (ValueConfinamiento == "si") {
        console.log("Entró a la validación");
        if( parseFloat(dist_confinamiento.value) < 1 || dist_confinamiento.value==""){
            console.log("* Confinamiento es inválida *");
            dist_confinamiento.className+=' is-invalid ';
            swal('Digite Confinamiento','Debe ingresar un dígito válido','error')
            return false;
        }else{       
          console.log("dist_confinamiento es válida");
      
          dist_confinamiento.classList.remove('is-invalid');
          dist_confinamiento.className+=' is-valid ';
          

          
        }
        
    }
   

    /* -------------------------------------------------- ----------------*/



    if( avatar.value === '' ){
        swal('IMAGEN 1','Seleccione de ingresar una imagen del árbol','error')
        avatar.className+=' is-invalid ';
        return false
    }else{
      delet.classList.remove('delet');
      avatar.classList.remove('is-invalid');
      avatar.className+=' is-valid ';
    }

    if( avatar2.value === '' ){
        swal('IMAGEN 2','Seleccione de ingresar una imagen del árbol','error')
        avatar2.className+=' is-invalid ';
        return false
    }else{
      delet.classList.remove('delet');
      avatar2.classList.remove('is-invalid');
      avatar2.className+=' is-valid ';
    }
    
    
    var table = document.getElementById("form2");
    table.style.display = "none";

    var table = document.getElementById("form3");
    table.style.display = "block";



    var table = document.getElementById("boton2");
    table.style.display = "none";

    var table = document.getElementById("boton3");
    table.style.display = "block";

    
}

//Formulario 3
function formshidde3(){

    var comercial = document.getElementById('comercial_fuste');
    var totalarbol = document.getElementById('totalarbol');
    const ejemayor = document.getElementById('ejemayor');
    const ejemenor = document.getElementById('ejemenor');
    const copa_viva = document.getElementById('copa_viva');
    const copa_ausente = document.getElementById('copa_ausente');
    const delet = document.getElementById('delet');
    const fusteUnico = document.getElementById('fuste_unico');
    const poliPolifurcado = document.getElementById('poli_polifurcado');
    const Cap = document.getElementById('cap');
    const Cap1 = document.getElementById('capa1');
    const Cap2 = document.getElementById('capa2');
    const Cap3 = document.getElementById('capa3');
    const Cap4 = document.getElementById('capa4');
    const Cap5 = document.getElementById('capa5');
    var numeroTallos = document.getElementById('numero_tallos');
   
    fusteUnico.addEventListener('change', () => {
        if (fusteUnico.checked) {
            Cap1.value = '';
            Cap2.value = '';
            Cap3.value = '';
            Cap4.value = '';
            Cap5.value = '';
            
        }
      });

      poliPolifurcado.addEventListener('change', () => {
        if (poliPolifurcado.checked) {
            Cap.value = '';
        }
      });

    /* -------- VALIDACION DE RADIO BUTTONS ---------------------- */
    
      /* Se valida el fuste unico, si esta chekeado entonces, se hace la validacion del input */
    if (fusteUnico.checked){
        

            if(Cap.value < 1 || Cap.value % 1 !== 0){

                Cap.className += ' is-invalid';
                swal('Ingresa un número valido en CAP ','','error')
                return false
            }else{
                delet.classList.remove('delet');
                Cap.classList.remove('is-invalid');
                Cap.className+=' is-valid '; 
            }
       
    }else{

        if(poliPolifurcado.checked){
         
            if (numeroTallos.value === "2"){
                if(Cap1.value < 1 || Cap1.value % 1 !== 0){

                    Cap1.className += ' is-invalid';
                    swal('Ingresa un número valido en CAP 1','','error')
                    return false
                }else{
                    delet.classList.remove('delet');
                    Cap1.classList.remove('is-invalid');
                    Cap1.className+=' is-valid ';  
                }
                if(Cap2.value < 1 || Cap2.value % 1 !== 0){
                    Cap2.className += ' is-invalid';
                    swal('Ingresa un número valido en CAP 2','','error')
                    return false
                }else{
                    delet.classList.remove('delet');
                    Cap2.classList.remove('is-invalid');
                    Cap2.className+=' is-valid ';  
                }        
            }
            else if(numeroTallos.value === "3"){
                if(Cap1.value < 1  || Cap1.value % 1 !== 0){
                    Cap1.className += ' is-invalid';
                    swal('Ingresa un número valido en CAP 1','','error')
                    return false
                }else{
                    delet.classList.remove('delet');
                    Cap1.classList.remove('is-invalid');
                    Cap1.className+=' is-valid ';  
                }
                if(Cap2.value < 1 || Cap2.value % 1 !== 0){
                    Cap2.className += ' is-invalid';
                    swal('Ingresa un número valido en CAP 2','','error')
                    return false
                }else{
                    delet.classList.remove('delet');
                    Cap2.classList.remove('is-invalid');
                    Cap2.className+=' is-valid ';  
                }
                if(Cap3.value < 1 || Cap3.value % 1 !== 0){
                    Cap3.className += ' is-invalid';
                    swal('Ingresa un número valido en CAP 3','','error')
                    return false
                }else{
                    delet.classList.remove('delet');
                    Cap3.classList.remove('is-invalid');
                    Cap3.className+=' is-valid ';  
                }
            }
            else if(numeroTallos.value === "4"){    
                if(Cap1.value < 1  || Cap1.value % 1 !== 0){
                    Cap1.className += ' is-invalid';
                    swal('Ingresa un número valido en CAP 1','','error')
                    return false
                }else{
                    delet.classList.remove('delet');
                    Cap1.classList.remove('is-invalid');
                    Cap1.className+=' is-valid ';  
                }
                if(Cap2.value < 1 || Cap2.value % 1 !== 0){
                    Cap2.className += ' is-invalid';
                    swal('Ingresa un número valido en CAP 2','','error')
                    return false
                }else{
                    delet.classList.remove('delet');
                    Cap2.classList.remove('is-invalid');
                    Cap2.className+=' is-valid ';  
                }
                if(Cap3.value < 1 || Cap3.value % 1 !== 0  ){
                    Cap3.className += ' is-invalid';
                    swal('Ingresa un número valido en CAP 3','','error')
                    return false
                }else{
                    delet.classList.remove('delet');
                    Cap3.classList.remove('is-invalid');
                    Cap3.className+=' is-valid ';  
                }
                if(Cap4.value < 1 || Cap4.value % 1 !== 0 ){
                    Cap4.className += ' is-invalid';
                    swal('Ingresa un número valido en CAP 4','','error')
                    return false
                }else{
                    delet.classList.remove('delet');
                    Cap4.classList.remove('is-invalid');
                    Cap4.className+=' is-valid ';  
                }
            }

            else if (numeroTallos.value === '5'){
                if(Cap1.value < 1 || Cap1.value % 1 !== 0 ){
                    Cap1.className += ' is-invalid';
                    swal('Ingresa un número valido en CAP 1','','error')
                    return false
                }else{
                    delet.classList.remove('delet');
                    Cap1.classList.remove('is-invalid');
                    Cap1.className+=' is-valid ';  
                }
                if(Cap2.value < 1 || Cap2.value % 1 !== 0 ){
                    Cap2.className += ' is-invalid';
                    swal('Ingresa un número valido en CAP 2','','error')
                    return false
                }else{
                    delet.classList.remove('delet');
                    Cap2.classList.remove('is-invalid');
                    Cap2.className+=' is-valid ';  
                }
                if(Cap3.value < 1 || Cap3.value % 1 !== 0){
                    Cap3.className += ' is-invalid';
                    swal('Ingresa un número valido en CAP 3','','error')
                    return false
                }else{
                    delet.classList.remove('delet');
                    Cap3.classList.remove('is-invalid');
                    Cap3.className+=' is-valid ';  
                }
                if(Cap4.value < 1 || Cap4.value % 1 !== 0){
                    Cap4.className += ' is-invalid';
                    swal('Ingresa un número valido en CAP 4','','error')
                    return false
                }else{
                    delet.classList.remove('delet');
                    Cap4.classList.remove('is-invalid');
                    Cap4.className+=' is-valid ';  
                }
                if(Cap5.value < 1 || Cap5.value % 1 !== 0){
                    Cap5.className += ' is-invalid';
                    swal('Ingresa un número valido en CAP 5','','error')
                    return false
                }else{
                    delet.classList.remove('delet');
                    Cap5.classList.remove('is-invalid');
                    Cap5.className+=' is-valid ';  
                }
            }
  
        }else{
            swal('Ingresa Forma del Tronco','','error')
            return false
        }
        
    }

    
    /* --------------------------------Validaciones de formulario 3 --------------------------- */


    if( parseFloat(comercial.value) < 1 || parseFloat(comercial.value) > 50 || comercial.value=="" ){
        swal('Comercial','comercial debe ser mayor a 1 y menor a 50','error')
        comercial.className+=' is-invalid ';
        return false;
    }else{
    
      delet.classList.remove('delet');
      comercial.classList.remove('is-invalid');
      comercial.className+=' is-valid ';
     
    }

    if( parseFloat(totalarbol.value) < 1 || parseFloat(totalarbol.value) > 50 || totalarbol.value=="" ){
        swal('Total Arbol','Total Arbol debe ser mayor a 1 y menor a 50','error')
        totalarbol.className+=' is-invalid ';
        return false;
    }else{
    
      delet.classList.remove('delet');
      totalarbol.classList.remove('is-invalid');
      totalarbol.className+=' is-valid ';
     
    }

    if( parseFloat(comercial.value) >= parseFloat(totalarbol.value) ){
        swal('TOTAL ARBOL','TOTAL ARBOL debe ser mayor a Comercial','error')
        comercial.className+=' is-invalid ';
        totalarbol.className+=' is-invalid ';
        return false;
    }else{
    
      delet.classList.remove('delet');
      comercial.classList.remove('is-invalid');
      comercial.className+=' is-valid ';
      totalarbol.classList.remove('is-invalid');
      totalarbol.className+=' is-valid ';
     
    }
    
    
     
    // Validacion de ejemenor y ejemayor
    
    /********************************************************************************************************** */
    if( parseFloat(ejemayor.value) < 1 || parseFloat(ejemayor.value) > 50 || ejemayor.value==""){
        swal('EJE MAYOR','Eje mayor debe ser mayor a 1 y menor a 50','error')
        ejemayor.className+=' is-invalid ';
        return false;
    }else{
    
      delet.classList.remove('delet');
      ejemayor.classList.remove('is-invalid');
      ejemayor.className+=' is-valid ';
     
    }

    if( parseFloat(ejemenor.value) < 1 || parseFloat(ejemenor.value) > 50 || ejemenor.value==""){
        swal('EJE MENOR','Eje menor debe ser mayor a 1 y menor a 50','error')
        ejemenor.className+=' is-invalid ';
        return false;
    }else{
    
      delet.classList.remove('delet');
      ejemenor.classList.remove('is-invalid');
      ejemenor.className+=' is-valid ';
     
    }

    if(  parseFloat(ejemenor.value) >= parseFloat(ejemayor.value) ){
        swal('EJE MAYOR','Eje mayor debe ser mayor a eje menor','error')
        ejemayor.className+=' is-invalid ';
        ejemenor.className+=' is-invalid ';
        return false;
    }else{
    
      delet.classList.remove('delet');
      ejemayor.classList.remove('is-invalid');
      ejemayor.className+=' is-valid ';
      ejemenor.classList.remove('is-invalid');
      ejemenor.className+=' is-valid ';
     
    }
    
    /********************************************************************************************************** */

    if( parseInt(copa_viva.value) < 1 || copa_viva.value=="" || copa_viva.value % 1 !== 0){
        swal('Copa Viva','Copa Viva debe ser mayor a 1 y menor a 50','error')
        copa_viva.className+=' is-invalid ';
        return false;
    }else{
    
      delet.classList.remove('delet');
      copa_viva.classList.remove('is-invalid');
      copa_viva.className+=' is-valid ';
     
    }

    if( copa_ausente.value < 1 || copa_ausente.value=="" || copa_ausente.value % 1 !== 0){
        swal('Copa Ausente','Copa Ausente debe ser mayor a 1 y menor a 101','error')
        copa_ausente.className+=' is-invalid ';
        return false;
    }else{
    
      delet.classList.remove('delet');
      copa_ausente.classList.remove('is-invalid');
      copa_ausente.className+=' is-valid ';
     
    }
    
    

   
    

    var table = document.getElementById("form3");
    table.style.display = "none";

    var table = document.getElementById("form4");
    table.style.display = "block";


    var table = document.getElementById("boton3");
    table.style.display = "none";

    var table = document.getElementById("boton4");
    table.style.display = "block";

    
}

// Formulario 4
function ocultar() {
    /* Se obtienen los datos del id en el select para identificar el tipo de rama si es buena o mala,
    Se hace una validacion para saber el valor del id en select, luego se establece un style.display dependiendo del valor y se oculta 
    o se muestran las tablas de contenido */
    var optionhidden = document.getElementById("vitalidad");
    optionhidden = optionhidden.options[optionhidden.selectedIndex].value;
    if (optionhidden == "Buena"   || optionhidden == "Mala" ) {
        document.getElementById("ocultar").style.display = "none";
    } else if (optionhidden == "Regular") {
        document.getElementById("ocultar").style.display = "block";
    }

    if (optionhidden == "Buena" || optionhidden == "Regular"){
        document.getElementById("controlfitosanitario_div").style.display = "block";
        document.getElementById("intervencion").style.display = "block";
        document.getElementById("talamuerto").style.display = "none";
    }else if(optionhidden == "Mala")
    {
        document.getElementById("controlfitosanitario_div").style.display = "none";
        document.getElementById("intervencion").style.display = "none";
        document.getElementById("talamuerto").style.display = "block";
    }



}



//***************************************************** Botones de anterior ************************************************************** */

/*--------------------------------------------------------------
# Anterior 2
--------------------------------------------------------------*/
function showanterior(){
    var table = document.getElementById("form2");
    table.style.display = "none";

    var table = document.getElementById("form1");
    table.style.display = "block";


    var table = document.getElementById("boton2");
    table.style.display = "none";

    var table = document.getElementById("boton1");
    table.style.display = "block";

}
/*--------------------------------------------------------------
# Anterior 3
--------------------------------------------------------------*/

function show3(){
    var table = document.getElementById("form3");
    table.style.display = "none";

    var table = document.getElementById("form2");
    table.style.display = "block";


    var table = document.getElementById("boton3");
    table.style.display = "none";

    var table = document.getElementById("boton2");
    table.style.display = "block";

}
/*--------------------------------------------------------------
# Anterior 4
--------------------------------------------------------------*/

function boton4(){
    var table = document.getElementById("form4");
    table.style.display = "none";

    var table = document.getElementById("form3");
    table.style.display = "block";


    var table = document.getElementById("boton4");
    table.style.display = "none";

    var table = document.getElementById("boton3");
    table.style.display = "block";

    
}

/*--------------------------------------------------------------
# Anterior 5
--------------------------------------------------------------*/
function boton5(){
    var table = document.getElementById("form4");
    table.style.display = "block";

    var table = document.getElementById("form5");
    table.style.display = "none";


    var table = document.getElementById("boton5");
    table.style.display = "none";

    var table = document.getElementById("boton4");
    table.style.display = "block";

    
    
}

/*--------------------------------------------------------------
# Habilitar Popovers
--------------------------------------------------------------*/
var popoverTriggerList = Array.prototype.slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl)
})

/*--------------------------------------------------------------
# Bloquear los botones de Popovers
--------------------------------------------------------------*/
var buttons = document.querySelectorAll('.info-button');
buttons.forEach(function(button) {
    button.addEventListener("click", function(event) {
        event.preventDefault();
      
    });
});




/*--------------------------------------------------------------
# Funcion para atraer las imagenes
--------------------------------------------------------------*/

 function getData(){
    let avatarInput = document.getElementById('avatar');
    let img = document.querySelector('label[for=avatar] img');

    avatarInput.onchange = async (e) => {
      
      img.classList.add('preview');
      img.src = URL.createObjectURL(e.target.files[0]);  
      
      console.log(img.offsetHeight, img.offsetWidth)
      
    }

    let avatarInput2 = document.getElementById('avatar2');
    let img2 = document.querySelector('label[for=avatar2] img');

    avatarInput2.onchange = async (e) => {
      
        img2.classList.add('preview');
        img2.src = URL.createObjectURL(e.target.files[0]);  
      
      console.log(img2.offsetHeight, img2.offsetWidth)
      
    }

    let avatarInput3 = document.getElementById('avatar3');
    let img3 = document.querySelector('label[for=avatar3] img');

    avatarInput3.onchange = async (e) => {
      
        img3.classList.add('preview');
        img3.src = URL.createObjectURL(e.target.files[0]);  
      
       console.log(img3.offsetHeight, img3.offsetWidth)
      
    }

    let avatarInput4 = document.getElementById('avatar4');
    let img4 = document.querySelector('label[for=avatar4] img');

    avatarInput4.onchange = async (e) => {
      
        img4.classList.add('preview');
        img4.src = URL.createObjectURL(e.target.files[0]);  
      
      console.log(img4.offsetHeight, img4.offsetWidth)
      
    }
}

document.getElementById("showImageButton").addEventListener("click", function() {
    // Obtén la URL de la imagen subida
    var imageUrl = document.querySelector('label[for=avatar] img').src;
    // Establece la URL de la imagen en el elemento de la imagen en el modal
    document.getElementById("modalImage").src = imageUrl;
    // Muestra el modal utilizando jQuery
    $("#imageModal").modal("show");
  });

  document.getElementById("showImageButton2").addEventListener("click", function() {
    // Obtén la URL de la imagen subida
    var imageUrl = document.querySelector('label[for=avatar2] img').src;
    // Establece la URL de la imagen en el elemento de la imagen en el modal
    document.getElementById("modalImage").src = imageUrl;
    // Muestra el modal utilizando jQuery
    $("#imageModal").modal("show");
  });

  document.getElementById("showImageButton3").addEventListener("click", function() {
    // Obtén la URL de la imagen subida
    var imageUrl = document.querySelector('label[for=avatar3] img').src;
    // Establece la URL de la imagen en el elemento de la imagen en el modal
    document.getElementById("modalImage").src = imageUrl;
    // Muestra el modal utilizando jQuery
    $("#imageModal").modal("show");
  });

  document.getElementById("showImageButton4").addEventListener("click", function() {
    // Obtén la URL de la imagen subida
    var imageUrl = document.querySelector('label[for=avatar4] img').src;
    // Establece la URL de la imagen en el elemento de la imagen en el modal
    document.getElementById("modalImage").src = imageUrl;
    // Muestra el modal utilizando jQuery
    $("#imageModal").modal("show");
  });


  $("#image-modal").on("show.bs.modal", function () {
    document.getElementById("modal-image").classList.add("zoom");
  });
  
  // quita la clase "zoom" del elemento de la imagen en la ventana modal cuando se cierra el modal
  $("#image-modal").on("hide.bs.modal", function () {
    document.getElementById("modal-image").classList.remove("zoom");
  });



  function validatePassword(password) {

    let currentPassword = document.getElementById("currentPassword");
    let new_Password = document.getElementById("newPassword");
    let renew_Password = document.getElementById("renewPassword");
    let isValid = true;
/*
    if (currentPassword.length < 8) {
        swal("La contraseña debe tener al menos 8 caracteres","","error");
      isValid = false;
    }

    if (new_Password.length < 8) {
        swal("La contraseña debe tener al menos 8 caracteres","","error");
      isValid = false;
    }

    if (!/[A-Z]/.test(new_Password)) {
        swal("La contraseña debe tener al menos una letra mayúscula","","error");
      isValid = false;
    }

    if (!/[a-z]/.test(new_Password)) {
        swal("La contraseña debe tener al menos una letra minúscula","","error");
      isValid = false;
    }

    if (!/\d/.test(new_Password)) {
        swal("La contraseña debe tener al menos un dígito","","error");
      isValid = false;
    }

    if (currentPassword  !== password ) {
        swal("La contraseña no es correcta","","error");
      isValid = false;
    }
*/
    if (new_Password.value != renew_Password.value) {
        renew_Password.className+=' is-invalid ';
        new_Password.className+=' is-invalid ';
        swal("La contraseña nueva y la confirmación de la contraseña no coinciden","","error");
        
        isValid = false;
    }


    return isValid;
  }

  var formulario_contrasena = document.getElementById("formulariocontrasena");


  if(!formulario_contrasena == null)
  {formulario_contrasena.addEventListener("submit", function(event) {
    if (!validatePassword()) {
      event.preventDefault();
    }
  });}


  function deleteInValidContrasena(){

    const newPassword = document.getElementById('newPassword');
    const renewPassword = document.getElementById('renewPassword');
    

    newPassword.classList.remove('is-invalid');
    renewPassword.classList.remove('is-invalid');


}

  const switchBtn = document.getElementById("switchBtn");
  
  if(!switchBtn == null){
  switchBtn.addEventListener("click", function() {
    // do something when switch is clicked
  });}

  

