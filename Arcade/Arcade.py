# -*- coding: utf-8 -*-
import os
import random
import sys

import pygame
from pygame.locals import *

_RESOLUCAO_TELA = 800, 600

_VERDE = (100, 244, 158)
_STATUS_STOP, _STATUS_PLAY = 0, 1

# configurações da base
_BASE_LARGURA = 100
_BASE_MAX_X = _RESOLUCAO_TELA[0] - _BASE_LARGURA

# configurações da nave
_NAVE_DIAMETRO = 70
_NAVE_MAX_X = _RESOLUCAO_TELA[0] - _NAVE_DIAMETRO
_NAVE_MAX_Y = _RESOLUCAO_TELA[1] - _NAVE_DIAMETRO + 20


class Arcade:
    def __init__(self):

        # centraliza janela
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        pygame.init()
        pygame.display.set_caption("Machine Learning - Luís Vitório")

        # imagens
        self.__img_nave = pygame.image.load('img/nave.png')
        self.__img_base = pygame.image.load('img/base.png')
        self.__img_fundo = pygame.image.load('img/fundo_800_600.jpg')

        self.__screen = pygame.display.set_mode(_RESOLUCAO_TELA)

        # definir imagem de fundo e atualizar
        self.__screen.blit(self.__img_fundo, (0, 0))
        pygame.display.flip()

        if pygame.font:
            self.font = pygame.font.Font(None, 25)
        else:
            self.font = pygame.font.SysFont('Sans', 25)

        # verifica se existe o diretório caso contrário cria
        # diretório para a base com os dados de aprendizado
        self.__dir_dataset = 'dataset'
        if os.path.exists(self.__dir_dataset) is False:
            os.mkdir(self.__dir_dataset)

        self.__iniciar_jogo()

    def __iniciar_jogo(self):
        # time de velociade do jogo
        self.__time = pygame.time.Clock()

        # incia o jogo com status stop para abrir a tela e não movimentar os objetos
        self.__status_jogo = _STATUS_STOP

        self._speed_game = 50
        self._fase = 1

        # exibe potuação na tela
        self.__pontos = [0, 0]
        self.__mostrar_pontuacao()

        # número de pixel que a imagem se moverá
        self.__lst_vel_nave = [5, -5]

        # inicia objetos na tela
        self.__base = pygame.Rect(self.sorteio(0, 700), _BASE_MAX_X, _BASE_LARGURA, _BASE_LARGURA)
        self.__nave = pygame.Rect(self.sorteio(0, 800), self.sorteio(0, 500), _NAVE_DIAMETRO, _NAVE_DIAMETRO)

    # def __placar(self):
    #     # texto placar
    #     self.__sprite = pygame.sprite.Sprite()
    #     self.__sprite.image = self.__img_fundo
    #     self.__sprite.rect = self.__img_fundo.get_rect()

    # sorteio da posição dos objetos da tela
    def sorteio(self, x, y):
        return random.randint(x, y)

    def __movimentar_nave(self):
        """
        Função para movimentar a nave automaticamente e colher dados para
        o Machine Learning além de determinar limites para a nave
        """

        # recebe valores setados na lista incrementando para movimentar
        self.__nave.left += self.__lst_vel_nave[0]
        self.__nave.top += self.__lst_vel_nave[1]

        # esquerda recebe 0 e add negativo para movimentar para direita
        if self.__nave.left <= 0:  # esquerda - 4
            self.__nave.left = 0
            self.__lst_vel_nave[0] = -self.__lst_vel_nave[0]

        # direita recebe 0 e add
        elif self.__nave.left >= _NAVE_MAX_X:  # direita - 2
            self.__nave.left = _NAVE_MAX_X
            self.__lst_vel_nave[0] = -self.__lst_vel_nave[0]

        # top recebe 0 se valor de top for menor ou igual a 0
        if self.__nave.top < 0:  # top - 3
            self.__nave.top = 0
            self.__lst_vel_nave[1] = -self.__lst_vel_nave[1]
        elif self.__nave.top >= _NAVE_MAX_Y:  # bottom - 1
            self.__nave.top = _NAVE_MAX_Y
            self.__lst_vel_nave[1] = -self.__lst_vel_nave[1]
            self.__pontos[0] += 1

    def __movimentar_base(self):
        """
            Movimenta a base
        """
        __menos, __mais = 5, 5
        if self.__tecla[K_LEFT]:
            self.__base.left -= __mais
            if self.__base.left < 0:
                self.__base.left = 0

        if self.__tecla[K_RIGHT]:
            self.__base.left += __menos
            if self.__base.left > _BASE_MAX_X:
                self.__base.left = _BASE_MAX_X

    def __colisoes(self):
        """
            Verifica a colisão
        """
        if self.__nave.colliderect(self.__base):
            self.__lst_vel_nave[1] = -self.__lst_vel_nave[1]
            self.__pontos[1] += 1
            print(self.__base[0])

    def __mostrar_pontuacao(self):
        """
        Methodo responsável exibir pontuação
        """
        f = "Fase: {0}".format(str(self._fase))
        f += ' Jogo {0} x {1} I.A '.format(str(self.__pontos[0]), str(self.__pontos[1]))
        pygame.display.set_caption("Machine Learning - " + f)

        if self.__pontos[1] == 10:
            self.__pontos = [0, 0]
            self._speed_game += 50
            self._fase += 1

    def run(self):
        """
            função que principal onde incia o jogo
        """
        while True:
            # pega eventos para finalizar a tela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Seta valor inicial para velocidade do jogo
            self.__time.tick(self._speed_game)

            # Captura a tecla precionada
            self.__tecla = pygame.key.get_pressed()
            self.__movimentar_base()

            # o break interrompe o while finalizando o jogo ao teclar o esc
            if self.__tecla[K_ESCAPE]:
                break

            # se o status for igual a 1 e a tecla enter precionada inicia os movimentos da tela
            if self.__tecla[K_RETURN] or self.__status_jogo == _STATUS_PLAY:
                self.__movimentar_nave()
                self.__colisoes()
                self.__status_jogo = _STATUS_PLAY
                self.__mostrar_pontuacao()

            # atualizando img de fundo
            self.__screen.blit(self.__img_fundo, (0, 0))

            # movendo a imagens
            self.__nave = self.__screen.blit(self.__img_nave, (self.__nave.left, self.__nave.top))
            self.__base = self.__screen.blit(self.__img_base, (self.__base.left, _RESOLUCAO_TELA[1] - 30))

            # atualiza a tela
            pygame.display.flip()


if __name__ == "__main__":
    gm = Arcade()
    gm.run()
