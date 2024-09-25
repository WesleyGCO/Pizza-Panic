from adapters.primary import pygame_output_adapter
from application.models.Vetor import Vetor
import random, pygame # type: ignore

class Objeto:
    def __init__(self, x, y, largura, altura):
        self.posicao = Vetor(x, y)
        self.largura = largura
        self.altura = altura
        self.start_x = self.posicao.x
        self.start_y = self.posicao.y

        self.velocidade = Vetor(x=0,y=0)
        self.aceleracao = Vetor(x=0,y=0)

    def desenhar(self, tela, imagem):
        print("Desenhei")
        tela.blit(pygame.transform.scale(imagem, (self.largura, self.altura)), (self.posicao.x, self.posicao.y))


    def processamento_fisica(self, tempo):
        self.posicao.x += self.velocidade.x * tempo + self.aceleracao.x * (tempo**2) * 0.5 
        self.posicao.y += self.velocidade.y * tempo + self.aceleracao.y * (tempo**2) * 0.5

        self.velocidade.x += self.aceleracao.x * tempo
        self.velocidade.y += self.aceleracao.y * tempo

    def pontuacao(self):
        pass

    def contar_pedido(self):
        return 1