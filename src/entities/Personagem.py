from typing import Any
import pygame

from entities.Vetor import Vetor
from entities.ItemRuim import ItemRuim

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Personagem(Vetor):
    def __init__(self, cor, tamanho_x, tamanho_y, velocidade, posicao_x, posicao_y):
        super().__init_Personagem__(cor, tamanho_x, tamanho_y, velocidade, posicao_x, posicao_y)
        self.itens_coletados = 0

    def desenhar(self, screen):
        pygame.draw.rect(screen, self.cor, (self.posicao_x, self.posicao_y, self.tamanho_x, self.tamanho_y))

    def andar_esquerda(self):
        # Mover para a esquerda
        self.posicao_x -= self.velocidade

            # Limitar movimento para não ultrapassar as bordas da tela
        if self.posicao_x < 0:  # Se estiver à esquerda da tela
            self.posicao_x = 0

    def andar_direita(self):
        # Mover para a direita
        self.posicao_x += self.velocidade

        # Limitar movimento para não ultrapassar as bordas da tela
        if self.posicao_x < 0:  # Se estiver à esquerda da tela
            self.posicao_x = 0
        elif self.posicao_x + self.tamanho_x > SCREEN_WIDTH:  # Se estiver à direita da tela
            self.posicao_x = SCREEN_WIDTH - self.tamanho_x

    def coletar_item(self, itemRuim):
        # Adiciona o item coletado à lista de itens coletados
        self.itens_coletados += 1

    def pegar_itens_coletados(self):
        return self.itens_coletados