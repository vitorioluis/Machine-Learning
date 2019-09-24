from PIL import Image
import os


def resize_img(dir, tamanho=(32, 32)):
    for path, subdirs, files in os.walk(dir):
        for img in files:
            if img[-3:] in ('jpg','png'):
                imagem = Image.open(img)
                imagem = imagem.resize(tamanho, Image.ANTIALIAS)
                imagem.save(img)




