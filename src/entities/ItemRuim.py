import pygame, random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class ItemRuim:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.radius = 25
        self.color = (0, 0, 255)
        self.speed_x = 2
        
    def update(self):
        # Atualiza a posição horizontal (movimento reto)
        self.x += self.speed_x

        # Calcula o deslocamento vertical baseado na posição atual em x (parábola)
        displacement = (self.x - self.start_x) ** 2 / \
            800  # Ajuste o valor conforme necessário
        self.y = self.start_y + displacement

        # Verifica se a bola azul ultrapassou a tela
        if self.x - self.radius >= SCREEN_WIDTH or self.y - self.radius >= SCREEN_HEIGHT:
            # Redefine a posição da bola azul para a posição inicial
            self.x = self.start_x
            self.y = self.start_y
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def draw_personagem(self, screen, personagem_x, personagem_y):
        pygame.draw.circle(screen, self.color, (personagem_x, personagem_y), self.radius)
    
    def reseta_posicao(self):
        # Redefine a posição do item ruim para a posição inicial
        self.x = self.start_x
        self.y = self.start_y