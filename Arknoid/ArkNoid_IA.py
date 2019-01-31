# -*- coding: utf-8 -*-
import sys

import pygame
from pygame.locals import *


class ArkNoid_ai:
    def __init__(self):
        pygame.init()
        self.__bola = pygame.image.load('img/bola.png')

        self.__tamanho_tela = 800, 600
        self.__screen = pygame.display.set_mode(self.__tamanho_tela)

        if pygame.font:
            self.font = pygame.font.Font(None, 25)
        else:
            self.font = None

        self.constantes()
        self.__iniciar_jogo()

    def constantes(self):
        self.__status_bola_pa, self.state_playing = 0, 1
        self.__preto = (0, 0, 0)
        self.__branco = (255, 255, 255)
        self.__vermelho = (255, 0, 0)

        self.__pa_largura, self.__pa_altura = 65, 12
        self.__pa_y = self.__tamanho_tela[1] - self.__pa_altura -10
        self.__max_pa_x = self.__tamanho_tela[0] - self.__pa_largura

        self.__raio_bola, self.__bola_diametro = 16, 16
        self.__bola_area = self.__bola_diametro / 2
        self.__max_bola_x = self.__tamanho_tela[0] - self.__bola_diametro
        self.__max_bola_y = self.__tamanho_tela[1] - self.__bola_diametro

        self.__xpos = 310
        self.__ypos = self.__pa_y - 16

        self.__menos, self.__mais = 5, 5

    def __iniciar_jogo(self):
        self.__clock = pygame.time.Clock()
        self.__status = self.__status_bola_pa
        self.__lst_pos_bola = [5, -5]
        self.__pa = pygame.Rect(283, self.__pa_y, self.__pa_largura, self.__pa_altura)
        self.__bola = pygame.Rect(300, self.__pa_y - self.__bola_diametro, self.__bola_diametro, self.__bola_diametro)

    def __movimentar_bola(self):
        self.__bola.left += self.__lst_pos_bola[0]
        self.__bola.top += self.__lst_pos_bola[1]

        if self.__bola.left <= 0:
            self.__bola.left = 0
            self.__lst_pos_bola[0] = -self.__lst_pos_bola[0]
        elif self.__bola.left >= self.__max_bola_x:
            self.__bola.left = self.__max_bola_x
            self.__lst_pos_bola[0] = -self.__lst_pos_bola[0]

        if self.__bola.top < 0:
            self.__bola.top = 0
            self.__lst_pos_bola[1] = -self.__lst_pos_bola[1]
        elif self.__bola.top >= self.__max_bola_y:
            self.__bola.top = self.__max_bola_y
            self.__lst_pos_bola[1] = -self.__lst_pos_bola[1]

    def __movimentar_pa(self):
        if self.__tecla[K_LEFT]:
            self.__pa.left -= self.__mais
            if self.__pa.left < 0:
                self.__pa.left = 0

        if self.__tecla[K_RIGHT]:
            self.__pa.left += self.__menos
            if self.__pa.left > self.__max_pa_x:
                self.__pa.left = self.__max_pa_x

    def main(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            self.__clock.tick(50)
            self.__screen.fill(self.__branco)

            self.__tecla = pygame.key.get_pressed()

            if self.__tecla[K_ESCAPE]:
                break

            if self.__tecla[K_RETURN] or self.__status == 1:
                self.__movimentar_bola()
                self.__movimentar_pa()
                self.__status=self.state_playing



            self.__screen.fill(self.__branco)

            self.__pa = pygame.draw.rect(self.__screen, self.__preto, self.__pa)
            self.__bola=pygame.draw.circle(self.__screen, self.__preto, (self.__bola.left + int(self.__raio_bola),
                                                            self.__bola.top + int(self.__raio_bola)),
                                                            int(self.__raio_bola))



            pygame.display.update()


if __name__ == "__main__":
    gm = ArkNoid_ai()
    gm.main()
