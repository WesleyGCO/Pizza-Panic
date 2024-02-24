import pygame, random
from entities.ItemRuim import ItemRuim
from entities.Personagem import Personagem

class Jogo:
    def __init__(self):
        # Configurações da janela
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption("Pizza Panic")

        self.relogio = pygame.time.Clock()
        self.personagem = Personagem(500, 500)
        self.itemRuim = ItemRuim(0, 300)

        self.is_running = False

    def init(self):
        # Inicializa o Pygame
        pygame.init()

        # Variável para controlar a execução do jogo
        self.is_running = True

    def run(self):
        # Executa o loop principal do jogo
        while self.is_running:
            self.handle_input()
            self.update()
            self.render()
            self.personagem.handle_input()
            self.personagem.update()
            self.itemRuim.update()
            
            self.screen.fill((255, 255, 255))
            self.personagem.draw(self.screen)
            
            self.itemRuim.draw(self.screen)
            
            pygame.display.flip()

    def handle_input(self):
        # Lida com a entrada do jogador
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        # Atualiza o estado do jogo
        pass

    def render(self):
        # Renderiza o estado do jogo na tela
        self.screen.fill((255, 255, 255))
        self.personagem.draw(self.screen)
        self.itemRuim.draw(self.screen)
        pygame.display.flip()

    def cleanup(self):
        # Limpa recursos alocados pelo jogo
        pygame.quit()
