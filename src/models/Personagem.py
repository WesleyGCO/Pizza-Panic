from typing import Any
import pygame # type: ignore

from models.Objeto import Objeto
from servicos.jogo_servico import Jogo_Servico

class Personagem(Objeto):

    jogo_servico = Jogo_Servico()

    def __init__(self, cor, x, y, largura, altura, velocidade):
        super().__init__(x, y, largura, altura)
        self.cor = cor
        self.velocidade = velocidade
        self.itens_coletados = 0
        self.imagem_pizzaiolo = pygame.image.load("./assets/Imagens/pizzaiolo.svg")

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.posicao.x, self.posicao.y, self.altura, self.largura))
        #tela.blit(pygame.transform.scale(self.imagem_pizzaiolo, (self.posicao.x, self.posicao.y), (self.largura, self.altura)))

    def andar_esquerda(self):
        # Mover para a esquerda
        self.posicao.x -= self.velocidade

        # Limitar movimento para não ultrapassar as bordas da tela
        if self.posicao.x < 0:  # Se estiver à esquerda da tela
            self.posicao.x = 0

    def andar_direita(self, tela_altura):
        # Mover para a direita
        self.posicao.x += self.velocidade

        # Limitar movimento para não ultrapassar as bordas da tela
        if self.posicao.x < 0:  # Se estiver à esquerda da tela
            self.posicao.x = 0
        elif self.posicao.x + self.altura > tela_altura:  # Se estiver à direita da tela
            self.posicao.x = tela_altura - self.altura

    def coletar_item(self, pontuacao):
        # Adiciona o item coletado à lista de itens coletados
        self.itens_coletados += pontuacao

    
    def pegar_itens_coletados(self):
        return self.itens_coletados