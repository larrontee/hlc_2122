# Ejercicio 5:
# Cuente todas las minúsculas, mayúsculas, dígitos y símbolos especiales de una cadena determinada
# Dado :
str1 = "C@#he26ma^&Du5ran"
# Resultado esperado :
# Recuentos totales de caracteres, dígitos y símbolos 
# Caracteres = 10 
# Dígitos = 3 
# Símbolo = 4
Dígitos=int(0)
Caracteres=int(0)
Símbolo=int(0)
        
for x in range(len(str1)):
    if(str1[x].isdigit()):
        Dígitos +=1
    elif(str1[x].islower() or str1[x].isupper()):
        Caracteres +=1
    else:
        Símbolo+=1


print("Dígitos " , Dígitos )
print("Caracteres" , Caracteres) 
print("Símbolo " , Símbolo)