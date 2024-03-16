paises=['Mex', 'Col', 'Arg']

import random
poblacion2={pais:random.randint(1,200) for pais in paises}

print(poblacion2)

resultado={pais: poblacion for (pais,poblacion) in poblacion2.items() if poblacion >50}

print(resultado)

#Generar un diccionario con texto

texto='Hola, soy Chabela'

unicos={letra: letra.upper() for letra in texto if letra in 'aeiou'}

print(unicos)