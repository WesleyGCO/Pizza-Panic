import pygame
from Vetor import Vetor

class Item(Vetor):
    def __init__(self, cor, tamanho_x, tamanho_y, velocidade, posicao_x, posicao_y, radius):
        super().__init__(cor, tamanho_x, tamanho_y, velocidade, posicao_x, posicao_y)
        self.radius = radius

    def desenhar(self, screen):
        pygame.draw.circle(screen, self.cor, (self.posicao_x, self.posicao_y), self.radius)
