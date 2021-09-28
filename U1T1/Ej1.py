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
cad=cadena[(len(cadena)/2):]




if len(cadena) >= 7 and numero%2==0:
    print(cad)
else:print("nah par")
    