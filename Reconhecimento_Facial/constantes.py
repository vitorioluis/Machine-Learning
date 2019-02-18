# -*- coding:utf-8 -*-
import cv2

# cores
WHITE = (255, 255, 255)
COR_FACE = (0, 255, 0)
COR_EYE = (255, 0, 0)

# obter os cascades em => https://github.com/opencv/opencv/tree/master/data/haarcascades
FACE_CASCADE = cv2.CascadeClassifier('dados/cascade/haarcascade_frontalface_default.xml')
EYE_CASCADE = cv2.CascadeClassifier('dados/cascade/haarcascade_eye_tree_eyeglasses.xml')
FONT = cv2.FONT_HERSHEY_DUPLEX

