import pygame

class Jogo_Servico:
    
    pygame.init()
    def menu_borda(self, screen, screen_width, screen_height):
        # Desenha a borda
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen_width, screen_height), 7)

        self.menu_superior = pygame.Surface((screen_width, 50))
        self.menu_superior.fill((77, 68, 57))

        screen.blit(self.menu_superior, (0, 0))