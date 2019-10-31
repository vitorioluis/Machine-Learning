import cv2
from config import GREEN, WHITE, TAMANHO_IMG
import pyautogui

# site de testes
# https://bitbucket.org/SpikeSL/vision-systems/src


face_cascade = cv2.CascadeClassifier('xml/haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
cam = cv2.VideoCapture(0)
# img = cv2.imread('img/photo.jpg')

while True:
    conect, img = cam.read()
    # Convert em scala de cinza
    img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detectar face
    faces = face_cascade.detectMultiScale(img_cinza, 1.1, 4)

    if conect:
        # construir retangulo na face
        for (x, y, w, h) in faces:
            # img_capturada = cv2.resize(img_cinza[y:y + h, x:x + w], TAMANHO_IMG)
            # cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)
            qpyautogui.moveTo(x, y, 1)

    cv2.imshow("Face", img)
    cv2.waitKey(1)

    # fechar tela com ESC
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()
