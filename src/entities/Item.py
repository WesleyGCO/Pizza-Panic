import pygame, random
from entities.Objeto import Objeto

class Item(Objeto):
    def __init__(self, x, y, largura, altura, vx, vy):
        super().__init__(x, y, largura, altura)
        self.vx = vx
        self.vy = vy
        self.start_x = self.posicao.x
        self.start_y = self.posicao.y
    
    def desenhar(self, screen, imagem):
        screen.blit(pygame.transform.scale(imagem, (self.largura, self.altura)), (self.posicao.x, self.posicao.y))

    def movimento_parabolico(self, gravidade):
        self.atualiza(self.vx, self.vy)
        self.vy += gravidade

    def reinicia_item(self):
        self.posicao.x = self.start_x
        self.posicao.y = self.start_y
        self.vx = random.uniform(2, 5)
        self.vy = -12