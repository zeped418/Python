#conjunto de datos parecido a un diccionario
set_countries={"Colombia", "Mexico", "Brasil"}
print(set_countries)
print(type(set_countries))

#pueden tener varios tipos de datos
set_mix={1,"Hola",1.0,False,}

#puedes hacer un conjunto a partir de un string
set_string=set("palabra")
print(set_string)

#de igual forma se puede desde una tupla
tupla=("abc", "cde", "fgh", "abc")

set_tupla=set(tupla)
print(set_tupla)

#desde una lista
lista=[1,10,2,8,19,1,20,2]
set_lista=set(lista)
print(set_lista)
#limpia la lista quitando los duplicados

print('numeros unicos: ')
print(list(set_lista))

#longitud de conjuntos
size_set_countries=len(set_countries)
print("Paises en set:",size_set_countries)

#Saber si un elemento pertenece al conjunto

print("Mexico" in set_countries)
print("USA" in set_countries)

#adicionar

set_countries.add("Peru")
print(set_countries)

set_countries.add("Peru")
print(set_countries)

#Se ve que aunque se adciona un elemento existente no lo imprime

set_countries.update({"Argentina", "Canada", "USA"})
print(set_countries)

#para eliminar elementos del conjunto
set_countries.remove("USA")
print(set_countries)

#es mejor eliminar con discard para descartar elementos

#para limpiar todo el conjunto 
set_countries.clean()

