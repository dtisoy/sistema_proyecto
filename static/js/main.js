// cerrar los avisos de las acciones de manera automatica
$(document).ready(function() {
    // show the alert
    setTimeout(function() {
        $(".alert").alert('close');
    }, 1500);
});