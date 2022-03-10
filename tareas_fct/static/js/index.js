
window.onload = inicio;

function inicio() {
    console.log("hola")
    let boton = document.getElementById("insertar");
    let borrar = document.getElementById("borrar");
    boton.addEventListener("click", insertar);
};
function insertar() {
    console.log("ey");
    console.log(window.location.href);
    window.location.href = 'http://localhost:8000/insertar_tarea';
    console.log(window.location.href);
}

