from entities.Vetor import Vetor
import random

class Objeto:
    def __init__(self, x, y, largura, altura):
        self.posicao = Vetor(x, y)
        self.largura = largura
        self.altura = altura
        self.start_x = self.posicao.x
        self.start_y = self.posicao.y

    def desenhar(self, screen):
        pass

    def atualiza(self, vx, vy):
        self.posicao.x += vx
        self.posicao.y += vy

    def reinicia_item(self):
        self.posicao.x = self.start_x
        self.posicao.y = self.start_y
        self.vx = random.uniform(2, 5)
        self.vy = -12

    def andar_esquerda(self):
        pass

    def andar_direita(self):
        pass

    def pontuacao(self):
        pass