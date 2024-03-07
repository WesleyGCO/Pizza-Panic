import pygame
from pygame.font import Font
from entities.Vetor import Vetor
from entities.ItemRuim import ItemRuim

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()

fonte = Font(None, 20)

class Personagem(Vetor):
    def __init__(self, cor, tamanho_x, tamanho_y, velocidade, posicao_x, posicao_y):
        super().__init__(cor, tamanho_x, tamanho_y, velocidade, posicao_x, posicao_y)
        self.itens_coletados = []     

    def desenhar(self, screen):
        pygame.draw.rect(screen, self.cor, (self.posicao_x, self.posicao_y, self.tamanho_x, self.tamanho_y))

        # Renderiza a quantidade de itens coletados
        texto_itens_coletados = f"+ {len(self.itens_coletados)}"
        
        superficie_texto = fonte.render(texto_itens_coletados, True, (255, 255, 255))
        # Desenha a superfície no topo da tela
        screen.blit(superficie_texto, (0, 0))

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
        self.itens_coletados.append(itemRuim)