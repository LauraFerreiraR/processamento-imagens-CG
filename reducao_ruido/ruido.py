import cv2
import os

# Nome da imagem de entrada e saída
imagem_entrada = 'original.jpg'
imagem_saida = 'imagem_suavizada.jpg'  # você pode trocar esse nome

# Carrega a imagem
img = cv2.imread(imagem_entrada)

# Aplica Gaussian Blur para suavizar (reduzir ruído)
img_denoised = cv2.GaussianBlur(img, (5, 5), 0)

# Salva a imagem suavizada
cv2.imwrite(imagem_saida, img_denoised)
print(f"Imagem gerada com sucesso: {imagem_saida}")

os.system(f"open {imagem_saida}")
