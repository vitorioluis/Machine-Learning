# -*- coding: utf-8 -*-
import sys
from random import randint

import pygame
from pygame.locals import *


class ArkNoid_ai:
    def __init__(self):
        pygame.init()
        self.__img_nave = pygame.image.load('img/nave.png')
        self.__img_base = pygame.image.load('img/base.png')

        self.__resolucao_tela = 640, 480
        self.__screen = pygame.display.set_mode(self.__resolucao_tela)

        if pygame.font:
            self.font = pygame.font.Font(None, 25)
        else:
            self.font = None

        self.constantes()
        self.__iniciar_jogo()

    def constantes(self):
        self.__status_nave_pa, self.state_playing = 0, 1
        self.__preto = (0, 0, 0)
        self.__branco = (255, 255, 255)
        self.__vermelho = (255, 0, 0)

        self.__nave_largura, self.__nave_altura = 0, 0
        # self.__nave_y = self.__resolucao_tela[1]
        self.__max_pa_x = self.__resolucao_tela[0] - self.__nave_largura

        self.__nave_diametro = 95
        self.__nave_area = self.__nave_diametro / 2
        self.__max_nave_x = self.__resolucao_tela[0] - self.__nave_diametro
        self.__max_nave_y = self.__resolucao_tela[1] - self.__nave_diametro + 20

        self.__xpos = 310
        self.__ypos = randint(100, self.__resolucao_tela[1] - self.__nave_altura)

        self.__menos, self.__mais = 5, 5

    def __iniciar_jogo(self):
        self.__time = pygame.time.Clock()
        self.__status = self.__status_nave_pa
        self.__lst_pos_nave = [5, -5]
        # self.__base = pygame.Rect(283, self.__nave_y, self.__nave_largura, self.__nave_altura)
        self.__nave = pygame.Rect(300, self.__max_nave_y, self.__nave_diametro, self.__nave_diametro)

    def __movimentar_nave(self):
        self.__nave.left += self.__lst_pos_nave[0]
        self.__nave.top += self.__lst_pos_nave[1]

        if self.__nave.left <= 0:
            print(self.__nave.left, self.__nave.top)
            self.__nave.left = 0
            self.__lst_pos_nave[0] = -self.__lst_pos_nave[0]
        elif self.__nave.left >= self.__max_nave_x:
            print(self.__nave.left, self.__nave.top)
            self.__nave.left = self.__max_nave_x
            self.__lst_pos_nave[0] = -self.__lst_pos_nave[0]

        if self.__nave.top < 0:
            print(self.__nave.left, self.__nave.top)
            self.__nave.top = 0
            self.__lst_pos_nave[1] = -self.__lst_pos_nave[1]
        elif self.__nave.top >= self.__max_nave_y:
            print(self.__nave.left, self.__nave.top)
            self.__nave.top = self.__max_nave_y
            self.__lst_pos_nave[1] = -self.__lst_pos_nave[1]

    def __movimentar_pa(self):
        if self.__tecla[K_LEFT]:
            self.__base.left -= self.__mais
            if self.__base.left < 0:
                self.__base.left = 0

        if self.__tecla[K_RIGHT]:
            self.__base.left += self.__menos
            if self.__base.left > self.__max_pa_x:
                self.__base.left = self.__max_pa_x

    def main(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.__time.tick(50)
            self.__screen.fill(self.__branco)

            self.__tecla = pygame.key.get_pressed()

            if self.__tecla[K_ESCAPE]:
                break

            if self.__tecla[K_RETURN] or self.__status == 1:
                self.__movimentar_nave()
                self.__movimentar_pa()
                self.__status = self.state_playing

            self.__screen.fill(self.__branco)

            self.__screen.blit(self.__img_nave, (self.__nave.left, self.__nave.top))
            # self.__screen.blit(self.__base_img,(self.__nave.left + int(self.__nave), self.__nave.top + int(self.__raio_nave))                              )
            #
            # self.__nave = pygame.draw.rect(self.__screen, self.__preto, self.__nave)
            # # self.__nave=pygame.draw.circle(self.__screen, self.__preto, (self.__nave.left + int(self.__raio_nave),
            #                                                 self.__nave.top + int(self.__raio_nave)),
            #                                                 int(self.__raio_nave))

            pygame.display.update()


if __name__ == "__main__":
    gm = ArkNoid_ai()
    gm.main()
