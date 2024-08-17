import random

from application.models.Item import Item

def escolher_item():
    tipos_item = list(Item.TIPOS_ITENS.keys())
    return random.choice(tipos_item)

def gerar_posicao_aleatoria():
    return random.uniform(300, 600), random.uniform(-200, -500)