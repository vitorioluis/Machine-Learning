# -*- coding: utf-8 -*-
"""
Código original e documentações:
http://codentronix.com/2011/04/14/game-programming-with-python-and-pygame-making-breakout/
"""
import os
import random
import sys

import pygame
from pygame.locals import *

_RESOLUCAO_TELA = 800, 600
_STATUS_PAUSE, _STATUS_PLAY = 0, 1

# configurações da base
_BASE_LARGURA = 100
_BASE_MAX_Y = _RESOLUCAO_TELA[1] - 30
_BASE_MAX_X = _RESOLUCAO_TELA[0] - _BASE_LARGURA

# configurações da nave
_NAVE_DIAMETRO = 70
_NAVE_MAX_X = _RESOLUCAO_TELA[0] - _NAVE_DIAMETRO
_NAVE_MAX_Y = _RESOLUCAO_TELA[1] - _NAVE_DIAMETRO + 20

BRICK_WIDTH, BRICK_HEIGHT, BRICK_COLOR = 60, 15, (200, 200, 0)


class Arcade:
    def __init__(self):

        # centraliza janela
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        # inicia a tela
        pygame.init()
        pygame.display.set_caption("Machine Learning - Luís Vitório")

        # imagens
        self.__img_nave = pygame.image.load('img/nave.png')
        self.__img_base = pygame.image.load('img/base.png')
        self.__img_fundo = pygame.image.load('img/fundo_800_600.jpg')

        # resolução de tela
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

        self._txt_dados_salvos = os.path.join(self.__dir_dataset, 'dados.txt')
        self.__iniciar_jogo()

    def __iniciar_jogo(self):
        # time de velociade do jogo
        self.__time = pygame.time.Clock()

        # incia o jogo com status stop para abrir a tela e não movimentar os objetos
        self.__status_jogo = _STATUS_PAUSE

        # velocidade e fase inicial
        self._speed_game = 50
        self._fase = 1

        # posição
        self.lst_pos_nave = [0, 0, 0, 0]  # direita, esquerda, cima, baixo

        # exibe potuação na tela
        self.__pontos = [0, 0]
        self.__mostrar_pontuacao()

        # número de pixel que a imagem se moverá
        self.__lst_speed = [5, -5]

        # Coleta dados do jogo
        self._dic = {}

        # inicia objetos na tela
        self.__base = pygame.Rect(Arcade.__sorteio(), _BASE_MAX_X, _BASE_LARGURA, _BASE_LARGURA)
        self.__nave = pygame.Rect(Arcade.__sorteio(), 0, _NAVE_DIAMETRO, _NAVE_DIAMETRO)
        # self.criar_tijolos_aleatorios()

    def criar_tijolos_aleatorios(self):
        self.bricks = []
        qtd_tijolos = random.randint(2, 5)
        for i in range(qtd_tijolos):
            x_ofs, y_ofs = random.randint(35, 100), random.randint(35, 500)
            self.bricks.append((x_ofs, y_ofs))

        for brick in self.bricks:
            print(brick)
            self.__screen.blit(self.__img_base, brick)

    @staticmethod
    def __sorteio(x=0, y=700):
        '''
         sorteio da posição dos objetos da tela
        '''
        return random.randint(x, y)

    def __movimentar_base(self):
        """
            Movimenta a base
        """

        # movimenta direita
        if self.__tecla[K_LEFT]:
            self.__base.left -= 5
            if self.__base.left < 0:
                self.__base.left = 0

        # movimenta esquerda
        if self.__tecla[K_RIGHT]:
            self.__base.left += 5
            if self.__base.left > _BASE_MAX_X:
                self.__base.left = _BASE_MAX_X

    def __movimentar_nave(self):
        """
            Função para movimentar a nave automaticamente e colher dados para
            o Machine Learning além de determinar limites para a nave
        """

        self.__nave.left += self.__lst_speed[0]
        self.__nave.top += self.__lst_speed[1]

        if self.__nave.left <= 0:
            self.__nave.left = 0
            self.__lst_speed[0] = -self.__lst_speed[0]
        elif self.__nave.left >= _NAVE_MAX_X:
            self.__nave.left = _NAVE_MAX_X
            self.__lst_speed[0] = -self.__lst_speed[0]

        if self.__nave.top < 0:
            self.__nave.top = 0
            self.__lst_speed[1] = -self.__lst_speed[1]
        elif self.__nave.top >= _NAVE_MAX_Y:
            self.__nave.top = _NAVE_MAX_Y
            self.__lst_speed[1] = -self.__lst_speed[1]

    def __colisoes(self):
        """
            Verifica a colisão com a base
        """
        if self.__nave.colliderect(self.__base):
            self.__pontos[1] += 1
            self.__lst_speed[1] = -self.__lst_speed[1]

    def __mostrar_pontuacao(self):
        """
        Methodo responsável exibir pontuação
        """
        f = "Fase: {0}".format(str(self._fase))
        f += ' Jogo {0} x {1} I.A '.format(str(self.__pontos[0]), str(self.__pontos[1]))
        pygame.display.set_caption("Machine Learning - " + f)

        # if self.__pontos[1] == 10:
        #     self.__pontos = [0, 0]
        #     self._fase += 1


    def __salvar_dados_jogo(self):
        # salvar dados para machine learning
        with open(self._txt_dados_salvos, 'w+') as txt:
            for lst in self._dic.values():
                txt.write(''.join(str(lst).replace('[', '').replace(']', '')) + '\n')
        del self._dic

    def run(self):
        """
            função principal onde incia o jogo
        """
        top, botton, left, rigth = 0, 0, 0, 0
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

            # o break interrompe o while finalizando o jogo ao teclar o esc
            if self.__tecla[K_ESCAPE]:
                self.__salvar_dados_jogo()
                break

            if self.__tecla[K_SPACE]:
                self.__status_jogo = _STATUS_PLAY if self.__status_jogo == 0 else _STATUS_PAUSE

            # se o status for igual a 1 e a tecla enter precionada inicia os movimentos da tela
            if self.__tecla[K_RETURN] or self.__status_jogo == _STATUS_PLAY:
                self.__movimentar_nave()
                self.__movimentar_base()
                self.__colisoes()
                self.__status_jogo = _STATUS_PLAY
                self.__mostrar_pontuacao()

            # atualizando img de fundo
            self.__screen.blit(self.__img_fundo, (0, 0))

            # movendo a imagens
            self.__nave = self.__screen.blit(self.__img_nave, (self.__nave.left, self.__nave.top))
            self.__base = self.__screen.blit(self.__img_base, (self.__base.left, _BASE_MAX_Y))

            # atualiza a tela
            pygame.display.flip()

            # dados para machine learning
            left = self.__nave.left if self.__nave.left > _RESOLUCAO_TELA[0] / 2 else left
            rigth = self.__nave.left if self.__nave.left < _RESOLUCAO_TELA[0] / 2 else rigth

            top = self.__nave.top if self.__nave.top < _RESOLUCAO_TELA[1] / 2 else top
            botton = self.__nave.top if self.__nave.top > _RESOLUCAO_TELA[1] / 2 else botton

            if botton >= 500:
                self._dic[len(self._dic) + 1] = [left, rigth, top, botton]


if __name__ == "__main__":
    gm = Arcade()
    gm.run()
