# Ejercicio 6:
# Dadas dos cadenas, s1 y s2, cree una cadena mixta usando las siguientes reglas
# Nota : cree una tercera cadena hecha del primer carácter de s1, luego el último carácter de s2, Siguiente, el segundo
# carácter de s1 y el segundo último carácter de s2, y así sucesivamente. Los caracteres sobrantes van al final del resultado.
# Dado:
s1 = "Abc"
s2 = "Xyzjdk"
# Resultado esperado:
# AzbycX
s3=s2[::-1]

long = int(len(s1))

for i in range(long): 
    s3+=s1[i]
    s3+=s2[-(i+1)]
    
print(s3)