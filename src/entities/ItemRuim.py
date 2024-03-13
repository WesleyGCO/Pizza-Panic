import pygame, random
from entities.Vetor import Vetor

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class ItemRuim(Vetor):
    def __init__(self, x, y, vx, vy):
        super().__init_ItemRuim__(x, y)
    
        self.vx = vx
        self.vy = vy
        self.largura = 40
        self.altura = 40
        self.start_x = x
        self.start_y = y
    
    def desenhar(self, screen, imagem):
        screen.blit(pygame.transform.scale(imagem, (self.largura, self.altura)), (self.x, self.y))
    
    def reseta_posicao(self):
        # Redefine a posição do item ruim para a posição inicial
        self.x = self.start_x
        self.y = self.start_y

    def movimento_parabolico(self, gravidade):
        self.atualiza(self.vx, self.vy)
        self.vy += gravidade  # Simulação da aceleração devido à gravidade

    def reinicia(self):
        self.x = 0  # Volta para a posição inicial 0x
        self.y = 300  # Volta para a posição inicial 300y
        self.vx = random.uniform(2, 5)  # Velocidade horizontal aleatória
        self.vy = -10  # Velocidade vertical inicial para a trajetória parabólica