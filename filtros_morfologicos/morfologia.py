import cv2
import numpy as np
import os

# Carregar imagem em escala de cinza
img = cv2.imread('original.jpg', 0)

# Binarização simples
_, img_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Criar kernel
kernel = np.ones((5,5), np.uint8)

# Aplicar erosão
erosion = cv2.erode(img_bin, kernel, iterations=1)

# Salvar e abrir
nome_resultado = "imagem_morfologia.jpg"
cv2.imwrite(nome_resultado, erosion)
os.system(f"open {nome_resultado}")
