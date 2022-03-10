
window.onload = inicio;

function inicio() {
    console.log("hola")
    let boton = document.getElementById("insertar");
    let logout = document.getElementById("logout");
    boton.addEventListener("click", insertar);
    logout.addEventListener("click", fuera);
};
function insertar() {
    console.log(window.location.href);
    window.location.href = 'http://localhost:8000/insertar_tarea';
    console.log(window.location.href);
}
function fuera() {
    console.log(window.location.href);
    window.location.href = 'http://localhost:8000/logout';
    console.log(window.location.href);
}

