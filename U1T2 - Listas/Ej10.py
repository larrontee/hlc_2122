# Ejercicio 10
# Dada una lista, elimine todas las ocurrencias de 20 de la lista
# Dado:
lista = [5, 20, 15, 20, 25, 50, 20]
# Resultado:
# [5, 15, 25, 50]

for i in range(len(lista)):
    if(lista[i]==20):
        lista[i]=200
