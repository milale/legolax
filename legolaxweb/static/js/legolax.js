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
