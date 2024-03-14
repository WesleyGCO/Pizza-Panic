from entities.Vetor import Vetor

class Objeto:
    def __init__(self, x, y, largura, altura):
        self.posicao = Vetor(x, y)
        self.largura = largura
        self.altura = altura

    def desenhar(self, screen):
        pass

    def atualiza(self, vx, vy):
        self.posicao.x += vx
        self.posicao.y += vy

    def andar_esquerda(self):
        pass

    def andar_direita(self):
        pass

    def retorna_x(self):
        return Vetor(self.posicao.x)
    
    def retorna_y(self):
        return Vetor(self.posicao.y)