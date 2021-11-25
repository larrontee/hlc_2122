import requests

# hasta sinopsis
# Terminator 2: The judgment day
# r = requests.get("https://www.filmaffinity.com/es/film576352.html")
# Monty Python's Life of Brian
# r = requests.get("https://www.filmaffinity.com/es/film612331.html")
r = requests.get("https://www.filmaffinity.com/es/film155187.html")
# r = requests.get("https://www.filmaffinity.com/es/film185733.html")
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
t = r.text

def titulo_original(t):
    etiqueta_titulo = "<dt>Título original</dt>"
    pos_etiqueta_titulo = t.find(etiqueta_titulo)
    titulo = t[pos_etiqueta_titulo:]
    titulo = titulo[: titulo.find("</dd>")].splitlines()[2].lstrip().rstrip()
    titulo = titulo.split("<")
    titulo = titulo[0]
    return titulo

def anio(t):
    etiqueta_anio = "<dt>Año</dt>"
    pos_etiqueta_anio = t.find(etiqueta_anio)
    anio = t[pos_etiqueta_anio:]
    anio = anio[: anio.find("</dd>")].splitlines()[1].lstrip().rstrip()
    anio = anio[anio.find(">") + 1 :]
    return anio


def daraçao(t):
    etiqueta_duracion = "<dt>Duración</dt>"
    pos_etiqueta_duracion = t.find(etiqueta_duracion)
    duracion = t[pos_etiqueta_duracion:]
    duracion = duracion[: duracion.find("</dd>")].splitlines()[1].lstrip().rstrip()
    duracion = duracion[duracion.find(">") + 1 :]
    return duracion


def pais(t):
    etiqueta_pais = "<dt>País</dt>"
    pos_etiqueta_pais = t.find(etiqueta_pais)
    pais = t[pos_etiqueta_pais:]
    pais = pais[: pais.find("</dd>")].splitlines()[1].lstrip().rstrip()
    pais = pais.split(">")
    pais = pais[int(len(pais) - 1)]
    pais = pais.split(";")
    pais = pais[int(len(pais) - 1)]
    return pais

def direccion(t):
    etiqueta_direccion = "<dt>Dirección</dt>"
    pos_etiqueta_direccion = t.find(etiqueta_direccion)
    direccion = t[pos_etiqueta_direccion:]
    direccion=direccion.splitlines()[2] 
    direccion=direccion.split(">")
    directores=""
    for i in range(len(direccion)-1):
        if direccion[i][0]!="<":
            directores+=direccion[i]

    aux=directores.split("<")
    aux1=""
    for i in range(len(aux)-1):
        if aux[i][0]!="/":
            aux1+=aux[i]
    return aux1

def guion(t):
    etiqueta_guion = "<dt>Guion</dt>"
    pos_etiqueta_guion = t.find(etiqueta_guion)
    guion = t[pos_etiqueta_guion + 14:]
    guion = guion[:guion.find("</dd>")]
    guion == guion[guion.find('<span class="nb>'): guion.find('</div>')]
    guionistas = ""
    a=0
    while guion.find("<span>") != -1:
        guion = guion[guion.find("<span>") + len("<span>"):]
        guionistas+=guion[:guion.find("</span>")]
        if a!=0:
            guionistas += ", " + guion[:guion.find("</span>")] 

        a+=1 
    return guionistas


def musica(t):
    etiqueta_guion = "<dt>Música</dt>"
    pos_etiqueta_guion = t.find(etiqueta_guion)
    guion = t[pos_etiqueta_guion + 14:]
    guion = guion[:guion.find("</dd>")]
    guion == guion[guion.find('<span class="nb>'): guion.find('</div>')]
    guionistas = ""
    a=0
    while guion.find("<span>") != -1:
        guion = guion[guion.find("<span>") + len("<span>"):]
        guionistas+=guion[:guion.find("</span>")]
        if a!=0:
            guionistas += " , " + guion[:guion.find("</span>")] 
        a+=1 
    return guionistas



def fotografia(t):
    etiqueta_guion = "<dt>Fotografía</dt>"
    pos_etiqueta_guion = t.find(etiqueta_guion)
    guion = t[pos_etiqueta_guion + 14:]
    guion = guion[:guion.find("</dd>")]
    guion == guion[guion.find('<span class="nb>'): guion.find('</div>')]
    guionistas = ""
    a=0
    while guion.find("<span>") != -1:
        guion = guion[guion.find("<span>") + len("<span>"):]
        guionistas+=guion[:guion.find("</span>")]
        if a!=0:
            guionistas += " , " + guion[:guion.find("</span>")] 
        a+=1 
    return guionistas

def productora(t):
    etiqueta_guion = "<dt>Productora</dt>"
    pos_etiqueta_guion = t.find(etiqueta_guion)
    guion = t[pos_etiqueta_guion + 14:]
    guion = guion[:guion.find("</dd>")]
    guion == guion[guion.find('<span class="nb>'): guion.find('</div>')]
    guionistas = ""
    a=0
    while guion.find("<span>") != -1:
        guion = guion[guion.find("<span>") + len("<span>"):]
        guionistas+=guion[:guion.find("</span>")]
        if a!=0:
            guionistas += " , " + guion[:guion.find("</span>")] 
        a+=1 
    return guionistas

def reparto(t):
    etiqueta_reparto = "<dt>Reparto</dt>"
    pos_etiqueta_reparto = t.find(etiqueta_reparto)
    reparto = t[pos_etiqueta_reparto:]
    reparto = reparto[:reparto.find("</dd>")]
    etiqueta_inicio = '<span itemprop="name">'
    etiqueta_cierre = "</span>"
    all_cast = ""
    a=0
    while(reparto.find(etiqueta_inicio) != -1):
        reparto = reparto[reparto.find(etiqueta_inicio)+len(etiqueta_inicio):]
        all_cast += reparto[:reparto.find(etiqueta_cierre)] 
        if a!=0:
            all_cast += " , " + reparto[:reparto.find(etiqueta_cierre)] 
            a+=1 
    return all_cast



def grupo(t):
    etiqueta_guion = "<dt>Grupos</dt>"
    pos_etiqueta_guion = t.find(etiqueta_guion)
    if pos_etiqueta_guion!=-1:
        guion = t[pos_etiqueta_guion + 14:]
        guion = guion[:guion.find("</dd>")]
        guion == guion[guion.find('<span class="nb>'): guion.find('</div>')]
        guionistas = ""
        a=0
        while guion.find("<span>") != -1:
            guion = guion[guion.find("<span>") + len("<span>"):]
            guionistas+=guion[:guion.find("</span>")]
            if a!=0:
                guionistas += " , " + guion[:guion.find("</span>")] 
            a+=1 

        guionistas=guionistas.split(">")
        guionistas=guionistas[1].split("<")
        guionistas=guionistas[0]
        return guionistas
    return "No hay grupo"

def sinopsis(t):
    etiqueta_sinopsis = "<dt>Sinopsis</dt>"
    pos_etiqueta_sinopsis = t.find(etiqueta_sinopsis)
    descripcion = t[pos_etiqueta_sinopsis:]
    descripcion = descripcion[: descripcion.find("</dd>")]
    descripcion=descripcion.split(">")
    descripcion=descripcion[3]
    descripcion=descripcion.split("(")
    descripcion=descripcion[0]

    return descripcion

datos={
"Título original": titulo_original(t),
"Año":+ anio(t),
"Pais":+ pais(t),
"Fotografia":fotografia(t),
"Duracion":+ daraçao(t),
"Grupo":grupo(t),
"Reparto":reparto(t),
"Productora":productora(t),
"Música":musica(t),
"Guion":guion(t),
"Dirección": direccion(t),
"Sinopsis":+ sinopsis(t)
}
print(datos)