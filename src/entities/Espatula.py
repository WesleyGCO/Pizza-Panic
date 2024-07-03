from entities.Objeto import Objeto
import pygame

class Espatula(Objeto):
    def __init__(self, x, y, largura, altura, vx, vy):
        super().__init__(x, y, largura, altura)
        self.vx = vx
        self.vy = vy
        self.imagem_espatula = pygame.image.load("./assets/Imagens/Espátula 300.png")

    def desenhar(self, tela):
        tela.blit(pygame.transform.scale(self.imagem_espatula, (self.largura, self.altura)), (self.posicao.x, self.posicao.y))

    def movimento_parabolico(self, gravidade):
        self.atualiza(self.vx, self.vy)
        self.vy += gravidade

    def reinicia(self):
        super().reinicia_item()