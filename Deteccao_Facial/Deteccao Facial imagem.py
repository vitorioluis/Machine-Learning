# -*- coding: utf-8 -*-

from glob import glob

import cv2

# documentação do Opencv => https://opencv-python-tutroals.readthedocs.io

# obter os cascades em => https://github.com/opencv/opencv/tree/master/data/haarcascades
cascade_face_path = 'cascade/haarcascade_frontalface_default.xml'
cascade_eye_open_path = 'cascade/haarcascade_eye_tree_eyeglasses.xml'

COR_RET_FACE = (0, 255, 0)
COR_RET_EYE = (255, 0, 0)

for image_path in glob('images/*jpg'):
    # ler imagem
    img = cv2.imread(image_path)

    # criar classificadores
    clf_face = cv2.CascadeClassifier(cascade_face_path)
    clf_eye_open = cv2.CascadeClassifier(cascade_eye_open_path)

    # converte em cinza
    image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    faces = clf_face.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

    # verifica se consegui detectar
    if len(faces) > 0:
        for x, y, w, h in faces:
            # desenha um retangulo no rosto
            img = cv2.rectangle(img, (x, y), (x + w, y + h), COR_RET_FACE, 2)

            # detecção de olhos
            r_gray = image_gray[y:y + h, x:x + w]
            r_color = img[y:y + h, x:x + w]

            # olhos abertos
            open_eyes = clf_eye_open.detectMultiScale(r_gray)
            for ex, ey, ew, eh in open_eyes:
                # desenha o retangulo nos olhos
                cv2.rectangle(r_color, (ex, ey), (ex + ew, ey + eh), COR_RET_EYE, 2)

        cv2.imshow('image', img)
        cv2.waitKey(0)

        cv2.destroyAllWindows()
