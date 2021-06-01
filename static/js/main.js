// cerrar los avisos de las acciones de manera automatica
$(document).ready(function () {
  // show the alert
  setTimeout(function () {
    $(".alert").alert("close");
  }, 1500);
});

// alerta de eliminacion de registros
const btnDelete = document.querySelectorAll(".btn-delete");

if (btnDelete) {
  const btnArray = Array.from(btnDelete);
  btnArray.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      if (!confirm("¡¡¡ ¿Está seguro de eliminar este registro? !!!")) {
        e.preventDefault();
      }
    });
  });
}
