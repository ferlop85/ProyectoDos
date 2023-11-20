import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Cargar la imagen con OpenCV
img_cv2 = cv2.imread("gato.jpg")

# Convertir la imagen de BGR a RGB
img_rgb = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)

# Separar las matrices de los tres canales de color
canal_r = img_rgb[:, :, 0]
canal_g = img_rgb[:, :, 1]
canal_b = img_rgb[:, :, 2]

# Mostrar las imágenes y los histogramas en una misma figura
fig, axs = plt.subplots(1, 4, figsize=(15, 4))

axs[0].imshow(img_rgb)
axs[0].set_title("Imagen Original")
axs[0].axis('off')

axs[1].imshow(canal_r, cmap='Reds')
axs[1].set_title("Canal Rojo")
axs[1].axis('off')

axs[2].imshow(canal_g, cmap='Greens')
axs[2].set_title("Canal Verde")
axs[2].axis('off')

axs[3].imshow(canal_b, cmap='Blues')
axs[3].set_title("Canal Azul")
axs[3].axis('off')

plt.show()


plt.imshow(imagen_gris_rgb)
plt.title("fer")
plt.axis('off')
plt.show()