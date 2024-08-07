import pygame # type: ignore

from core.entities.Objeto import Objeto

class Pizza(Objeto):
    def __init__(self, x, y, largura, altura, vx, vy):
        super().__init__(x, y, largura, altura)
        self.vx = vx
        self.vy = vy
        # self.aceleracao.y = 1000
        self.imagem = pygame.image.load("./assets/Imagens/pizza.png")

    def desenhar(self, tela):
        super().desenhar(tela, self.imagem)

    def reinicia(self):
        super().reinicia_item()

    def pontuacao(self):
        return 5