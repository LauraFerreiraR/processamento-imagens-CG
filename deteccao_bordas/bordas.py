import cv2
import os

# Nome da imagem de entrada e saída
imagem_entrada = 'original.jpg'
imagem_saida = 'imagem_bordas.jpg'  # você pode mudar esse nome

# Carrega a imagem
img = cv2.imread(imagem_entrada, 0)  # Carrega em escala de cinza

# Detecta bordas
edges = cv2.Canny(img, 100, 200)

# Salva a imagem com bordas
cv2.imwrite(imagem_saida, edges)
print(f"Imagem gerada: {imagem_saida}")

os.system(f"open {imagem_saida}")