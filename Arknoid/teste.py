# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

pygame.init()

vermelho = (255, 0, 0)
preto = (0, 0, 0)

comprimento_ecra = 640
altura_ecra = 480

ecra = pygame.display.set_mode((comprimento_ecra, altura_ecra))

raio_circulo = 10

xpos = 50
ypos = 50

circulo = pygame.draw.circle(ecra, vermelho, (xpos, ypos), raio_circulo)

movimento_em_x = 5
movimento_em_y = 5

pygame.display.flip()

pygame.key.set_repeat(100, 100)

while True:
    for event in pygame.event.get():
        pass

    tecla_pressionada = pygame.key.get_pressed()

    if tecla_pressionada[K_LEFT]:
        xpos -= movimento_em_x

    if tecla_pressionada[K_RIGHT]:
        xpos += movimento_em_x

    if tecla_pressionada[K_UP]:
        ypos -= movimento_em_y

    if tecla_pressionada[K_DOWN]:
        ypos += movimento_em_y

    ecra.fill(preto)
    circulo = pygame.draw.circle(ecra, vermelho, (xpos, ypos), raio_circulo)
    pygame.display.flip()
