from adapters.primary import pygame_output_adapter
from adapters.primary.ui.fase_ui import FaseUI
from adapters.primary.ui.jogo_ui import JogoUI
from adapters.primary.use_cases import gerenciar_fase, gerenciar_menus
from application.models.Jogo import Jogo
from adapters.primary.ui.menu_fase_ui import MenuFaseUI
from adapters.primary.ui.menu_inicial_ui import MenuInicialUI
from core.services.item_servico import ItemService
from core.services.personagem_servico import PersonagemService
from core.services.tempo_servico import TempoService

def iniciar_jogo(tamanho_tela_largura, tamanho_tela_altura):
    jogo_model = Jogo()
    personagem_servico = PersonagemService()
    item_servico = ItemService()
    tempo_servico = TempoService()
    menu_inicial = MenuInicialUI(tamanho_tela_altura, tamanho_tela_largura)
    menu_fase = MenuFaseUI(tamanho_tela_largura, tamanho_tela_altura)
    
    while True:
        if (gerenciar_menus.rodar_menu_inicial(menu_inicial)):
            jogo_ui = JogoUI(tamanho_tela_largura, tamanho_tela_altura, item_servico, personagem_servico)
            fase_ui = FaseUI(tamanho_tela_altura, tamanho_tela_largura, jogo_model.relogio, jogo_model.posicao_x_texto, jogo_model.posicao_y_texto)
    
            executar_jogo(jogo_model, jogo_ui, fase_ui, menu_fase, item_servico, personagem_servico, tempo_servico, tamanho_tela_largura, tamanho_tela_altura)
            break

def executar_jogo(jogo_model, jogo_ui, fase_ui, menu_fase, item_servico, personagem_servico, tempo_servico,
                  tamanho_tela_largura, tamanho_tela_altura):
    while True:
            gerenciar_fase.setar_fase(jogo_model, 1)
            if not (gerenciar_fase.iniciar_fase(menu_fase, jogo_model, jogo_ui, fase_ui, 
                                        item_servico, personagem_servico, tempo_servico, tamanho_tela_largura, tamanho_tela_altura)):
                pygame_output_adapter.preencher_tela((0,0,0))
                iniciar_jogo(tamanho_tela_largura, tamanho_tela_altura)
                break

def encerrar_jogo():
    pygame_output_adapter.sair()
    
def setar_jogo_perdido(jogo_model):
    jogo_model.fase_perdida = True
