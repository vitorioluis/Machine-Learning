# -*- coding:utf-8 -*-
import os

import cv2
import numpy as np
from PIL import Image


def getImageWithID(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    FaceList = []
    IDs = []
    for imagePath in imagePaths:
        faceImage = Image.open(imagePath).convert('L')  # Open image and convert to gray
        faceImage = faceImage.resize((110, 110))  # resize the image so the EIGEN recogniser can be trained
        faceNP = np.array(faceImage, 'uint8')  # convert the image to Numpy array
        ID = int(os.path.split(imagePath)[-1].split('.')[1])  # Retreave the ID of the array
        FaceList.append(faceNP)  # Append the Numpy Array to the list
        IDs.append(ID)  # Append the ID to the IDs list
        cv2.imshow('Treinando Modelo', faceNP)  # Show the images in the list
        cv2.waitKey(1)
    return np.array(IDs), FaceList  # The IDs are converted in to a Numpy array


if __name__ == "__main__":
    # diretorio das fotos
    path = 'dados/fotos'
    cv2.face.EigenFaceRecognizer_create()
    IDs, FaceList = getImageWithID(path)

    print('EIGEN')
    EigenFace = cv2.face.EigenFaceRecognizer_create(15)
    EigenFace.train(FaceList, IDs)
    EigenFace.save('dados/Reconhecimento/trainingDataEigan.xml')

    print('FISHER')
    FisherFace = cv2.face.FisherFaceRecognizer_create(2)
    FisherFace.train(FaceList, IDs)
    FisherFace.save('dados/Reconhecimento/trainingDataFisher.xml')

    print('LBPH')
    LBPHFace = cv2.face.LBPHFaceRecognizer_create(1, 1, 7, 7)
    LBPHFace.train(FaceList, IDs)
    LBPHFace.save('dados/Reconhecimento/trainingDataLBPH.xml')

    print('treino dos modelos concluido...')
    cv2.destroyAllWindows()


