# -*- coding:utf-8 -*-
import os

import cv2
import numpy as np
from PIL import Image


def getImageWithID(path):
    img_paths = [os.path.join(path, f) for f in os.listdir(path)]
    lst_face = []
    lst_id = []
    for image_path in img_paths:
        face_image = Image.open(image_path).convert('L')  # Open image and convert to gray
        face_image = face_image.resize((110, 110))  # resize the image so the EIGEN recogniser can be trained
        face_np = np.array(face_image, 'uint8')  # convert the image to Numpy array
        ID = int(os.path.split(image_path)[-1].split('.')[1])  # Retreave the ID of the array
        lst_face.append(face_np)  # Append the Numpy Array to the list
        lst_id.append(ID)  # Append the ID to the IDs list
        cv2.imshow('Treinando Modelo', face_np)  # Show the images in the list
        cv2.waitKey(1)
    cv2.destroyAllWindows()
    return np.array(lst_id), lst_face  # The IDs are converted in to a Numpy array


if __name__ == "__main__":
    # diretorio das fotos
    path_fotos = 'dados/fotos'
    path_xml = 'dados/Reconhecimento'
    IDs, FaceList = getImageWithID(path_fotos)

    print('EIGEN')
    EigenFace = cv2.face.EigenFaceRecognizer_create(15)
    EigenFace.train(FaceList, IDs)
    EigenFace.save(os.path.join(path_xml, 'trainingDataEigan.xml'))

    print('FISHER')
    FisherFace = cv2.face.FisherFaceRecognizer_create(2)
    FisherFace.train(FaceList, IDs)
    FisherFace.save(os.path.join(path_xml, 'trainingDataFisher.xml'))

    print('LBPH')
    LBPHFace = cv2.face.LBPHFaceRecognizer_create(1, 1, 7, 7)
    LBPHFace.train(FaceList, IDs)
    LBPHFace.save(os.path.join(path_xml, 'trainingDataLBPH.xml'))

    print('treino dos modelos concluido...')

