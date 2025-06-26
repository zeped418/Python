"""
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */

"""

texto="Hola Mundini"


def invierteCadena(texto:str):
    lista=[]
    largo=len(texto)-1
    for i in range (0,largo+1):
        lista.append(texto[largo-i])
    print(''.join(lista))

invierteCadena(texto)