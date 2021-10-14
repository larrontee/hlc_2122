# Ejercicio 3:
# Dadas dos cadenas, s1 y s2 devuelven una nueva cadena compuesta por el primer, el medio y el último carácter de cada 
# cadena de entrada
# Dado :
s1 = "Chema"
s2 = "Duran"
# Resultado:
# CDeran

s3=s1[:1]+s2[:1]+s1[int(len(s1)/2):int(len(s1)/2)+1]+s2[int(len(s2)/2):int(len(s2)/2)+1]+s1[-1]+s2[-1]
print(s3)