#import cv2

#img = cv2.imread('original.jpg')
#resized = cv2.resize(img, (300, 300), interpolation=cv2.INTER_LINEAR)
#cv2.imwrite('resultado.jpg', resized)

import cv2
import os

img = cv2.imread("original.jpg")

(h, w) = img.shape[:2]
centro = (w // 2, h // 2)

matriz_rot = cv2.getRotationMatrix2D(centro, 45, 1.0)
img_rotacionada = cv2.warpAffine(img, matriz_rot, (w, h))

nome_resultado = "iamgem_trasformadarotacao.jpg"
cv2.imwrite(nome_resultado, img_rotacionada)
os.system(f"open {nome_resultado}")
