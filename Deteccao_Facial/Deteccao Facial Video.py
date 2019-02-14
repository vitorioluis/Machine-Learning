# -*- coding:utf-8 -*-
import cv2
import numpy as np

import NameFind
from constantes import CLF_EYE, COR_EYE, FONT, WHITE, CLF_FACE, COR_FACE


# pip install opencv-python
# documentação do Opencv => https://opencv-python-tutroals.readthedocs.io





def deteccao_face_video():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if ret:
            # converte em cinza
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = CLF_FACE.detectMultiScale(frame_gray, 1.1, 5, minSize=(30, 30))

            for x, y, w, h in faces:
                # desenha um retangulo na face
                NameFind.draw_box(frame, x, y, w, h)
                cv2.putText(frame, '...', (x - 5, y - 10), FONT, 1, COR_EYE, 2)

                # detecção dos olhos
                r_gray = frame_gray[y:y + h, x:x + w]
                r_color = frame[y:y + h, x:x + w]

                open_eyes = CLF_EYE.detectMultiScale(r_gray)
                for ex, ey, ew, eh in open_eyes:
                    # desenha o retangulo nos olhos
                    NameFind.draw_box(r_color, ex, ey, ew, eh)

            cv2.imshow('Deteccao Facial', frame)
            k = cv2.waitKey(30) & 0xff

            if k == 27:
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    deteccao_face_video()
