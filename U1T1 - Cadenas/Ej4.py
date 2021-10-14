# Ejercicio 4:
# Dada una cadena de entrada con la combinación de mayúsculas y minúsculas,organice
# los caracteres de tal manera que todas las letras minúsculas deben ir primero.
# Dado :
str1 = "ChEmaDUraN"
# Resultado:
# hmaraCEDUN
str2=""
str3=""
for x in range(len(str1)):
    if(str1[x].islower()):
        str2+=str1[x]
    else:
        str3+=str1[x]
print(str2 + str3)


