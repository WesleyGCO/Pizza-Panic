from adapters.primary import pygame_output_adapter

def menu_borda_ui(tela_altura, tela_largura):
    
    pygame_output_adapter.desenhar_retangulo((0, 0, 0), (0, 0, tela_altura, tela_largura), 7)
    
    menu_superior = pygame_output_adapter.criar_superficie(tela_altura)
    pygame_output_adapter.preencher_superficie(menu_superior, (77, 68, 57))
    pygame_output_adapter.desenhar_superficie(menu_superior, (0, 0))