import cv2
import os
import numpy as np
from config import PATH_IMG_DEFAULT

from cv2.face import EigenFaceRecognizer_create
from cv2.face import FisherFaceRecognizer_create
from cv2.face import LBPHFaceRecognizer_create


def get_img_id():
    __lst_ids, __lst_face = [], []
    __lst_path = [os.path.join(PATH_IMG_DEFAULT, path) for path in os.listdir(PATH_IMG_DEFAULT)]
    for path in __lst_path:
        img_face = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(path)[-1].split('.')[0])
        __lst_ids.append(id)
        __lst_face.append(img_face)
        # cv2.imshow("Face", img_face)
        # cv2.waitKey(50)
    return np.array(__lst_ids), __lst_face


lst_ids, lst_face = get_img_id()

eigen_face = EigenFaceRecognizer_create()
eigen_face.train(lst_face, lst_ids)
eigen_face.write('modelos_treinados/class_eigen.face.yml')

ficher_face = FisherFaceRecognizer_create()
ficher_face.train(lst_face, lst_ids)
ficher_face.write('modelos_treinados/class_ficher.face.yml')

lbph_face = LBPHFaceRecognizer_create()
lbph_face.train(lst_face, lst_ids)
lbph_face.write('modelos_treinados/class_lbph.face.yml')
