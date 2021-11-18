# Ejercicio 3
# Dada una lista de números. Convierte cada elemento de una lista en su cuadrado
# Dado:
lista = [1, 2, 3, 4, 5, 6, 7]
# Resultado:
# [1, 4, 9, 16, 25, 36, 49]
lista2=[]

for i in range(int(len(lista))):
    lista2.append(int(lista[i])*int(lista[i]))
    
print(lista2)