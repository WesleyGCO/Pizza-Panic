import pygame
from entities.PygameInterface import PygameInterface

class PygameAdaptador(PygameInterface):
    def __init__():
        pygame.init()

    def init(self):
        pass

    def criar_tela(self, altura, largura):
        return pygame.display.set_mode(altura, largura)
    
    def define_titulo(self, titulo):
        pygame.display.set_caption(titulo)

    def carregar_imagem(self, caminho):
        return pygame.image.load(caminho)
    
    def capturar_evento(self):
        return pygame.event.get()
    
    def sair(self):
        pygame.quit()
    
    def capturar_tecla(self):
        return pygame.key.get_pressed()
    
    def atualizar_tela(self):
        pygame.display.flip()

    def criar_clock(self):
        pygame.time.Clock()