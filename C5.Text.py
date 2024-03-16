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

#Utilzar comillas dobles o apostrofes nos ayuda a poder escribir alguna de estás como parte del texto mismo.

texto1="I'am Carlos"
texto2='....Es un "suponer"'

print(texto1,texto2)

#Format

template="1. Hola, mi nombre es " + nombre + "y mi apellido es " + apellido
template2="2. Hola, mi nombre es {} y mi apellido es {}".format(nombre, apellido)
template3=f"3. Hola, mi nombre es {nombre} y mi apellido es {apellido}"
#el más utilizado es el formato 3
print(template, template2, template3)

print(100**0.5)