from PIL import Image
from glob import glob


for img in glob(dir):
    imagem = Image.open(img)
    imagem = imagem.resize((32, 32), Image.ANTIALIAS)
    imagem.save(img)
