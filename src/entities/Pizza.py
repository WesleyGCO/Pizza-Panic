from entities.Personagem import Personagem
import pygame # type: ignore
from entities.Objeto import Objeto

class Pizza(Objeto):
    def __init__(self, x, y, largura, altura, vx, vy):
        super().__init__(x, y, largura, altura)
        self.vx = vx
        self.vy = vy
        self.imagem_pizza = pygame.image.load("./assets/Imagens/pizza.png")

    def desenhar(self, tela):
        tela.blit(pygame.transform.scale(self.imagem_pizza, (self.largura, self.altura)), (self.posicao.x, self.posicao.y))

    def movimento_parabolico(self, gravidade):
        self.atualiza(self.vx, self.vy)
        self.vy += gravidade

    def reinicia(self):
        super().reinicia_item()

    def pontuacao(self):
        return 5