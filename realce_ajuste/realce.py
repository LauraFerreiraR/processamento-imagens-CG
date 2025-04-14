import cv2
import numpy as np
import os

# Nome da imagem de entrada e saída

imagem_entrada = 'original.jpg'
imagem_saida = 'imagem_realcada.jpg'  

# Carrega a imagem
img = cv2.imread(imagem_entrada)

# Aplica realce de contraste com alpha e beta
alpha = 1.5  # Contraste
beta = 20    # Brilho
img_enhanced = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

# Salva a imagem realçada
cv2.imwrite(imagem_saida, img_enhanced)
print(f"Imagem gerada: {imagem_saida}")

os.system(f"open {imagem_saida}")
