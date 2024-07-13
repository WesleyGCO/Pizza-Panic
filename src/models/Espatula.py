from models.Objeto import Objeto
import pygame # type: ignore

class Espatula(Objeto):
    def __init__(self, x, y, largura, altura, vx, vy):
        super().__init__(x, y, largura, altura)
        self.vx = vx
        self.vy = vy
        self.imagem_espatula = pygame.image.load("./assets/Imagens/Espátula 300.png")

    def desenhar(self, tela):
        super().desenhar(tela, self.imagem_espatula)

    def movimento_parabolico(self, gravidade):
        super().atualiza(self.vx, self.vy)
        self.vy += gravidade

    def reinicia(self):
        super().reinicia_item()

    def pontuacao(self):
        return -2