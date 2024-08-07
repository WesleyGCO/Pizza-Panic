import pygame #type: ignore

class MenuBordaUI:
    def menuBordaUI(tela, tela_altura, tela_largura):
            # Desenha a borda
            pygame.draw.rect(tela, (0, 0, 0), (0, 0, tela_altura, tela_largura), 7)

            menu_superior = pygame.Surface((tela_altura, 50))
            menu_superior.fill((77, 68, 57))

            tela.blit(menu_superior, (0, 0))