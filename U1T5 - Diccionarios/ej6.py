# Ejercicio 6
# Eliminar un conjunto de claves de un diccionario
# Dado:
diccionario = {
    "nombre": "Pikolo",
    "edad": 28,
    "salario": 8000,
    "planeta": "Namek"
}
keysToRemove = ["nombre", "salario"]
# Resultado:
# {'planeta': 'Namek', 'edad': 28}
dic=[(k,v) for (k,v) in diccionario.items()]
au x={}



for i in range(0, len(dic)):
    for j in range(0, len(dic[0])):
        if(dic[i][j]!="nombre" or dic[i][j]!="salario"):
            aux[]=dic
print(dic)