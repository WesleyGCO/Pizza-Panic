import pygame # type: ignore

from typing import Any

from core.entities.Objeto import Objeto

class Personagem(Objeto):

    def __init__(self, cor, x, y, largura, altura, aceleracao):
        super().__init__(x, y, largura, altura)
        self.cor = cor
        self.itens_coletados = 0
        self.aceleracao.x = aceleracao
        self.imagem_pizzaiolo = pygame.image.load("./assets/Imagens/pizzaiolo.png")

    def desenhar(self, tela):
        # pygame.draw.rect(tela, self.cor, (self.posicao.x, self.posicao.y, self.altura, self.largura))
        #tela.blit(pygame.transform.scale(self.imagem_pizzaiolo, (self.posicao.x, self.posicao.y), (self.largura, self.altura)))
        tela.blit(pygame.transform.scale(self.imagem_pizzaiolo, (self.largura, self.altura)), (self.posicao.x, self.posicao.y))


    def atualiza_mov_esquerda(self, tempo, aceleracao):
        # Acelerar para a esquerda
        self.aceleracao.x = aceleracao
        self.velocidade.x = 0 

        self.velocidade.x = self.aceleracao.x * tempo

        if self.posicao.x == 0:
            self.posicao.x = 0
        else:
            self.posicao.x -= self.velocidade.x

    def atualiza_mov_direita(self, tempo, aceleracao, w_max):
        # Acelerar para a esquerda
        self.aceleracao.x = aceleracao
        self.velocidade.x = 0 

        if self.posicao.x == w_max + 100:
            self.posicao.x = w_max + 100
        else:
            # print(self.posicao.x)
            self.posicao.x += self.aceleracao.x * tempo

    def coletar_item(self, pontuacao):
        # Adiciona o item coletado à lista de itens coletados
        self.itens_coletados += pontuacao

    
    def pegar_itens_coletados(self):
        return self.itens_coletados