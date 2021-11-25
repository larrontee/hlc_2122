# Cree un nuevo diccionario extrayendo las siguientes claves de un diccionario a continuación
# Dado:
# diccionario = {
#     "nombre": "Pikolo",
#     "edad":28,
#     "salario": 8000,
#     "planeta": "Namek"
#     }
# Claves para extraer:
# keys = ["nombre", "salario"]
# Resultado:
# {'nombre': 'Kelly', 'salario': 8000}


diccionario = {
    "nombre": "Kelly",
    "edad":28,
    "salario": 8000,
    "planeta": "Namek"
}

# Esto es un iterador logico que copia el diccionario y lo convierte en array 
dic=[(k,v) for (k,v) in diccionario.items()]
print(dic)
# con esto ahora puedes recorrerlo con un for e ir mirando en cada posicion si es la clave que quieres




aux={}
for i in range(0, len(dic)): 
    for j in range(0, len(dic[0])):
        if(dic[i][j]=="nombre" or dic[i][j]=="salario"):
            aux[dic[i][0]]=dic[i][1]

# diccionario=[(k,diccionario[k]) for (k) in keysToRemove]
# print(diccionario)

print(aux)