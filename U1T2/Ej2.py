# Ejercicio 2:
# Concatenar dos listas por índice

# Dado:
lista1 = ["M", "nom", "e", "Che"]
lista2 = ["i", "bre", "s", "ma"]

# Resultado esperado:
# ['Mi nombre es Chema']


if(int(len(lista1))>int(len(lista2))):
    longitud= int(len(lista2))
else:
    longitud= int(len(lista1))


cadena=""

for i in range(int(len(lista2)+int(diferencia))):
    

    cadena+=lista1[i] 
    cadena+=lista2[i] 
    cadena += " "

lista3=[cadena]
print(lista3)
