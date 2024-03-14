import pygame

class Jogo_Servico:
  
    pygame.init()
    def menu_borda(self, tela, tela_altura, tela_largura):
        # Desenha a borda
        pygame.draw.rect(tela, (0, 0, 0), (0, 0, tela_altura, tela_largura), 7)

        self.menu_superior = pygame.Surface((tela_altura, 50))
        self.menu_superior.fill((77, 68, 57))

        tela.blit(self.menu_superior, (0, 0))