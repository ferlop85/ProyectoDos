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

histR, binsR = np.histogram(canal_r.flatten(),256,[0,256])
histG, binsG = np.histogram(canal_g.flatten(),256,[0,256])

fig, axs = plt.subplots(2, 2, figsize=(15, 8))

axs[0, 0].imshow(canal_r, cmap='Reds')
axs[0, 0].set_title("Canal Rojo")
axs[0, 0].axis('off')

axs[0, 1].imshow(canal_g, cmap='Greens')
axs[0, 1].set_title("Canal Verde")
axs[0, 1].axis('off')

cdfR = histR.cumsum()
cdf_normalizedR = cdfR * float(histR.max()) / cdfR.max()

cdfG = histG.cumsum()
cdf_normalizedG = cdfG * float(histG.max()) / cdfG.max()

axs[1, 0].plot(cdf_normalizedR, color="b")
axs[1, 0].hist(canal_r.flatten(), 256, [0, 256], color="r")
axs[1, 0].set_title("Histograma Canal Rojo")

axs[1, 1].plot(cdf_normalizedG, color="b")
axs[1, 1].hist(canal_g.flatten(), 256, [0, 256], color="g")
axs[1, 1].set_title("Histograma Canal Verde")

plt.show()

# Separar las matrices de los tres canales de color
canal_r = cv2.equalizeHist(canal_r)
canal_g = cv2.equalizeHist(canal_g)

histR, binsR = np.histogram(canal_r.flatten(),256,[0,256])
histG, binsG = np.histogram(canal_g.flatten(),256,[0,256])

fig, axs = plt.subplots(2, 2, figsize=(15, 8))

axs[0, 0].imshow(canal_r, cmap='Reds')
axs[0, 0].set_title("Canal Rojo")
axs[0, 0].axis('off')

axs[0, 1].imshow(canal_g, cmap='Greens')
axs[0, 1].set_title("Canal Verde")
axs[0, 1].axis('off')

cdfR = histR.cumsum()
cdf_normalizedR = cdfR * float(histR.max()) / cdfR.max()

cdfG = histG.cumsum()
cdf_normalizedG = cdfG * float(histG.max()) / cdfG.max()

axs[1, 0].plot(cdf_normalizedR, color="b")
axs[1, 0].hist(canal_r.flatten(), 256, [0, 256], color="r")
axs[1, 0].set_title("Histograma Canal Rojo")

axs[1, 1].plot(cdf_normalizedG, color="b")
axs[1, 1].hist(canal_g.flatten(), 256, [0, 256], color="g")
axs[1, 1].set_title("Histograma Canal Verde")

plt.show()