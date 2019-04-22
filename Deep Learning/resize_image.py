from PIL import Image
from glob import glob


def resize_img(dir, tamanho=(32, 32)):
    for img in glob(dir):
        imagem = Image.open(img)
        imagem = imagem.resize(tamanho, Image.ANTIALIAS)
        imagem.save(img)
