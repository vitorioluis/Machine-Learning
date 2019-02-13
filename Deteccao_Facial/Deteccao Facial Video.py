# -*- coding: utf-8 -*-
import cv2

# documentação do Opencv => https://opencv-python-tutroals.readthedocs.io

# cores
COR_RET_FACE = (0, 255, 0)
COR_RET_EYE = (255, 0, 0)

# obter os cascades em => https://github.com/opencv/opencv/tree/master/data/haarcascades
cascade_face_path = 'cascade/haarcascade_frontalface_default.xml'
cascade_eye_open_path = 'cascade/haarcascade_eye_tree_eyeglasses.xml'

# criar classificadores
clf_face = cv2.CascadeClassifier(cascade_face_path)
clf_eye_open = cv2.CascadeClassifier(cascade_eye_open_path)

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cap.read()
    if ret:
        # converte em cinza
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = clf_face.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # verifica se consegui detectar
        for x, y, w, h in faces:
            # desenha um retangulo no rosto
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), COR_RET_FACE, 2)
            cv2.putText(frame, 'Boiola', (x - 10, y - 10), font, 1, COR_RET_EYE, 2, cv2.LINE_AA)

            # detecção de olhos
            r_gray = frame_gray[y:y + h, x:x + w]
            r_color = frame[y:y + h, x:x + w]

            # olhos abertos
            open_eyes = clf_eye_open.detectMultiScale(r_gray)
            for ex, ey, ew, eh in open_eyes:
                # desenha o retangulo nos olhos
                cv2.rectangle(r_color, (ex, ey), (ex + ew, ey + eh), COR_RET_EYE, 2)

        cv2.imshow('Video', frame)
        k = cv2.waitKey(30) & 0xff

        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()
