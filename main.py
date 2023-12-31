# menu.py
from funciones import*

def menu():
    imagen_original = None
    imagen_modificada = None

    while True:
        print("\nMenú:")
        print("1. Cargar imagen")
        print("2. Mostrar imagen original")
        print("3. Ajustar imagen con histograma")
        print("4. Ajustar imagen con histograma propio")
        print("5. Aplicar filtro")
        print("6. Hacer boceto")
        print("7. Mostrar imagen modificada")
        print('8. Recargar imagen orginal')
        print('9. Guardar imagen como "MiImagen.jpg"')
        print("10. Salir")

        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            nombre_imagen = input("Ingrese el nombre de la imagen (por ejemplo, 'gato.jpg'): ")
            palabra_clave = obtener_palabra_clave()
            imagen_original  = cargar_imagen(nombre_imagen, palabra_clave)
            if imagen_original is not None:
                imagen_modificada = imagen_original.copy()
            else:
                print("No se pudo cargar la imagen. Por favor, intente de nuevo.")
        elif opcion == "2":
            if imagen_original == None:
                print("Primero debes cargar una imagen. Usa la opción '1' para cargar una imagen.")
            else:
                mostrar_imagen_matplotlib(imagen_original, titulo="Imagen Original")
        elif opcion == "3":
            if imagen_original == None:
                print("Primero debes cargar una imagen. Usa la opción '1' para cargar una imagen.")
            else:
                imagen_modificada = ajustar_contraste_histograma(imagen_modificada)
        elif opcion == "4":
            if imagen_original == None:
                print("Primero debes cargar una imagen. Usa la opción '1' para cargar una imagen.")
            else:
                imagen_modificada = ajustar_contraste_histograma_propio(imagen_modificada)
        elif opcion == "5":
            if imagen_original is None:
                print("Primero debes cargar una imagen. Usa la opción '1' para cargar una imagen.")
            else:
                mostrar_plt_de_filtros(imagen_modificada)
                filtro = seleccionar_filtro()
                if filtro is not None:
                    imagen_modificada = aplicar_filtro(filtro, imagen_modificada)
                    print(f"Se ha aplicado el filtro '{filtro}'")
        elif opcion == "6":
            if imagen_original == None:
                print("Primero debes cargar una imagen. Usa la opción '1' para cargar una imagen.")
            else:
                imagen_modificada = dibujar_boceto_persona(imagen_modificada, persona=True)
        elif opcion == "7":
            if imagen_original == None:
                print("Primero debes cargar una imagen. Usa la opción '1' para cargar una imagen.")
            else:
                mostrar_imagen_matplotlib(imagen_modificada, titulo="Imagen Modificada")
        elif opcion == "8":
            if imagen_original is None:
                print("Primero debes cargar una imagen. Usa la opción '1' para cargar una imagen.")
            else:
                imagen_modificada = imagen_original.copy()
        elif opcion == "9":
            if imagen_original is None:
                print("Primero debes cargar una imagen. Usa la opción '1' para cargar una imagen.")
            else:
                guardar_imagen(imagen_modificada)
        elif opcion == "10":
            print("Hasta luego")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()