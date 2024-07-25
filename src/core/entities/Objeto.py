from core.entities.Vetor import Vetor
import random, pygame # type: ignore

class Objeto:
    def __init__(self, x, y, largura, altura):
        self.posicao = Vetor(x, y)
        self.largura = largura
        self.altura = altura
        self.start_x = self.posicao.x
        self.start_y = self.posicao.y

        self.velocidade = Vetor(x=0,y=0)
        self.aceleracao = Vetor(x,y)

    def desenhar(self, tela, imagem):
        tela.blit(pygame.transform.scale(imagem, (self.largura, self.altura)), (self.posicao.x, self.posicao.y))

    def atualiza(self, vx, vy, tempo):
        self.posicao.x += vx * tempo
        self.posicao.y += vy * tempo

    def movimento_parabolico(self, aceleracao, tempo):
        self.atualiza(self.vx, self.vy, tempo)
        self.vy += aceleracao

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

    def contar_pedido(self):
        return 1