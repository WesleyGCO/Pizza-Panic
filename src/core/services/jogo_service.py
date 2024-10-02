from core.interfaces.JogoInterface import JogoInterface

from adapters.primary import pygame_output_adapter
from adapters.primary.use_cases import gerenciar_jogo

class JogoService(JogoInterface):
    def __init__(self, settings):
        self.tamanho_tela_altura = settings['video']['screen_width']
        self.tamanho_tela_largura = settings['video']['screen_height']
        pygame_output_adapter.iniciar()
        
        self.tela = pygame_output_adapter.criar_tela((self.tamanho_tela_altura, self.tamanho_tela_largura))
        pygame_output_adapter.criar_titulo("Pizza Panic")

    def iniciar_jogo(self):        
        gerenciar_jogo.iniciar_jogo(self.tamanho_tela_largura, self.tamanho_tela_altura)
                
    def encerrar_jogo(self):
        pygame_output_adapter.sair()