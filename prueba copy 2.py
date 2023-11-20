import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen con OpenCV en escala de grises
img_cv2 = cv2.imread("gato.jpg", 0)


def funcion(img_cv2):
    # Ecualizar la imagen en escala de grises
    imagen_equalizada = cv2.equalizeHist(img_cv2)
    print(img_cv2.astype(np.float32))
    print(img_cv2.astype(np.float32)+1)

    epsilon = 0.6
    variacion_relativa = (imagen_equalizada.astype(np.float32)) / (img_cv2.astype(np.float32) + epsilon)

    print(variacion_relativa)

    def aplicar(matriz, relativa):
        matriz = matriz.astype(np.float32) * 0.6 * relativa.astype(np.uint8)
        matriz = np.round(matriz).astype(np.uint8)
        return matriz

    neuva = cv2.imread("gato.jpg")
    neuva = cv2.cvtColor(neuva, cv2.COLOR_BGR2RGB)
    R = neuva[:, :, 0]
    G = neuva[:, :, 1]
    B = neuva[:, :, 2]

    R_nuevo = aplicar(R, variacion_relativa)
    G_nuevo = aplicar(G, variacion_relativa)
    B_nuevo = aplicar(B, variacion_relativa)

    nueva_imagen = np.stack((R_nuevo, G_nuevo, B_nuevo), axis=-1)

# Mostrar la imagen original y la nueva imagen en un solo gráfico
    plt.figure(figsize=(15, 8))

# Imagen original
    plt.subplot(2, 2, 1)
    plt.imshow(neuva)
    plt.title('Imagen Original')
    plt.axis('off')

# Histograma de la imagen original
    plt.subplot(2, 2, 2)
    plt.hist(img_cv2.flatten(), 256, [0, 256], color='gray', alpha=0.7)
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

funcion(img_cv2)