import pygame
from Vetor import Vetor

class Personagem(Vetor):
    def __init__(self, cor, tamanho_x, tamanho_y, velocidade, posicao_x, posicao_y):
        super().__init__(cor, tamanho_x, tamanho_y, velocidade, posicao_x, posicao_y)

    def desenhar(self, screen):
        pygame.draw.rect(screen, self.cor, (self.posicao_x, self.posicao_y, self.tamanho_x, self.tamanho_y))

    def andar_direita(self):
        # Mover para a direita
        self.posicao_x += self.velocidade

        # Limitar movimento para não ultrapassar as bordas da tela
        largura_tela = 800  # Largura da tela
        if self.posicao_x < 0:  # Se estiver à esquerda da tela
            self.posicao_x = 0
        elif self.posicao_x + self.tamanho_x > largura_tela:  # Se estiver à direita da tela
            self.posicao_x = largura_tela - self.tamanho_x

    def andar_esquerda(self):
        # Mover para a esquerda
        self.posicao_x -= self.velocidade

            # Limitar movimento para não ultrapassar as bordas da tela
        if self.posicao_x < 0:  # Se estiver à esquerda da tela
            self.posicao_x = 0