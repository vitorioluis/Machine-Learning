# -*- coding:utf-8 -*-
import cv2

import NameFind
from constantes import CLF_EYE, CLF_FACE

# pip install opencv-python
# documentação do Opencv => https://opencv-python-tutroals.readthedocs.io


recognise = cv2.face.EigenFaceRecognizer_create(15, 4000)  # creating EIGEN FACE RECOGNISER
recognise.read("Recogniser/trainingDataEigan.xml")


def deteccao_face_video():
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
                eyes = CLF_EYE.detectMultiScale(r_gray)
                for (ex, ey, ew, eh) in eyes:
                    ID, conf = recognise.predict(r_gray)  # Determine the ID of the photo
                    NAME = NameFind.ID2Name(ID, conf)
                    NameFind.DispID(x, y, w, h, NAME, frame_gray)

            cv2.imshow('Deteccao Facial', frame_gray)
            k = cv2.waitKey(30) & 0xff

            if k == 27:
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    deteccao_face_video()
