import cv2

# carregaxml com parametros
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('dataset/download.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# DETECTAR FACE
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# construir retangulo na face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# salvar nova imagem
cv2.imwrite('./saida/nova_img.jpg', img)

# mostrar
cv2.imshow('img', img)
cv2.waitKey()

