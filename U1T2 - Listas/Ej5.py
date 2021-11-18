# Ejercicio 5

# Dada dos listas, itere ambas simultáneamente de modo que lista1 debería mostrar el elemento en el orden original y lista2 en orden inverso

# Dado:

lista1 = [10, 20, 30, 40]
lista2 = [100, 200, 300, 400]


for i in range(int(len(lista2))):
    print(lista1[i])
    print(lista2[int(len(lista2))-i-1])

