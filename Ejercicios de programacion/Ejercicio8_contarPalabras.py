"""
/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
 */

"""

def right(s:str, amount:int):
    return s[-amount:]


def contarPalabras(texto):
    espacios=0
    lista=[]
    dicc={}

    regex='0123456789,;.:-_!"#$%&/()=?¡¿+}{-[]*<>|°^`~¬}'

    for letra in texto:
        if letra==' ':
            espacios+=1
        if regex.find(letra) > -1:
            texto=texto.replace(letra,'')

    for i in range(0,espacios+1):

        largo=len(texto)
        if i!=espacios:
            sigEsp=texto.index(' ')
        else:
            sigEsp=largo

        palabra=texto[0:sigEsp]

        texto=right(texto,largo - 1 - sigEsp)

        lista.append(palabra)

    lista=[x.lower() for x in lista]

    unique_list = []

    for x in lista:
        x=x.lower()
        if x not in unique_list:
            unique_list.append(x)

    ocurrencias=[lista.count(x) for x in unique_list]

    # Convertir cada elemento para que solo la primera letra esté en mayúscula
    lista_convertida = [elemento.capitalize() for elemento in unique_list]


    nuevo_dicc={palabra: ocurrencia for (palabra, ocurrencia) in zip(lista_convertida,ocurrencias)}

    print(nuevo_dicc)

contarPalabras("¡Hola hola mundini! mi nombre es Carlos, Carlos Zepeda. Es un placer.")

#Returns {'Hola': 2, 'Mundini': 1, 'Mi': 1, 'Nombre': 1, 'Es': 2, 'Carlos': 2, 'Zepeda': 1, 'Un': 1, 'Placer': 1}