import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Personagem:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.color = (255, 0, 0)
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 0.5
        
    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity_x = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.velocity_x = self.speed
        else:
            self.velocity_x = 0  # Zera a velocidade horizontal se nenhuma tecla esquerda ou direita for pressionada

            
    def update(self):
        
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        # Verifique se o personagem atingiu os limites da tela
        if self.x < 0:  # Se o personagem sair pela esquerda
            self.x = 0
        elif self.x + self.width > SCREEN_WIDTH:  # Se o personagem sair pela direita
            self.x = SCREEN_WIDTH - self.width

        if self.y < 0:  # Se o personagem sair pelo topo
            self.y = 0
        elif self.y + self.height > SCREEN_HEIGHT:  # Se o personagem sair pelo fundo
            self.y = SCREEN_HEIGHT - self.height
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))