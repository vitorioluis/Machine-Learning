# -*- coding: utf-8 -*-

import cv2
import numpy as np

import NameFind
from constantes import WHITE, CLF_FACE


def captura_fotos_novo_reconhecimento_facial():
    ID = NameFind.AddName()
    Count = 0
    cap = cv2.VideoCapture(0)  # camera do note

    while Count < 50:
        ret, img = cap.read()
        # Converte a camera em cinza
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # testando o brilho da img
        if np.average(gray) > 110:
            # Detectar os rostos e armazenar as posições
            faces = CLF_FACE.detectMultiScale(gray, 1.3, 5)
            # X, Y LARGURA, ALTURA
            for (x, y, w, h) in faces:
                # Reconhecimento do rosto e cortando a img
                FaceImage = gray[y - int(h / 2): y + int(h * 1.5), x - int(x / 2): x + int(w * 1.5)]
                Img = (NameFind.DetectEyes(FaceImage))
                cv2.putText(gray, "Rosto detectado", (x + int((w / 2)), y - 5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)
                if Img is not None:
                    # Mostra rosto detectado
                    frame = Img
                else:
                    frame = gray[y: y + h, x: x + w]
                cv2.imwrite("fotos/rosto." + str(ID) + "." + str(Count) + ".jpg", frame)
                cv2.waitKey(300)
                cv2.imshow("FOTO CAPTURADA", frame)
                Count = Count + 1
        cv2.imshow('Cadastro de fotos', gray)

        # finaliza com esc
        if cv2.waitKey(30) & 0xff == 27:
            break


    print('FOTOS CAPTURADAS COM SUCESSO COMPLETA')

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    captura_fotos_novo_reconhecimento_facial()
