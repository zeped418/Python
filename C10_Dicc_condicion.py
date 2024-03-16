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

#Generar un listado de numeros pares

numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print('v1 =>', even_numbers)

# Ahora usando List Comprehension
even_numbers_v2 = [n for n in numbers if n % 2 == 0]

print('v2 =>', even_numbers_v2)