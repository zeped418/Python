text="Carlos"
#Para ingresar a las posiciones del texto usa los corchetes
'''
print(len(text))
text[1]
text[1:4]
text[1:]
text[:5]
print(text[0:6:2])
'''

# Lista de valores

lista=[1,2,3,4,5]
print(lista)
print(lista[1])  
lista.append(10) #agrega un valor al final de la lista
print(lista)
lista.insert(0,-10) #inserta un objeto en la posición indicada
print(lista)
print(lista.index(10))
'''
append(): Añade un ítem al final de la lista.

clear(): Vacía todos los ítems de una lista.

extend(): Une una lista a otra.

count(): Cuenta el número de veces que aparece un ítem.

index(): Devuelve el índice en el que aparece un ítem (error si no aparece).

insert(): Agrega un ítem a la lista en un índice específico.

pop(): Extrae un ítem de la lista y lo borra.

remove(): Borra el primer ítem de la lista cuyo valor concuerde con el 
que indicamos.

reverse(): Le da la vuelta a la lista actual.

sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.
'''
letters = ['A', 'B', 'C', 'D', 'E', 'F']

# Escribe tu solución 👇

print(letters)
letters.append("G")
print(letters)
letters.pop(0)
print(letters)
letters.insert(0, "Z")
print(letters)
letters.remove("C")
print(letters)
letters.reverse()
print(letters)