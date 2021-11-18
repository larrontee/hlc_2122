# Ejercicio 6
# Eliminar cadenas vacías de la lista de cadenas
# Dado:
lista = ["Chema", "", "Juan Diego", "Diana", "", "Alejandro"]
# Resultado:
# ["Chema", "Juan Diego", "Diana", "Alejandro"]

lista_aux=lista

for i in range(len(lista)):
    if(lista[i]!=""):
        lista_aux.append(lista[i])

lista=lista_aux
print(lista)