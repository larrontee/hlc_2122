# Ejercicio 8
# Dada una lista anidada, extiéndala agregando la sublista ["h", "i", "j"]de tal manera que se vea como la siguiente lista
# Dado:
lista = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# Sublista que se agregará = ["h", "i", "j"]
sublista = ["h", "i", "j"]
# Resultado:
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j' ], 'k'], 'l'], 'm', 'n']

lista[2][1][2].append(sublista)
print(lista)
