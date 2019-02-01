# -*- coding: utf-8 -*-
import sys
from random import randint

import pygame
from pygame.locals import *


class ArkNoid_ai:
    def __init__(self):
        pygame.init()
        self.__img_nave = pygame.image.load('img/nav24.png')
        self.__img_base = pygame.image.load('img/base.png')
        self.__img_fundo = pygame.image.load('img/fundo.jpg')

        self.__resolucao_tela = 600, 480
        self.__screen = pygame.display.set_mode(self.__resolucao_tela)

        self.__screen.blit(self.__img_fundo, (0, 0))
        pygame.display.flip()

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

        self.__max_pa_x = self.__resolucao_tela[0]
        self.__pa_diametro = 90

        self.__nave_diametro = 70
        self.__nave_area = self.__nave_diametro / 2
        self.__max_nave_x = self.__resolucao_tela[0] - self.__nave_diametro
        self.__max_nave_y = self.__resolucao_tela[1] - self.__nave_diametro + 20

        self.__xpos = 310
        self.__ypos = self.__resolucao_tela[1]

        self.__menos, self.__mais = 5, 5

    def __iniciar_jogo(self):
        self.__time = pygame.time.Clock()
        self.__status = self.__status_nave_pa
        self.__lst_pos_nave = [5, -5]

        self.__base = pygame.Rect(300, self.__max_pa_x, self.__pa_diametro, self.__pa_diametro)
        self.__nave = pygame.Rect(300, self.__max_nave_y, self.__nave_diametro, self.__nave_diametro)

    def __movimentar_nave(self):
        self.__nave.left += self.__lst_pos_nave[0]
        self.__nave.top += self.__lst_pos_nave[1]

        if self.__nave.left <= 0:  # esquerda - 4
            print('4', self.__nave.left, self.__nave.top)
            self.__nave.left = 0
            self.__lst_pos_nave[0] = -self.__lst_pos_nave[0]
        elif self.__nave.left >= self.__max_nave_x:  # direita - 2
            print('2', self.__nave.left, self.__nave.top)
            self.__nave.left = self.__max_nave_x
            self.__lst_pos_nave[0] = -self.__lst_pos_nave[0]

        if self.__nave.top < 0:  # top - 3
            print('3', self.__nave.left, self.__nave.top)
            self.__nave.top = 0
            self.__lst_pos_nave[1] = -self.__lst_pos_nave[1]
        elif self.__nave.top >= self.__max_nave_y:  # bottom - 1
            print('1', self.__nave.left, self.__nave.top)
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
            # self.__screen.fill(self.__preto)

            self.__tecla = pygame.key.get_pressed()

            if self.__tecla[K_ESCAPE]:
                break

            if self.__tecla[K_RETURN] or self.__status == 1:
                self.__movimentar_nave()
                self.__movimentar_pa()
                self.__status = self.state_playing

            # atualizando img de fundo
            self.__screen.blit(self.__img_fundo, (0, 0))

            # movendo a img
            self.__screen.blit(self.__img_nave, (self.__nave.left, self.__nave.top))
            self.__screen.blit(self.__img_base, (self.__base.left, self.__base.top))

            pygame.display.flip()
            # pygame.display.update()


if __name__ == "__main__":
    gm = ArkNoid_ai()
    gm.main()
