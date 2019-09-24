import cv2

# # carrega xml com parametros
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# # capiturar video
# cap = cv2.VideoCapture(0)
#
# while True:
#     # ler frame
#     _, img = cap.read()
#
#     # Convert em scala de cinza
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     # detectar face
#     faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#
#     # construir retangulo na face
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#
#     cv2.imshow('Video', img)
#
#     # fechar tela com ESC
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()

title = 'Reconhecimento Facial openCV - '
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('TestVid.wmv')
while True:
    ret, frame = cap.read()
    if ret:
        # converte em cinza
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(frame_gray, 1.3, 5)

        for x, y, w, h in faces:
            r_gray = cv2.resize((frame_gray[y:y + h, x:x + w]), (110, 110))
            # id_face, conf = modelo.predict(r_gray)
            # name_face = NameFind.ID2Name(id_face, conf)
            # NameFind.DispID(x, y, w, h, name_face, frame_gray)

        cv2.imshow(title, frame_gray)
        k = cv2.waitKey(30) & 0xff

        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()
