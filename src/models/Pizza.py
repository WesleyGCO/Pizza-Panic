from models.Personagem import Personagem
import pygame # type: ignore
from models.Objeto import Objeto

class Pizza(Objeto):
    def __init__(self, x, y, largura, altura, vx, vy):
        super().__init__(x, y, largura, altura)
        self.vx = vx
        self.vy = vy
        self.imagem_pizza = pygame.image.load("./assets/Imagens/pizza.png")

    def desenhar(self, tela):
        super().desenhar(tela, self.imagem_pizza)

    def movimento_parabolico(self, gravidade):
        super().atualiza(self.vx, self.vy)
        self.vy += gravidade

    def reinicia(self):
        super().reinicia_item()

    def pontuacao(self):
        return 5