function generate_bootstrap_modal(titulo, texto) {
  div_modal = document.createElement("div");
  div_modal.className = "modal";
  div_modal.setAttribute("tabindex", "-1");
  div_modal_dialog = document.createElement("div");
  div_modal_dialog.className = "modal-dialog";
  div_modal_content = document.createElement("div");
  div_modal_content.className = "modal-content";
  div_modal_header = document.createElement("div");
  div_modal_header.className = "modal-header";
  div_modal_title = document.createElement("h5");
  div_modal_title.className = "modal-title";
  div_modal_title.innerHTML = titulo;
  div_modal_header.appendChild(div_modal_title);
  div_modal_header_btn_close = document.createElement("button");
  div_modal_header_btn_close.className = "btn-close";
  div_modal_header_btn_close.setAttribute("data-bs-dismiss", "modal");
  div_modal_header_btn_close.setAttribute("aria-label", "Cerrar");
  div_modal_header.appendChild(div_modal_header_btn_close);
  div_modal_content.appendChild(div_modal_header);
  div_modal_body = document.createElement("div");
  div_modal_body.className = "modal-body";
  div_modal_body_p = document.createElement("p");
  div_modal_body_p.innerHTML = texto;
  div_modal_body.appendChild(div_modal_body_p);
  div_modal_content.appendChild(div_modal_body);
  div_modal_footer = document.createElement("div");
  div_modal_footer.className = "modal-footer";
  div_modal_footer_btn_close = document.createElement("button");
  div_modal_footer_btn_close.className = "btn btn-secondary";
  div_modal_footer_btn_close.setAttribute("data-bs-dismiss", "modal");
  div_modal_footer_btn_close.innerHTML = "Cancelar";
  div_modal_footer.appendChild(div_modal_footer_btn_close);
  div_modal_footer_btn_save = document.createElement("button");
  div_modal_footer_btn_save.className = "btn btn-primary";
  div_modal_footer_btn_save.innerHTML = "Ok";
  div_modal_footer.appendChild(div_modal_footer_btn_save);
  div_modal_content.appendChild(div_modal_footer);
  div_modal_dialog.appendChild(div_modal_content);
  div_modal.appendChild(div_modal_dialog);
  return div_modal;
}

window.onload = function () {
  horas = document.getElementById("horas");
  if (horas) {
    // document.getElementById("horas").value = 0;
    document.getElementById("horas").oninput = function () {
      let valor = document.getElementById("horas").value;
      console.log(valor);
      document.getElementById("horas_value").innerHTML = valor;
    };
  }
};
