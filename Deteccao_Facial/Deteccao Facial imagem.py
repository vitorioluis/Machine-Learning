# -*- coding: utf-8 -*-

from glob import glob

import cv2

# documentação do Opencv => https://opencv-python-tutroals.readthedocs.io


# cores
COR_RET_FACE = (0, 255, 0)
COR_RET_EYE = (255, 0, 0)

# obter os cascades em => https://github.com/opencv/opencv/tree/master/data/haarcascades
CLF_FACE = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')
CLF_EYE = cv2.CascadeClassifier('cascade/haarcascade_eye_tree_eyeglasses.xml')
FONT = cv2.FONT_HERSHEY_SIMPLEX

for image_path in glob('images/*jpg'):
    # ler imagem
    img = cv2.imread(image_path)

    # converte em cinza
    image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    faces = CLF_FACE.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

    # verifica se consegui detectar
    if len(faces) > 0:
        for x, y, w, h in faces:
            # desenha um retangulo no rosto
            img = cv2.rectangle(img, (x, y), (x + w, y + h), COR_RET_FACE, 2)

            # detecção de olhos
            r_gray = image_gray[y:y + h, x:x + w]
            r_color = img[y:y + h, x:x + w]

            # olhos abertos
            open_eyes = CLF_EYE.detectMultiScale(r_gray)
            for ex, ey, ew, eh in open_eyes:
                # desenha o retangulo nos olhos
                cv2.rectangle(r_color, (ex, ey), (ex + ew, ey + eh), COR_RET_EYE, 2)

        cv2.imshow(image_path, img)
        k = cv2.waitKey(30) & 0xff

        if k == 27:
            break


        cv2.destroyAllWindows()
