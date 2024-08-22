from adapters.primary.ui.fase_ui import FaseUI
from adapters.primary.ui.jogo_ui import JogoUI
from application.models.Jogo import Jogo

from core.interfaces.JogoInterface import JogoInterface
from core.services.item_service import ItemService
from core.services.personagem_service import PersonagemService

from adapters.primary import pygame_output_adapter
from adapters.primary.use_cases import gerenciar_fase

class JogoService(JogoInterface):
    def __init__(self, settings):
        self.jogo_model = Jogo()
        self.personagem_service = PersonagemService()
        self.item_service = ItemService()
        self.tamanho_tela_altura = settings['video']['screen_width']
        self.tamanho_tela_largura = settings['video']['screen_height']
        
    def iniciar_jogo(self):
        pygame_output_adapter.iniciar()
        
        self.tela = pygame_output_adapter.criar_tela((self.tamanho_tela_altura, self.tamanho_tela_largura))
        pygame_output_adapter.criar_titulo("Pizza Panic")
        
        self.jogo_ui = JogoUI(self.tamanho_tela_largura, self.tamanho_tela_altura, self.item_service, self.personagem_service)
        self.fase_ui = FaseUI(self.tamanho_tela_altura, self.tamanho_tela_largura, self.jogo_model.relogio, self.jogo_model.posicao_x_texto, self.jogo_model.posicao_y_texto)
        
        rodando_jogo = True
        while rodando_jogo:
            if (self.jogo_ui.rodar_menu_inicial()):
                gerenciar_fase.setar_fase(self.jogo_model, 1)
                gerenciar_fase.iniciar_fase(self.jogo_model, self.jogo_ui, 
                                            self.fase_ui, self.item_service, self.personagem_service)
                
            # if (self.jogo_model.fase_atual == 6):
            #     print("Entrei aqui")
            #     self.encerrar_jogo()
                    
        pygame_output_adapter.sair()
                
    def encerrar_jogo(self):
        self.jogo_ui.rodar_menu_inicial()