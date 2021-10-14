# Ejercicio 1:
# Dada una cadena de longitud impar mayor que 7, devuelva una nueva cadena
# formada por los tres caracteres del medio de una cadena determinada
# Dado :
# Caso 1
# str1 = "ChemTioaDur"
# Resultado
# Tio

cadena = input("introduce una cadena mayor que 7")
numero=len(cadena)
cad=cadena[int((len(cadena)/2))-1:int((len(cadena)/2))+2]
print(cad)

    
