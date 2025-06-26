"""

/*
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 */

"""

str1="hola a todos chicos"
str2="mundini munidote"

out1="a"
out2="uie"

for letra in str1:
    if str2.find(letra) >= 0:
        #print("Reemplaza " + letra)
        str1=str1.replace(letra,'')

for letra in str2:
    if str1.find(letra) >= 0:
        str2=str2.replace(letra,'')

str1=''.join(set(str1))
str2=''.join(set(str2))

print(f"""Letras de la palabra 1: {str1} 
Letras de la palabra 2: {str2}""")


