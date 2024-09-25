from adapters.primary import pygame_output_adapter
from core.services import randomizacao_service
from application.models.Item import Item

def criar_item():
    tipo_item = randomizacao_service.escolher_item()
    x, y = randomizacao_service.gerar_posicao_aleatoria()
    return Item(tipo_item, 0, 300, 40, 40, x, y)
    
def desenhar_rodar_item(item, angulo):
    pygame_output_adapter.desenhar_rodar_item(item, angulo)