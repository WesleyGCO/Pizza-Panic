import pygame

class Vetor:
    def __init__(self, cor, tamanho_x, tamanho_y, velocidade, posicao_x, posicao_y):
        self.__cor = cor
        self.__tamanho_x = tamanho_x
        self.__tamanho_y = tamanho_y
        self.__velocidade = velocidade
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y

    def andar_esquerda(self):
        # Mover para a esquerda
        self.posicao_x -= self.__velocidade

            # Limitar movimento para não ultrapassar as bordas da tela
        if self.posicao_x < 0:  # Se estiver à esquerda da tela
            self.posicao_x = 0


    def andar_direita(self):
        # Mover para a direita
        self.posicao_x += self.__velocidade

        # Limitar movimento para não ultrapassar as bordas da tela
        largura_tela = 800  # Largura da tela
        if self.posicao_x < 0:  # Se estiver à esquerda da tela
            self.posicao_x = 0
        elif self.posicao_x + self.__tamanho_x > largura_tela:  # Se estiver à direita da tela
            self.posicao_x = largura_tela - self.__tamanho_x



    def desenhar(self, screen):
        pygame.draw.rect(screen, self.__cor, (self.posicao_x, self.posicao_y, self.__tamanho_x, self.__tamanho_y))
