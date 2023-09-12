
/**
 * Created by jorge on 21/03/16.
 */

// [ DEMO ] GENERATE RANDOM ALERTS
	// =================================================================

function llamarMensajes	(llamada, mensaje){

	/// CARGAR MENSAJES DE  REGISTRO USUARIOS

	if("exito_usuario".localeCompare(llamada) == 0 ){

		swal('Censo Arboreo 2022',''+mensaje,'success')

	}else if("fracaso_usuario".localeCompare(llamada) == 0 )
	{
		swal('Censo Arboreo 2022',''+mensaje,'error')
	}
	else if("info_usuario".localeCompare(llamada) == 0 )
	{
		swal('Censo Arboreo 2022',''+mensaje,'info')
	}

}