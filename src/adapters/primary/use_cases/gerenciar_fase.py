from adapters.primary import pygame_output_adapter
from application.models.Fase import Fase
from core.services.fase_service import FaseService


def setar_fase(jogo_model, numero_fase):
    jogo_model.fase_atual = numero_fase
  
def criar_fase(numero_fase, personagem, itens_ruins):
    tempo_inicial = 60  
    pedido = 3 + (numero_fase - 1) * 5  
    
    return Fase(numero_fase, personagem, itens_ruins, tempo_inicial, pedido)

def iniciar_fase(jogo_model, jogo_ui, fase_ui, item_service, personagem_service):
    while True:  
        fase = criar_fase(jogo_model.fase_atual, jogo_ui.personagem, jogo_ui.itens_ruins)
        fase_service = FaseService(fase, fase_ui, item_service, personagem_service)
        fase_service.iniciar()

        if fase.concluida:
            fase.concluir()
            pygame_output_adapter.tocar_som("conclusao_fase")
            jogo_model.fase_atual += 1
            jogo_ui.rodar_menu_fase(jogo_model, jogo_model.fase_atual)
        else:
            break  

def verificar_conclusao_fase(fase_model):
    if fase_model.pedido == fase_model.pedido_coletado:
        fase_model.concluida = True