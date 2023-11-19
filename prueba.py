import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img_cv2 = cv2.imread("gato.jpg")

# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2GRAY)

# Crear una imagen RGB replicando el canal de escala de grises en cada canal
imagen_gris_rgb = cv2.cvtColor(imagen_gris, cv2.COLOR_GRAY2RGB)

# Mostrar la imagen en escala de grises en formato RGB
plt.imshow(imagen_gris_rgb)
plt.title("Imagen en escala de grises en formato RGB")
plt.axis('off')
plt.show()

print(imagen_gris_rgb)


plt.imshow(imagen_gris_rgb)
plt.title("fer")
plt.axis('off')
plt.show()