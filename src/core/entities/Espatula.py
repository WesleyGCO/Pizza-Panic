import pygame #type: ignore

from core.entities.Objeto import Objeto

class Espatula(Objeto):
    def __init__(self, x, y, largura, altura, vx, vy):
        super().__init__(x, y, largura, altura)
        self.vx = vx
        self.vy = vy
        self.imagem = pygame.image.load("./assets/Imagens/Espátula 300.png")

    def desenhar(self, tela):
        super().desenhar(tela, self.imagem)

    # def movimento_parabolico(self, gravidade):
    #     super().atualiza(self.vx, self.vy)
    #     self.vy += gravidade

    def reinicia(self):
        super().reinicia_item()

    def pontuacao(self):
        return -2