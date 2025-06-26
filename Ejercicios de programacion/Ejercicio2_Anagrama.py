"""
https://retosdeprogramacion.com/ejercicios

/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */

"""

def my_function(word1,word2):

    #Prints for testing
    # print('Word1: ' + word1)
    # print('Word2: ' + word2)

    if len(word1)==0 or len(word2)==0: return False 

    arrayWord1=[]
    arrayWord2=[]

    for letter in word1:
        arrayWord1.append(letter)
    
    for letter in word2:
        arrayWord2.append(letter)

    arrayWord2.reverse()

    word1=''.join(arrayWord1)
    word2=''.join(arrayWord2)

    # print('Word1: ' + word1)
    # print('Word2: ' + word2)

    if word1 == word2:
        return True
    else:
        return False

print(my_function('','bola'))
# Returns False

print(my_function('hola','bola'))
# Returns False

print(my_function('sanas', 'sanas'))
#Returns True 