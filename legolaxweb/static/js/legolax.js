/* Main tabs */
$(function(){ $("#principal").tabs({collapsible: true}); });

/* Dialogo para confirmar cambios */
$(document).ready(function(){
    // Formateamos el botón Diálogo sencillo
    $('#dialogSencillo').button();
    // Damos formato a la Ventana de Diálogo    
    $('#dialogo').dialog({
        // Indica si la ventana se abre de forma automática
        autoOpen: false,
        // Indica si la ventana es modal
        modal: true,
        // Largo
        width: 300,
        // Alto
        height: 160,
        // Creamos los botones
        buttons: {
            Confirmar: function() {
                // ir a una url
                //window.location.href="url";
                $('#formulario').submit();
            },
            Cancelar: function() {
                // Cerrar ventana de diálogo
                $(this).dialog( "close" );
            }
        }
    });
    // Mostrar Diálogo Sencillo
    $('#dialogSencillo').click(function(){
        $('#dialogo').dialog('open');
    });
});

//Desactivar el enter en los formularios
$(document).ready(function() {
    $("form").keypress(function(e) {
        if (e.which == 13) {
            return false;
        }
    });
});

//Personalizar el datepicker
$(function() {
		$( "#fentrega" ).datepicker( $.datepicker.regional[ "es" ],"option","dateFormat","dd/mm/yy" );
});
$(function() {
		$( "#id_fentrega" ).datepicker( $.datepicker.regional[ "es" ],"option","dateFormat","dd/mm/yy" );
});
$(function() {
		$( "#fregistro" ).datepicker( $.datepicker.regional[ "es" ],"option","dateFormat","dd/mm/yy" );
});
$(function() {
		$( "#id_fregistro" ).datepicker( $.datepicker.regional[ "es" ],"option","dateFormat","dd/mm/yy" );
});

//Validar el ingreso de DNI
$(document).ready(function() {
    $("#id_dni").keydown(function(event) {
        // Allow only backspace and delete
        if ( event.keyCode == 46 || event.keyCode == 8 ) {
            // let it happen, don't do anything
        }
        else {
			if(event.keyCode < 95){
				// Ensure that it is a number and stop the keypress
				if ((event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105 )) {
					event.preventDefault(); 
				}
            }
        }
    });
});
$(document).ready(function() {
    $("#dni").keydown(function(event) {
        // Allow only backspace and delete
        if ( event.keyCode == 46 || event.keyCode == 8 ) {
            // let it happen, don't do anything
        }
        else {
			if(event.keyCode < 95){
				// Ensure that it is a number and stop the keypress
				if ((event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105 )) {
					event.preventDefault(); 
				}
            }
        }
    });
});
