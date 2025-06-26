import re

def contarPalabras(texto):
    # Eliminar caracteres no deseados y convertir a minúsculas
    texto_limpio = re.sub(r'[^\w\s]', '', texto).lower()

    # Dividir el texto en palabras
    palabras = texto_limpio.split()

    print(palabras)

    # Contar ocurrencias de cada palabra
    diccionario = {}
    for palabra in palabras:
        diccionario[palabra] = diccionario.get(palabra, 0) + 1

    # Mostrar el recuento final
    print(diccionario)

contarPalabras("¡Hola hola mundini! mi nombre es Carlos, Carlos Zepeda. Es un placer.")
