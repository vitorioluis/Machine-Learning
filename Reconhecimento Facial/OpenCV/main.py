import cv2
from config import GREEN, WHITE, TAMANHO_IMG

# site de testes
# https://bitbucket.org/SpikeSL/vision-systems/src

def reconhecer_face(modelo):
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
                img_capturada = cv2.resize(img_cinza[y:y + h, x:x + w], TAMANHO_IMG)
                cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)

                # PREDIÇÃO DO MODELO
                id, acc = modelo.predict(img_capturada)
                legenda = '{0} {1}'.format(str(id), str(acc))
                cv2.putText(img, legenda, (x, y + h + 30), font, 2, WHITE)

        cv2.imshow("Face", img)
        cv2.waitKey(1)

        # fechar tela com ESC
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    dic = {1: "EigenFace", 2: "FisherFace", 3: "LBPHFace"}
    modelo = None

    print("Escolha o algoritmo:")
    print("1 - EigenFace")
    print("2 - FisherFace")
    print("3 - LBPHFace\r")
    md = int(input("> "))

    print("Modelo escolhido " + dic[md] if md in dic else "Opção {0} desconhecida".format(md))

    if md == 1:
        modelo = cv2.face.EigenFaceRecognizer_create()
        modelo.read('modelos_treinados/class_eigen.face.yml')
    elif md == 2:
        modelo = cv2.face.FisherFaceRecognizer_create()
        modelo.read('modelos_treinados/class_ficher.face.yml')
    elif md == 3:
        modelo = cv2.face.LBPHFaceRecognizer_create()
        modelo.read('modelos_treinados/class_lbph.face.yml')
    else:
        print('Modelo não localizado')

    if modelo:
        reconhecer_face(modelo)
