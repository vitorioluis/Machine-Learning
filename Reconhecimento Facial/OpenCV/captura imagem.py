import cv2
from config import GREEN, WHITE, VALOR_ILUMINACAO, PATH_IMG_DEFAULT, TAMANHO_IMG
import numpy as np

# # carrega xml com parametros
face_cascade = cv2.CascadeClassifier('xml/haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier('xml/haarcascade-eye.xml')

# capiturar video
cap = cv2.VideoCapture(0)

cont_capturadas = 1
qtd_fotos_capturadas = 25

id = input("Digite seu identificador: ")

while True:
    # ler frame
    conect, img = cap.read()

    if conect:
        # Convert em scala de cinza
        img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # detectar face
        faces = face_cascade.detectMultiScale(img_cinza, 1.1, 4)

        # construir retangulo na face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)

            capturar_olhos = img[y:y + h, x:x + w]
            capturar_cinza_olhos = cv2.cvtColor(capturar_olhos, cv2.COLOR_BGR2GRAY)
            olhos_detectados = eyes_cascade.detectMultiScale(capturar_cinza_olhos)
            for (ox, oy, ow, oh) in olhos_detectados:
                cv2.rectangle(capturar_olhos, (ox, oy), (ox + ow, oy + oh), WHITE)

                if cv2.waitKey(1) & 0xFF == ord("q") and np.average(img_cinza) > VALOR_ILUMINACAO:
                    try:
                        imagem_capturada = cv2.resize(img_cinza[y:y + h, x:x + w], TAMANHO_IMG)
                        nome_img_capturada = "{0}/{1}.{2}.jpg".format(PATH_IMG_DEFAULT, id, cont_capturadas)
                        cv2.imwrite(nome_img_capturada, imagem_capturada)
                        print(nome_img_capturada)
                        cont_capturadas += 1
                    except:
                        pass

        cv2.imshow('Captura de Imagens', img)
        cv2.waitKey(1)
        if cont_capturadas >= qtd_fotos_capturadas:
            break

    # fechar tela com ESC
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
