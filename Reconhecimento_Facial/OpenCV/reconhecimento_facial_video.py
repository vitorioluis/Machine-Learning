import cv2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (127, 255, 0)
BLUE = (255, 0, 0)

# # carrega xml com parametros
face_cascade = cv2.CascadeClassifier('xml/haarcascade_frontalface_default.xml')
face_eye = cv2.CascadeClassifier('xml/haarcascade_eye.xml')
face_smile = cv2.CascadeClassifier('xml/haarcascade_smile.xml')

# capiturar video
cap = cv2.VideoCapture(0)
texto = 'texto'

while True:
    # ler frame
    ret, img = cap.read()

    if ret:
        # Convert em scala de cinza
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # detectar face
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # construir retangulo na face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), WHITE, 2)
            cv2.rectangle(img, (int(x) - 1, int(y - 25)), (int(x + 10 + (len(texto) * 7)), int(y - 1)), WHITE, -2)
            cv2.putText(img, texto, (int(x) + 5, int(y - 10)), cv2.FONT_HERSHEY_DUPLEX, .4, BLACK)

            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            eyes = face_eye.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), GREEN, 1)

            # smile = face_smile.detectMultiScale(roi_gray)
            # for (sx, sy, sw, sh) in smile:
            #     cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 127, 255), 2)

    # mostrar video
    cv2.imshow('Video', img)

    # fechar tela com ESC
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
