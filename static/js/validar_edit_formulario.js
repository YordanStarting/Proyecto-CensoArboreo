otros()

function otros() {
    /* Hola mundo*/
    var checkbox = document.getElementById("otros_control_fitosanitario");
    if (checkbox.checked) {
        document.getElementById("otros_coment").style.display = "block";
    } else {
        document.getElementById("otros_coment").style.display = "none";
    }
}
 
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
    function fuste_polifurcado() {
        
        var ocultarfuste = document.getElementById("numero_tallos");
        ocultarfuste = ocultarfuste.options[ocultarfuste.selectedIndex].value;
       
        if (ocultarfuste == "2") {
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
    
    function estadoRegistr() {
        /* Hola mundo*/
        const placaAntigua = document.getElementById("placa_antigua")

        var estadoRegistro = document.getElementById("estado_registro");
        estadoRegistro = estadoRegistro.options[estadoRegistro.selectedIndex].value;

        if (estadoRegistro == "Nuevo"){
            placaAntigua.value=0;
        }

        if (estadoRegistro == "Antiguo") {
            document.getElementById("antigua_placa").style.display = "block";
        }
        else{
            document.getElementById("antigua_placa").style.display = "none";
        }
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

    function formshidde(){
        const vitalidad = document.getElementById("vitalidad");
        const selectVitalidad = vitalidad.options[vitalidad.selectedIndex];
        const vitalidadValue = selectVitalidad.value;
        const porqueTala = document.getElementById("porquetala");

        var otros = document.getElementById("comentarios_otros");
        var checkbox = document.getElementById("otros_control_fitosanitario");
        const placaAntigua = document.getElementById("placa_antigua");
        const estadoRegistro = document.getElementById("estado_registro");
        const selectRegistro = estadoRegistro.options[estadoRegistro.selectedIndex];
        const selectValue = selectRegistro.value;
        const qr = document.getElementById('qr');
        const avatar = document.getElementById('avatar');
        const avatar2 = document.getElementById('avatar2');
        const delet = document.getElementById('delet');
        const dist_confinamiento = document.getElementById("dist_confinamiento")
        const Confinamiento = document.getElementById("confinamiento")
        const selectConfinamiento = Confinamiento.options[Confinamiento.selectedIndex]
        const ValueConfinamiento = selectConfinamiento.value
        var comercial = document.getElementById('comercial_fuste');
        var totalarbol = document.getElementById('totalarbol');
        const ejemayor = document.getElementById('ejemayor');
        const ejemenor = document.getElementById('ejemenor');
        var copa_viva = document.getElementById('copa_viva');
        var copa_ausente = document.getElementById('copa_ausente');
        const fusteUnico = document.getElementById('fuste_unico');
        const poliPolifurcado = document.getElementById('poli_polifurcado');
        const Cap = document.getElementById('cap');
        const Cap1 = document.getElementById('capa1');
        const Cap2 = document.getElementById('capa2');
        const Cap3 = document.getElementById('capa3');
        const Cap4 = document.getElementById('capa4');
        const Cap5 = document.getElementById('capa5');
        var numeroTallos = document.getElementById('numero_tallos');
    
        console.log("VALIDATING");
       
        if (selectValue == "Antiguo") {
            
            console.log("Entró a la validación");
            if( placaAntigua.value < 1 || placaAntigua.value % 1 !== 0){
                console.log("Placa antigua es inválida");
                placaAntigua.className+=' is-invalid ';
                swal('Digite la Placa Antigua','Debe ingresar un dígito de Placa antigua válido debe ser mayor a 1 y entero','error')
                placaAntigua.focus();
                return false;
            }else{       
              console.log("Placa antigua es válida");
              placaAntigua.classList.remove('is-invalid');
              placaAntigua.className+=' is-valid ';
              
            }      
        }

        /* validacion */
        if( qr.value < 1 || qr.value % 1 !== 0){
            console.log("Entro en mala validacion")
            qr.className+=' is-invalid ';
            swal('Digite el código QR','Debe ingresar un dígito de QR válido debe ser mayor a 1 y entero','error')
            qr.focus();
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
                dist_confinamiento.focus();
                return false;
            }else{       
              console.log("dist_confinamiento es válida");
          
              dist_confinamiento.classList.remove('is-invalid');
              dist_confinamiento.className+=' is-valid ';
              
    
              
            }
            
        }


        fusteUnico.addEventListener('change', () => {
            if (fusteUnico.checked) {
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
            
    
                if(Cap.value < 1 || Cap.value=="" || Cap.value % 1 !== 0){
                    Cap.className += ' is-invalid';
                    swal('Ingresa un número valido en CAP ','','error')
                    Cap.focus();
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
                        Cap1.focus();
                        return false
                    }else{
                        delet.classList.remove('delet');
                        Cap1.classList.remove('is-invalid');
                        Cap1.className+=' is-valid ';  
                    }
                    if(Cap2.value < 1 || Cap2.value % 1 !== 0){
                        Cap2.className += ' is-invalid';
                        swal('Ingresa un número valido en CAP 2','','error')
                        Cap2.focus();
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
                        Cap1.focus();
                        return false
                    }else{
                        delet.classList.remove('delet');
                        Cap1.classList.remove('is-invalid');
                        Cap1.className+=' is-valid ';  
                    }
                    if(Cap2.value < 1 || Cap2.value % 1 !== 0){
                        Cap2.className += ' is-invalid';
                        swal('Ingresa un número valido en CAP 2','','error')
                        Cap2.focus();
                        return false
                    }else{
                        delet.classList.remove('delet');
                        Cap2.classList.remove('is-invalid');
                        Cap2.className+=' is-valid ';  
                    }
                    if(Cap3.value < 1 || Cap3.value % 1 !== 0){
                        Cap3.className += ' is-invalid';
                        swal('Ingresa un número valido en CAP 3','','error')
                        Cap3.focus();
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
                        Cap1.focus();
                        return false
                    }else{
                        delet.classList.remove('delet');
                        Cap1.classList.remove('is-invalid');
                        Cap1.className+=' is-valid ';  
                    }
                    if(Cap2.value < 1 || Cap2.value % 1 !== 0){
                        Cap2.className += ' is-invalid';
                        swal('Ingresa un número valido en CAP 2','','error')
                        Cap2.focus();
                        return false
                    }else{
                        delet.classList.remove('delet');
                        Cap2.classList.remove('is-invalid');
                        Cap2.className+=' is-valid ';  
                    }
                    if(Cap3.value < 1 || Cap3.value % 1 !== 0){
                        Cap3.className += ' is-invalid';
                        swal('Ingresa un número valido en CAP 3','','error')
                        Cap3.focus();
                        return false
                    }else{
                        delet.classList.remove('delet');
                        Cap3.classList.remove('is-invalid');
                        Cap3.className+=' is-valid ';  
                    }
                    if(Cap4.value < 1 || Cap4.value % 1 !== 0){
                        Cap4.className += ' is-invalid';
                        swal('Ingresa un número valido en CAP 4','','error')
                        Cap4.focus();
                        return false
                    }else{
                        delet.classList.remove('delet');
                        Cap4.classList.remove('is-invalid');
                        Cap4.className+=' is-valid ';  
                    }
                }
    
                else if (numeroTallos.value === '5'){
                    if(Cap1.value < 1 || Cap1.value % 1 !== 0){
                        Cap1.className += ' is-invalid';
                        swal('Ingresa un número valido en CAP 1','','error')
                        Cap1.focus();
                        return false
                    }else{
                        delet.classList.remove('delet');
                        Cap1.classList.remove('is-invalid');
                        Cap1.className+=' is-valid ';  
                    }
                    if(Cap2.value < 1 || Cap2.value % 1 !== 0){
                        Cap2.className += ' is-invalid';
                        swal('Ingresa un número valido en CAP 2','','error')
                        Cap2.focus();
                        return false
                    }else{
                        delet.classList.remove('delet');
                        Cap2.classList.remove('is-invalid');
                        Cap2.className+=' is-valid ';  
                    }
                    if(Cap3.value < 1 || Cap3.value % 1 !== 0){
                        Cap3.className += ' is-invalid';
                        swal('Ingresa un número valido en CAP 3','','error')
                        Cap3.focus();
                        return false
                    }else{
                        delet.classList.remove('delet');
                        Cap3.classList.remove('is-invalid');
                        Cap3.className+=' is-valid ';  
                    }
                    if(Cap4.value < 1 || Cap4.value % 1 !== 0){
                        Cap4.className += ' is-invalid';
                        swal('Ingresa un número valido en CAP 4','','error')
                        Cap4.focus();
                        return false
                    }else{
                        delet.classList.remove('delet');
                        Cap4.classList.remove('is-invalid');
                        Cap4.className+=' is-valid ';  
                    }
                    if(Cap5.value < 1 || Cap5.value % 1 !== 0){
                        Cap5.className += ' is-invalid';
                        swal('Ingresa un número valido en CAP 5','','error')
                        Cap5.focus();
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
    
    
        if( parseFloat(comercial.value) < 1 || parseFloat(comercial.value) > 50 || comercial.value==""){
            swal('Comercial','Comercial debe ser mayor a 1 y menor a 50','error')
            comercial.className+=' is-invalid ';
            comercial.focus();
            return false;
        }else{
        
          delet.classList.remove('delet');
          comercial.classList.remove('is-invalid');
          comercial.className+=' is-valid ';
         
        }
    
        if( parseFloat(totalarbol.value) < 1 || parseFloat(totalarbol.value) > 50 || totalarbol.value==""){
            swal('Total Arbol','Total Arbol debe ser mayor a 1 y menor a 50','error')
            totalarbol.className+=' is-invalid ';
            totalarbol.focus();
            return false;
        }else{
        
          delet.classList.remove('delet');
          totalarbol.classList.remove('is-invalid');
          totalarbol.className+=' is-valid ';
         
        }
    
        if( parseFloat(comercial.value) >= parseFloat(totalarbol.value)){
            swal('TOTAL ARBOL','TOTAL ARBOL debe ser mayor a Comercial','error')
            comercial.className+=' is-invalid ';
            totalarbol.className+=' is-invalid ';
            comercial.focus();
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
        if( ejemayor.value < 1 || ejemayor.value > 50 || ejemayor.value==""){
            swal('EJE MAYOR','Eje mayor debe ser mayor a 1 y menor a 50','error')
            ejemayor.className+=' is-invalid ';
            ejemayor.focus();
            return false;
            
        }else{
        
          delet.classList.remove('delet');
          ejemayor.classList.remove('is-invalid');
          ejemayor.className+=' is-valid ';
         
        }
    
        if( ejemenor.value < 1 || ejemenor.value > 50 || ejemenor.value==""){
            swal('EJE MENOR','Eje menor debe ser mayor a 1 y menor a 50','error')
            ejemenor.className+=' is-invalid ';
            ejemenor.focus();
            return false;
           
        }else{
        
          delet.classList.remove('delet');
          ejemenor.classList.remove('is-invalid');
          ejemenor.className+=' is-valid ';
         
        }
    
        if(  parseFloat(ejemenor.value) >= parseFloat(ejemayor.value) ){
            swal('EJE MAYOR','Eje mayor debe ser mayor a eje menor','error')
            ejemayor.className+=' is-invalid ';
            ejemayor.focus();
            return false;
            
        }else{
        
          delet.classList.remove('delet');
          ejemayor.classList.remove('is-invalid');
          ejemayor.className+=' is-valid ';
          ejemenor.classList.remove('is-invalid');
          ejemenor.className+=' is-valid ';
         
        }
        
        /********************************************************************************************************** */

        if( parseFloat(copa_viva.value) < 1 || copa_viva.value==""){
            swal('Copa Viva','Copa Viva debe ser mayor a 1 y menor a 50','error')
            copa_viva.className+=' is-invalid ';
            copa_viva.focus();
            return false;
          
        }else{
        
          delet.classList.remove('delet');
          copa_viva.classList.remove('is-invalid');
          copa_viva.className+=' is-valid ';
         
        }

        if( copa_ausente.value < 1 || copa_ausente.value >= 101 || copa_ausente.value=="" || copa_ausente.value % 1 !== 0){
            swal('Copa Ausente','Copa Ausente debe ser mayor a 1 y menor a 100','error')
            copa_ausente.className+=' is-invalid ';
            copa_ausente.focus();
            return false;
           
        }else{
        
          delet.classList.remove('delet');
          copa_ausente.classList.remove('is-invalid');
          copa_ausente.className+=' is-valid ';
         
        }
       
        
        if (vitalidadValue == "Mala") {
            swal('hola')
            if( porqueTala.value === ''){
                console.log("Parametro")
                porqueTala.className += ' is-invalid';
                swal('Ingresa caracteres validos en ¿Porqué Tala?','','error')
                return false
               
            }
            
            else{       
              aler("Placa antigua es válida");
              porqueTala.classList.remove('is-invalid');
              porqueTala.className+=' is-valid ';
              
            }      
        }else{
            console.log("valor")
        }

        if(checkbox.checked){
            if(otros.value === ''){
                otros.className += ' is-invalid';
                swal('Ingresa caracteres validos en Otra intervención fitosanitaria  ','','error')
                return false
               
            }
            
            else{
                delet.classList.remove('delet');
                otros.value .classList.remove('is-invalid');
                otros.value .className+=' is-valid '; 
            }
        }else{
            console.log("valor")
        }


       

    
    }

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


    

