# -*- coding: utf-8 -*-

import cv2
import numpy as np

import NameFind
from constantes import WHITE, FACE_CASCADE, FONT


def captura_fotos_novo_reconhecimento_facial():
    num_fotos_captura = 50  # número de fotos a ser capturadas
    id_name = NameFind.AddName()  # busca o id do nome no cadastro
    cap = cv2.VideoCapture(0)  # camera do note
    count = 0

    while count < num_fotos_captura:
        ret, img = cap.read()
        # Converte a camera em cinza
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # testando o brilho da img
        if np.average(gray) > 110:
            # Detectar os rostos e armazenar as posições
            faces = FACE_CASCADE.detectMultiScale(gray, 1.3, 5)
            # X, Y LARGURA, ALTURA
            for (x, y, w, h) in faces:
                # Reconhecimento do rosto e cortando a img
                face_image = gray[y - int(h / 2): y + int(h * 1.5), x - int(x / 2): x + int(w * 1.5)]
                img = (NameFind.DetectEyes(face_image))
                cv2.putText(gray, "ROSTO DETECTADO", (x+int((w/2)), y-5), FONT, .4, WHITE)
                if img is not None:
                    # Mostra rosto detectado
                    frame = img
                else:
                    frame = gray[y: y + h, x: x + w]
                cv2.imwrite("dados/fotos/" + str(id_name) + "." + str(count) + ".jpg", frame)
                cv2.waitKey(300)
                cv2.imshow("#", frame)
                count += 1
        cv2.imshow('Caputura de fotos', gray)

        # finaliza com esc
        if cv2.waitKey(30) & 0xff == 27:
            break

    print('FOTOS CAPTURADAS COM SUCESSO!')

    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    captura_fotos_novo_reconhecimento_facial()
