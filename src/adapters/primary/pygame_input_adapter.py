import pygame #type: ignore

def capturar_eventos():
    return pygame.event.get()

def capturar_tecla():
    keys = pygame.key.get_pressed()
    informacao_dado = {
        'esquerda': keys[pygame.K_LEFT],
        'direita': keys[pygame.K_RIGHT],
    }
    return informacao_dado

def eh_sair(evento):
    if (evento.type == pygame.QUIT):
        return True
    else:
        return False
    
def clicado(evento):
    if (evento.type == pygame.MOUSEBUTTONDOWN):
        return True
    else:
        return False
    
def mouse_posicao():
    return pygame.mouse.get_pos()