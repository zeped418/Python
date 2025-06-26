# {key: value for }

dicc={}

for i in range(1,11):
    dicc[i]=i*2

print(dicc)

# manera 2 más corta

dicc2={i:i*2 for i in range(1,10)}
print(dicc2)

# lista de paises

paises=['Mex', 'Col', 'Arg']

poblacion={}

import random

for pais in paises:
    poblacion[pais]=random.randint(1,100)

print(poblacion)


poblacion2={pais:random.randint(1,200) for pais in paises}
print(poblacion2)

# ejercicio 

nombres=['Nicolas', 'Pedro', 'Rita']

edades=[12,23,44]

union=zip(nombres,edades)

#imprime una referencia pero no la union
print(union)

#muentra [('Nicolas', 12), ('Pedro', 23), ('Rita', 44)]    
print(list(union))

nuevo_dicc={nombre: edad for (nombre, edad) in zip(nombres,edades)}

print(nuevo_dicc)