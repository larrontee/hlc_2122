# Ejercicio 4
# Concatenar dos listas en el siguiente orden
# Dado:
lista1 = ["Hola ", "toma "]
lista2 = ["guapo", "señor"]
lista3=[]
# Resultado:
# ['Hola guapo', 'Hola señor', 'toma guapo', 'toma señor']
lista2r=lista2[::-1]
cadena=""

for x in range(int(len(lista1))):
    for y in range(int(len(lista1))):
            cadena += lista1[x]
            cadena += lista2[y]
            lista3.append(cadena)
            cadena=""

print(lista3)