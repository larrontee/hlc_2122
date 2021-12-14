import requests


class filmaffinity:
    def __init__(self, url):
        self.__resultado = {}
        self.__url = url
        self.__html = ""

    def set_url(url):
        self.__url = url

    def do_request():
        self.__html = requests.get(url)

    def __titulo_original(t):
        etiqueta_titulo = "<dt>Título original</dt>"
        pos_etiqueta_titulo = t.find(etiqueta_titulo)
        titulo = t[pos_etiqueta_titulo:]
        titulo = titulo[: titulo.find("</dd>")].splitlines()[2].lstrip().rstrip()
        titulo = titulo.split("<")
        titulo = titulo[0]
        return titulo

    def __anio(t):
        etiqueta_anio = "<dt>Año</dt>"
        pos_etiqueta_anio = t.find(etiqueta_anio)
        anio = t[pos_etiqueta_anio:]
        anio = anio[: anio.find("</dd>")].splitlines()[1].lstrip().rstrip()
        anio = anio[anio.find(">") + 1 :]
        return anio

    def __daraçao(t):
        etiqueta_duracion = "<dt>Duración</dt>"
        pos_etiqueta_duracion = t.find(etiqueta_duracion)
        duracion = t[pos_etiqueta_duracion:]
        duracion = duracion[: duracion.find("</dd>")].splitlines()[1].lstrip().rstrip()
        duracion = duracion[duracion.find(">") + 1 :]
        return duracion

    def __pais(t):
        etiqueta_pais = "<dt>País</dt>"
        pos_etiqueta_pais = t.find(etiqueta_pais)
        pais = t[pos_etiqueta_pais:]
        pais = pais[: pais.find("</dd>")].splitlines()[1].lstrip().rstrip()
        pais = pais.split(">")
        pais = pais[int(len(pais) - 1)]
        pais = pais.split(";")
        pais = pais[int(len(pais) - 1)]
        return pais

    def __direccion(t):
        etiqueta_direccion = "<dt>Dirección</dt>"
        pos_etiqueta_direccion = t.find(etiqueta_direccion)
        direccion = t[pos_etiqueta_direccion:]
        direccion = direccion.splitlines()[2]
        direccion = direccion.split(">")
        directores = ""
        for i in range(len(direccion) - 1):
            if direccion[i][0] != "<":
                directores += direccion[i]

        aux = directores.split("<")
        aux1 = ""
        for i in range(len(aux) - 1):
            if aux[i][0] != "/":
                aux1 += aux[i]

        return aux1

    def __guion(t):
        etiqueta_guion = "<dt>Guion</dt>"
        pos_etiqueta_guion = t.find(etiqueta_guion)
        guion = t[pos_etiqueta_guion + 14 :]
        guion = guion[: guion.find("</dd>")]
        guion == guion[guion.find('<span class="nb>') : guion.find("</div>")]
        guionistas = ""
        a = 0
        while guion.find("<span>") != -1:
            guion = guion[guion.find("<span>") + len("<span>") :]
            guionistas += guion[: guion.find("</span>")]
            if a != 0:
                guionistas += ", " + guion[: guion.find("</span>")]
            a += 1

        return guionistas

    def __musica(t):
        etiqueta_guion = "<dt>Música</dt>"
        pos_etiqueta_guion = t.find(etiqueta_guion)
        guion = t[pos_etiqueta_guion + 14 :]
        guion = guion[: guion.find("</dd>")]
        guion == guion[guion.find('<span class="nb>') : guion.find("</div>")]
        guionistas = ""
        a = 0
        while guion.find("<span>") != -1:
            guion = guion[guion.find("<span>") + len("<span>") :]
            guionistas += guion[: guion.find("</span>")]
            if a != 0:
                guionistas += " , " + guion[: guion.find("</span>")]
            a += 1

        return guionistas

    def __fotografia(t):
        etiqueta_guion = "<dt>Fotografía</dt>"
        pos_etiqueta_guion = t.find(etiqueta_guion)
        guion = t[pos_etiqueta_guion + 14 :]
        guion = guion[: guion.find("</dd>")]
        guion == guion[guion.find('<span class="nb>') : guion.find("</div>")]
        guionistas = ""
        a = 0
        while guion.find("<span>") != -1:
            guion = guion[guion.find("<span>") + len("<span>") :]
            guionistas += guion[: guion.find("</span>")]
            if a != 0:
                guionistas += " , " + guion[: guion.find("</span>")]
            a += 1
        return guionistas

    def __productora(t):
        etiqueta_guion = "<dt>Productora</dt>"
        pos_etiqueta_guion = t.find(etiqueta_guion)
        guion = t[pos_etiqueta_guion + 14 :]
        guion = guion[: guion.find("</dd>")]
        guion == guion[guion.find('<span class="nb>') : guion.find("</div>")]
        guionistas = ""
        a = 0
        while guion.find("<span>") != -1:
            guion = guion[guion.find("<span>") + len("<span>") :]
            guionistas += guion[: guion.find("</span>")]
            if a != 0:
                guionistas += " , " + guion[: guion.find("</span>")]
            a += 1
        return guionistas

    def __reparto(t):
        etiqueta_reparto = "<dt>Reparto</dt>"
        pos_etiqueta_reparto = t.find(etiqueta_reparto)
        reparto = t[pos_etiqueta_reparto:]
        reparto = reparto[: reparto.find("</dd>")]
        etiqueta_inicio = '<span itemprop="name">'
        etiqueta_cierre = "</span>"
        all_cast = ""
        a = 0
        while reparto.find(etiqueta_inicio) != -1:
            reparto = reparto[reparto.find(etiqueta_inicio) + len(etiqueta_inicio) :]
            all_cast += reparto[: reparto.find(etiqueta_cierre)]
            if a != 0:
                all_cast += " , " + reparto[: reparto.find(etiqueta_cierre)]
                a += 1
        return all_cast

    def __grupo(t):
        etiqueta_guion = "<dt>Grupos</dt>"
        pos_etiqueta_guion = t.find(etiqueta_guion)
        if pos_etiqueta_guion != -1:
            guion = t[pos_etiqueta_guion + 14 :]
            guion = guion[: guion.find("</dd>")]
            guion == guion[guion.find('<span class="nb>') : guion.find("</div>")]
            guionistas = ""
            a = 0
            while guion.find("<span>") != -1:
                guion = guion[guion.find("<span>") + len("<span>") :]
                guionistas += guion[: guion.find("</span>")]
                if a != 0:
                    guionistas += " , " + guion[: guion.find("</span>")]
                a += 1
            guionistas = guionistas.split(">")
            guionistas = guionistas[1].split("<")
            guionistas = guionistas[0]
            return guionistas
        return "No hay grupo"

    def __sinopsis(t):
        etiqueta_sinopsis = "<dt>Sinopsis</dt>"
        pos_etiqueta_sinopsis = t.find(etiqueta_sinopsis)
        descripcion = t[pos_etiqueta_sinopsis:]
        descripcion = descripcion[: descripcion.find("</dd>")]
        descripcion = descripcion.split(">")
        descripcion = descripcion[3]
        descripcion = descripcion.split("(")
        descripcion = descripcion[0]
        return descripcion

    def __procesar(self):

        self.__resultado = {
            "Titulo": self.__titulo_original(self.__html),
            "Año": self.__anio(self.__html),
            "Duracion": self.__daraçao(self.__html),
            "Pais": self.__pais(self.__html),
            "Direccion": self.__direccion(self.__html),
            "Guion": self.__guion(self.__html),
        }

        self.__musica(self.__html)
        self.__fotografia(self.__html)
        self.__productora(self.__html)
        self.__reparto(self.__html)
        self.__grupo(self.__html)
        self.__sinopsis(self.__html)
