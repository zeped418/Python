"""

/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */

Dato: 

Un número primo es un número natural 

- mayor que 1
- solo es divisible entre sí mismo y 1 

Lista de números primos del 1 al 100:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

"""

import math 

def esPrimo(numero):
    
    # 2 es un caso especial de número primo
    if numero == 2:
        return True
    
    # Si el número es menor o igual a 1, no es primo
    if numero <= 1 or numero % 2 == 0:
        return False
    
    # Verificar divisibilidad por impares hasta la raíz cuadrada del número
    #La raíz cuadrada se aplica para simplificar el proceso, ya que si un numero es dividido entre su raíz cuadrada, entonces no es primo
    #se suma 1 para asegurar que la raíz cuadrada sea inclusiva en el rango del for
    limite = int(math.sqrt(numero)) + 1

    # 3,5,7,9...etc. Los números pares se descartan antes.
    for i in range(3, limite, 2):
        if numero % i == 0:
            return False
    return True

# Imprimir números primos del 1 al 100
print("Lista de números primos del 1 al 100:")
for i in range(1, 101):
    if esPrimo(i):
        print(i, end=", ")

"""
Resultado:

Lista de números primos del 1 al 100:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

"""
