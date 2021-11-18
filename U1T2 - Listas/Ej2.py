# Ejercicio 2:
# Concatenar dos listas por índice

# Dado:
lista1 = ["M", "nom", "e", "Che"]
lista2 = ["i", "bre", "s", "ma","Duran","hola","fran"]

# Resultado esperado:
# ['Mi nombre es Chema']


if(int(len(lista1))>int(len(lista2))):
    longitud= int(len(lista2))
    largo=lista1
    chico=lista2
else:
    longitud= int(len(lista1))
    largo=lista2
    chico=lista2

cadena=""

for i in range(longitud):
    cadena+=lista1[i] 
    cadena+=lista2[i] 
    cadena += " "

for i in range(int(len(largo))):
    if(i>=int(len(largo[longitud:int(len(largo))]))):
        cadena+=largo[i] 
        cadena += " "



lista3=[cadena]
print(lista3)
