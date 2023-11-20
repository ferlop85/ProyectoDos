# funciones_imagen.py
import cv2
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import numpy as np

def obtener_palabra_clave():
    palabras_clave_validas = ["Youtube", "Instagram", "Twitter", "Facebook"]

    while True:
        palabra_clave = input("Ingrese la palabra clave (Youtube, Instagram, Twitter o Facebook): ")
        if palabra_clave in palabras_clave_validas:
            return palabra_clave
        else:
            print("Palabra clave no válida. Intente de nuevo.")

def cargar_imagen(nombre_imagen, palabra_clave):
    try:
        # Verificar si el archivo existe antes de intentar cargarlo
        with open(nombre_imagen, 'rb'):
            pass
        
        # Si el archivo existe, proceder con la carga y redimensionamiento
        img_cv2 = cv2.imread(nombre_imagen)

        # Dimensiones recomendadas para cada plataforma
        dimensiones_plataforma = {
            "Youtube": (1280, 720),
            "Instagram": (1080, 1080),
            "Twitter": (1200, 675),
            "Facebook": (1200, 630)
        }

        # Obtener las dimensiones recomendadas para la palabra clave
        dimensiones = dimensiones_plataforma.get(palabra_clave)

        # Redimensionar la imagen manteniendo la proporción
        img_rgb = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_pil.thumbnail(dimensiones)

        print(f"Imagen redimensionada para {palabra_clave}. Dimensiones: {dimensiones}")
        return img_pil
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_imagen}' no existe. Intente de nuevo.")
        return None
    except Exception as e:
        print(f"Error al cargar/redimensionar la imagen: {e}")
        return None

def mostrar_imagen_matplotlib(imagen_pil, titulo="Imagen Redimensionada"):
    # Mostrar la imagen utilizando la biblioteca Matplotlib
    plt.imshow(imagen_pil)
    plt.title(titulo)
    plt.axis('off')  # Desactivar ejes
    plt.show()

def aplicar(matriz, relativa):
    matriz = matriz.astype(np.float32) * relativa.astype(np.float32)
    matriz = np.round(matriz).astype(np.uint8)
    return matriz
    
def ajustar_contraste_histograma_propio(img_cv2):
    try:
        # Convertir la imagen de Pillow a una matriz numpy
        img_array = np.array(img_cv2)
        img_gris = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        imagen_equalizada = cv2.equalizeHist(img_gris)

        epsilon = 70
        variacion_relativa = (imagen_equalizada.astype(np.float32)) / (img_gris.astype(np.float32) + epsilon)

        R = img_array[:, :, 0]
        G = img_array[:, :, 1]
        B = img_array[:, :, 2]

        R_nuevo = aplicar(R, variacion_relativa)
        G_nuevo = aplicar(G, variacion_relativa)
        B_nuevo = aplicar(B, variacion_relativa)

        nueva_imagen = np.stack((R_nuevo, G_nuevo, B_nuevo), axis=-1)

# Mostrar la imagen original y la nueva imagen en un solo gráfico
        plt.figure(figsize=(15, 8))

# Imagen original
        plt.subplot(2, 2, 1)
        plt.imshow(img_cv2)
        plt.title('Imagen Original')
        plt.axis('off')

# Histograma de la imagen original
        plt.subplot(2, 2, 2)
        plt.hist(img_array.flatten(), 256, [0, 256], color='gray', alpha=0.7)
        plt.title('Histograma Original')

# Nueva imagen
        plt.subplot(2, 2, 3)
        plt.imshow(nueva_imagen)
        plt.title('Nueva Imagen')
        plt.axis('off')

# Histograma de la nueva imagen
        plt.subplot(2, 2, 4)
        plt.hist(nueva_imagen.flatten(), 256, [0, 256], color='gray', alpha=0.7)
        plt.title('Histograma Nueva Imagen')

        plt.show()
        img_ecualizada_pil = Image.fromarray(nueva_imagen)
        return img_ecualizada_pil
    except Exception as e:
        print(f"Error al ajustar el contraste: {e}")
        return None

    
def mostrar_plt_de_filtros(imagen_pil):
    try:
        # Convertir la imagen de Pillow a una matriz numpy
        img_np = np.array(imagen_pil)

        # Mostrar las imágenes en una misma figura
        plt.figure(figsize=(15, 5))

        # Mostrar la imagen original
        plt.subplot(2, 5, 1)
        plt.imshow(imagen_pil)
        plt.title("Original")
        plt.axis('off')

        # Iterar sobre todos los filtros y mostrar las imágenes filtradas
        nombres_filtros = [
            "BLUR", "CONTOUR", "DETAIL",
            "EDGE_ENHANCE", "EDGE_ENHANCE_MORE",
            "EMBOSS", "FIND_EDGES",
            "SHARPEN", "SMOOTH"
        ]

        for i, filtro in enumerate(nombres_filtros, start=2):
            # Convertir la imagen de nuevo a formato Pillow antes de aplicar el filtro
            imagen_pil_temp = Image.fromarray(img_np)

            # Aplicar el filtro
            imagen_filtrada = imagen_pil_temp.filter(ImageFilter.__dict__[filtro])

            plt.subplot(2, 5, i)
            plt.imshow(imagen_filtrada)
            plt.title(filtro)
            plt.axis('off')

        plt.show()

        return None  # No hay imagen filtrada para devolver en este caso
    except Exception as e:
        print(f"Error al aplicar los filtros: {e}")
        return None

def dibujar_boceto_persona(imagen, persona=True):
    try:
        if not persona:
            print("No hay persona en el dibujo.")
            return imagen  # Devuelve la imagen original si no hay persona

        imagen_np = np.array(imagen)
        
        # Convertir la imagen a escala de grises
        imagen_gris = cv2.cvtColor(imagen_np, cv2.COLOR_BGR2GRAY)

        # Aplicar un filtro de desenfoque para suavizar la imagen y reducir el ruido
        imagen_suavizada = cv2.GaussianBlur(imagen_gris, (5, 5), 0)

        # Aplicar el detector de bordes utilizando el operador de Sobel
        bordes = cv2.Canny(imagen_suavizada, 50, 150)

        # Convertir la imagen de boceto a formato RGB
        bordes_rgb = cv2.cvtColor(bordes, cv2.COLOR_GRAY2RGB)

        plt.figure(figsize=(10, 5))

        plt.subplot(1, 2, 1)
        plt.imshow(imagen)
        plt.title("Imagen Original")
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.imshow(bordes_rgb)
        plt.title("Boceto de la Persona")
        plt.axis('off')

        plt.show()

        return bordes_rgb  # Devuelve la imagen con el boceto

    except Exception as e:
        print(f"Error al dibujar el boceto de la persona: {e}")
        return imagen  # Devuelve la imagen original en caso de error


def guardar_imagen(imagen, nombre_archivo="MiImagen.jpg"):
    try:
        imagen.save(nombre_archivo)
        print(f"Imagen guardada como '{nombre_archivo}' exitosamente.")
    except Exception as e:
        print(f"Error al guardar la imagen: {e}")


def seleccionar_filtro():
    while True:
        try:
            nombres_filtros = [
                "BLUR", "CONTOUR", "DETAIL",
                "EDGE_ENHANCE", "EDGE_ENHANCE_MORE",
                "EMBOSS", "FIND_EDGES",
                "SHARPEN", "SMOOTH"
            ]

            print("\nSeleccione un filtro:")
            for i, filtro in enumerate(nombres_filtros, start=1):
                print(f"{i}. {filtro}")

            filtro_seleccionado = input("Ingrese el número del filtro: ")

            try:
                filtro_seleccionado = int(filtro_seleccionado)
                if 1 <= filtro_seleccionado <= len(nombres_filtros):
                    return nombres_filtros[filtro_seleccionado - 1]
                else:
                    print("Número de filtro no válido. Intente de nuevo.")
            except ValueError:
                print("Por favor, ingrese un número válido. Intente de nuevo.")

        except Exception as e:
            print(f"Error al seleccionar el filtro: {e}")

        print()  # Agregar una línea en blanco para mejorar la legibilidad


def aplicar_filtro(filtro, imagen_pil):
    try:
        # Convertir la imagen de Pillow a una matriz numpy
        img_np = np.array(imagen_pil)

        # Convertir la imagen de nuevo a formato Pillow antes de aplicar el filtro
        imagen_pil_temp = Image.fromarray(img_np)

        # Aplicar el filtro seleccionado
        imagen_modificada = imagen_pil_temp.filter(ImageFilter.__dict__[filtro])

        return imagen_modificada

    except Exception as e:
        print(f"Error al aplicar el filtro: {e}")
        return None
