var my_url = "/static/js/lista_genero_arboles.json"
//var datos_json = (function () { var json = null; $.ajax({ 'async': false, 'global': false, 'url': my_url, 'dataType': "json", 'success': function (data) { json = data; } }); return json; })();

///Fuente: https://www.iteramos.com/pregunta/71308/cargar-json-en-la-variable
function asignar_nombre_comun(){ 
    var nombre_comun;
    nombre_comun = document.getElementById("nombre_comun")[document.getElementById("nombre_comun").selectedIndex].value
    
    // Familia
    document.getElementById("familia").value=datos_json[nombre_comun][0]

    // Género
    document.getElementById("genero").value=datos_json[nombre_comun][1]

    // Nombre Científico
    document.getElementById("nombre_cientifico").value=datos_json[nombre_comun][2]


   /// document.getElementById("familia").options[i].text=datos_json["nombre_comun"][0]
  }

