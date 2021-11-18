# Ejercicio 1
# A continuación se muestran las dos listas, conviértalo en el diccionario
keys = ['Diez', 'Veinte', 'Treinta']
values = [10, 20, 30]
# Resultado:
# {'Diez': 10, 'Veinte': 20, 'Treinta': 30}

dic ={}

for i in range(0,len(keys)):
    dic[keys[i]] = values[i]

print(dic)