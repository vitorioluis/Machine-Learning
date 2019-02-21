# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame.locals import *


class ArkNoid_ML:
    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Machine Learning - Luís Vitório")

        # Importação das imagens
        self.__img_nave = pygame.image.load('img/nave.png')
        self.__img_base = pygame.image.load('img/base.png')
        self.__img_fundo = pygame.image.load('img/fundo_800_600.jpg')

        # resolução da tela
        self.__resolucao_tela = 800, 600
        self.__screen = pygame.display.set_mode(self.__resolucao_tela)

        # definir imagem de fundo e atualizar
        self.__screen.blit(self.__img_fundo, (0, 0))
        pygame.display.flip()

        if pygame.font:
            self.font = pygame.font.Font(None, 25)
        else:
            self.font = pygame.font.SysFont('Sans', 25)

        self.__placar()
        self.constantes()
        self.__iniciar_jogo()

    def constantes(self):
        """
        Função com variáveis constantes utilizadas na classe

        """
        self.__verde = (100, 244, 158)
        self.__status_stop, self.status_play, self.status_pausa = 0, 1, 2

        # configurações da base
        self.__base_largura = 100
        self.__base_diametro = 90
        self.__base_altura = 12
        self.__base_max_x = self.__resolucao_tela[0] - self.__base_largura
        self.__base_max_y = self.__resolucao_tela[1] - self.__base_diametro
        self.__base_y = self.__resolucao_tela[1] - self.__base_largura * 2

        # configurações da nave
        self.__nave_diametro = 70
        self.__nave_area = self.__nave_diametro / 2
        self.__nave_max_x = self.__resolucao_tela[0] - self.__nave_diametro
        self.__nave_max_y = self.__resolucao_tela[1] - self.__nave_diametro + 20

        # posição inicial da nave
        self.__xpos = 310
        self.__ypos = self.__resolucao_tela[1]

    def __iniciar_jogo(self):
        # time de velociade do jogo
        self.__time = pygame.time.Clock()

        # incia o jogo com status stop para abrir a tela e não movimentar os objetos
        self.__status = self.__status_stop

        self._speed_game = 50
        self._fase = 1

        # exibe potuação na tela
        self.__placar()
        self.__pontos = [0, 0]
        self.__mostrar_pontuacao()

        # número de pixel que a imagem se moverá
        self.__lst_vel_nave = [5, -5]

        # inicia objetos na tela
        self.__base = pygame.Rect(
            self.sorteio(0, 700), self.__base_max_x, self.__base_largura, self.__base_largura)
        self.__nave = pygame.Rect(self.sorteio(0, 800), self.sorteio(
            0, 600), self.__nave_diametro, self.__nave_diametro)

    def __placar(self):
        # texto placar
        self.__sprite = pygame.sprite.Sprite()
        self.__sprite.image = self.__img_fundo
        self.__sprite.rect = self.__img_fundo.get_rect()

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
        elif self.__nave.left >= self.__nave_max_x:  # direita - 2
            self.__nave.left = self.__nave_max_x
            self.__lst_vel_nave[0] = -self.__lst_vel_nave[0]

        # top recebe 0 se valor de top for menor ou igual a 0
        if self.__nave.top < 0:  # top - 3
            self.__nave.top = 0
            self.__lst_vel_nave[1] = -self.__lst_vel_nave[1]
        elif self.__nave.top >= self.__nave_max_y:  # bottom - 1
            self.__nave.top = self.__nave_max_y
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
            if self.__base.left > self.__base_max_x:
                self.__base.left = self.__base_max_x

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
            self.__pontos=[0,0]
            self._speed_game += 50
            self._fase += 1

    def main(self):
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
            if self.__tecla[K_RETURN] or self.__status == self.status_play:
                self.__movimentar_nave()
                self.__colisoes()
                self.__status = self.status_play
                self.__mostrar_pontuacao()

            # atualizando img de fundo
            self.__screen.blit(self.__img_fundo, (0, 0))

            # movendo a imagens
            self.__nave = self.__screen.blit(self.__img_nave, (self.__nave.left, self.__nave.top))
            self.__base = self.__screen.blit(self.__img_base,
                                             (self.__base.left, self.__resolucao_tela[1] - 30))

            # atualiza a tela
            pygame.display.flip()


if __name__ == "__main__":
    gm = ArkNoid_ML()
    gm.main()
