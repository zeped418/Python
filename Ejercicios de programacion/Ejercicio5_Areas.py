"""

/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */

"""

def calcula_area(figura: str, base:float, altura:float):
    
    figura=str(figura).lower().strip()
    if figura=='triángulo' or figura=='triangulo':
        area=base*altura*0.5
    elif figura=='cuadrado' and base==altura:
        area=base**2
    elif figura=='rectangulo' or figura=='rectánuglo':
        area=base*altura
    else:
        return "Información de entrada incorrecta"
    return area

print(f"Area 1: {calcula_area('triangulo',3,2)}")
print(f"Area 2: {calcula_area('cuadrado',15,15)}")
print(f"Area 3: {calcula_area('rectangulo',3,2)}")