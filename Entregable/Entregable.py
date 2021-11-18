import requests

# hasta sinopsis

# Terminator 2: The judgment day
# r = requests.get("https://www.filmaffinity.com/es/film576352.html")
# Monty Python's Life of Brian
r = requests.get("https://www.filmaffinity.com/es/film612331.html")
# r = requests.get("https://www.filmaffinity.com/es/film185733.html")

# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
t = r.text

# print(t)


def titulo_original(t):
    etiqueta_titulo = "<dt>Título original</dt>"
    pos_etiqueta_titulo = t.find(etiqueta_titulo)
    titulo = t[pos_etiqueta_titulo:]
    titulo = titulo[: titulo.find("</dd>")].splitlines()[2].lstrip().rstrip()
    titulo = titulo.split("<")
    titulo = titulo[0]
    return titulo


print("Título original:" + titulo_original(t))


def anio(t):
    etiqueta_anio = "<dt>Año</dt>"
    pos_etiqueta_anio = t.find(etiqueta_anio)
    anio = t[pos_etiqueta_anio:]
    anio = anio[: anio.find("</dd>")].splitlines()[1].lstrip().rstrip()
    anio = anio[anio.find(">") + 1 :]
    return anio


print("Año: " + anio(t))


def daraçao(t):
    etiqueta_duracion = "<dt>Duración</dt>"
    pos_etiqueta_duracion = t.find(etiqueta_duracion)
    duracion = t[pos_etiqueta_duracion:]
    duracion = duracion[: duracion.find("</dd>")].splitlines()[1].lstrip().rstrip()
    duracion = duracion[duracion.find(">") + 1 :]
    return duracion


print("Duracion: " + daraçao(t))


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


print("Pais: " + pais(t))


def direccion(t):
    etiqueta_direccion = "<dt>Dirección</dt>"
    pos_etiqueta_direccion = t.find(etiqueta_direccion)
    direccion = t[pos_etiqueta_direccion:]
    direccion = direccion[: direccion.find("</dd>")].splitlines()[2].lstrip().rstrip()
    direccion = direccion.split(">")
    direccion = direccion[4]
    direccion = direccion.split("<")
    direccion = direccion[0]
    return direccion


print("Direccion: " + direccion(t))


def guion(t):
    etiqueta_direccion = "<dt>Guion</dt>"
    pos_etiqueta_direccion = t.find(etiqueta_direccion)
    direccion = t[pos_etiqueta_direccion:]
    direccion = direccion[: direccion.find("</dd>")].splitlines()[2].lstrip().rstrip()
    direccion = direccion.split(">")
    direccion = direccion[4]
    direccion = direccion.split("<")
    direccion = direccion[0]
    return direccion


print("Direccion: " + direccion(t))
