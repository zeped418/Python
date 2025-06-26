"""

/*
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
 */

"""


import requests
from PIL import Image
from io import BytesIO

def obtener_dimensiones_imagen(url):
    try:
        # Realizar la solicitud GET a la URL de la imagen
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza una excepción si el status code no es 200
        
        # Leer la imagen desde la respuesta de la solicitud
        imagen = Image.open(BytesIO(respuesta.content))
        
        # Obtener las dimensiones de la imagen
        width, height = imagen.size
        
        return width, height
    
    except requests.exceptions.HTTPError as err:
        print(f"Error al obtener la imagen: {err}")
        return None, None
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None, None

def main():
    # URL de la imagen
    url_imagen = "https://images.squarespace-cdn.com/content/v1/52c9d908e4b0e87887310693/1570977177233-3MLE72XBCVKG0S2Y8DS5/spiderman-into-spider-verse-5k-7b-2048x2048-1020x1020.jpg"

    # Obtener las dimensiones de la imagen
    width, height = obtener_dimensiones_imagen(url_imagen)
    
    if width is not None and height is not None:
        print("Anchura de la imagen:", width)
        print("Altura de la imagen:", height)
    else:
        print("No se pudieron obtener las dimensiones de la imagen.")

if __name__ == "__main__":
    main()
