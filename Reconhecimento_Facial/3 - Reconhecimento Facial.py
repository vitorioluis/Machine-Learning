# -*- coding:utf-8 -*-
import cv2

import NameFind
from constantes import CLF_FACE

# documentação do Opencv
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html


def deteccao_face_video(modelo):
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture('TestVid.wmv')
    ID = 0
    while True:
        ret, frame = cap.read()
        if ret:
            # converte em cinza
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = CLF_FACE.detectMultiScale(frame_gray, 1.3, 5)

            for x, y, w, h in faces:
                r_gray = cv2.resize((frame_gray[y:y + h, x:x + w]), (110, 110))
                ID, conf = modelo.predict(r_gray)  # Determine the ID of the photo
                NAME = NameFind.ID2Name(ID, conf)
                NameFind.DispID(x, y, w, h, NAME, frame_gray)

            cv2.imshow('Reconhecimento Facial openCV', frame_gray)
            k = cv2.waitKey(30) & 0xff

            if k == 27:
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":

    print('-- Modelos de reconhecimento facial --')
    print('1 - EIGEN')
    print('2 - FISHER')
    print('3 - LBPH')

    x = int(input('Escolha uma opção: '))
    if x == 1:
        modelo = cv2.face.EigenFaceRecognizer_create(15, 4000)
        modelo.read("Reconhecimento/trainingDataEigan.xml")
    elif x == 2:
        modelo = cv2.face.FisherFaceRecognizer_create(2)
        modelo.read("Reconhecimento/trainingDataFisher.xml")
    elif x == 3:
        modelo = cv2.face.LBPHFaceRecognizer_create(1, 1, 7, 7)
        modelo.read('Reconhecimento/trainingDataLBPH.xml')
    else:
        print("Opção desconhecida")
        cv2.destroyAllWindows()


    deteccao_face_video(modelo)
