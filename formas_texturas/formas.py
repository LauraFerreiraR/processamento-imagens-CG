# Lê a imagem colorida
img_color = cv2.imread('original.jpg')

# Converte pra escala de cinza e aplica limiarização
gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Encontra contornos
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Desenha os contornos
img_contours = img_color.copy()
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)

# Salva e abre
nome_resultado = "imagem_formasetextura.jpg"
cv2.imwrite(nome_resultado, img_contours)
os.system(f"open {nome_resultado}")
