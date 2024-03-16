#Strings o cadenas de texto van dentro de "String" o 'String'

nombre='carlos' #string
edad=18 #integer
hombre=True #boolean
Estatura=175.5 #float

#nota: cuando usas input, todos los valores los almacena como texto

print(type(nombre), type(edad), type(hombre), type(Estatura))

#para concatenar strings se puede utilizar +

apellido='zepeda'

full_name=nombre+" "+apellido

print(full_name)