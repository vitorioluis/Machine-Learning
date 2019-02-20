# -*- coding:utf-8 -*-
import cv2
import NameFind
from constantes import FACE_CASCADE


# documentação do Opencv
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html


def reconecimento_facial_video(modelo, tp):
    title = 'Reconhecimento Facial openCV - ' + tp
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture('TestVid.wmv')
    while True:
        ret, frame = cap.read()
        if ret:
            # converte em cinza
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = FACE_CASCADE.detectMultiScale(frame_gray, 1.3, 5)

            for x, y, w, h in faces:
                r_gray = cv2.resize((frame_gray[y:y + h, x:x + w]), (110, 110))
                id_face, conf = modelo.predict(r_gray)
                name_face = NameFind.ID2Name(id_face, conf)
                NameFind.DispID(x, y, w, h, name_face, frame_gray)

            cv2.imshow(title, frame_gray)
            k = cv2.waitKey(30) & 0xff

            if k == 27:
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    while True:
        print('-- Modelos de reconhecimento facial disponíveis --')

        print('1 - EIGEN')
        print('2 - FISHER')
        print('3 - LBPH')
        print('4 - Sair')

        x = int(input('Escolha uma opção: '))
        if x == 1:
            tp = 'EIGEN'
            modelo = cv2.face.EigenFaceRecognizer_create(15, 4000)
            modelo.read("dados/Reconhecimento/trainingDataEigan.xml")
        elif x == 2:
            tp = 'FISHER'
            modelo = cv2.face.FisherFaceRecognizer_create(2)
            modelo.read("dados/Reconhecimento/trainingDataFisher.xml")
        elif x == 3:
            tp = 'LBPH'
            modelo = cv2.face.LBPHFaceRecognizer_create(1, 1, 7, 7)
            modelo.read('dados/Reconhecimento/trainingDataLBPH.xml')
        elif x == 4:
            break
        else:
            print("\n------------------")
            print("Opção desconhecida")
            print("------------------\n")
            cv2.destroyAllWindows()

        if x <= 3:
            reconecimento_facial_video(modelo, tp)
